import os
from wordcloud import WordCloud


tweetsfile = open(os.path.join("output", "tweets_python.txt"))
text = tweetsfile.read()
tweetsfile.close()

wordcloud = WordCloud().generate(text)

image = wordcloud.to_image()
image.save(os.path.join("output", "python_cloud.png"))
