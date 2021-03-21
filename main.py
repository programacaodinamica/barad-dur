import os
from searchtweets import load_credentials, ResultStream, gen_request_parameters
from searchtweets import collect_results


keymap = {
    "SEARCHTWEETS_BEARER_TOKEN": os.path.join("credentials", "bearertoken"),
    "SEARCHTWEETS_CONSUMER_KEY": os.path.join("credentials", "apikey"),
    "SEARCHTWEETS_CONSUMER_SECRET": os.path.join("credentials", "apisecret")
}

OUT_DIR = "output"

for key, value in keymap.items():
    with open(value, "r") as credfile:
        os.environ[key] = credfile.read()

stream_args = load_credentials(filename="config.yaml",
                 yaml_key="search_tweets_pgdinamica",
                 env_overwrite=True)

LIMIT = 100
search_term = "python"

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)

for day in range(14, 21):
    query = gen_request_parameters(f"{search_term} lang:pt", 
                                start_time=f"2021-03-{day} 09:00",
                                results_per_call=LIMIT)

    tweets = collect_results(query, 
                    max_tweets=LIMIT,
                    result_stream_args=stream_args)

    print(f"{len(tweets)} resultados no dia {day}")

    with open(os.path.join(OUT_DIR, 
                f"tweets_{search_term}.txt"), "a") as tweetsfile:
        lines = [tweet['text'] for tweet in tweets if 'text' in tweet]
        tweetsfile.writelines(lines)

print("FIM")
    

