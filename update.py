import requests, json, datetime,math,random
import nlpcloud
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib.image as img

keys = {}

with open('keys.txt','r') as f:
    for line in f:
        key,value = line.split(':')
        keys[key.lower()] = value.strip()

api_url = 'https://newsapi.org/v2/top-headlines?'
d = datetime.date.today() - datetime.timedelta(days=1)
date = d.strftime('%Y-%m:%d')
url = api_url + f'from={date}&country=in&apiKey={keys["newsapi"]}'

response = requests.get(url)

a = []

data = json.loads(response.text)


a += [article["title"] for article in  data["articles"]]  
random.shuffle(a)
s =  " ".join(a)
z = " ".join(s.split(" ")[:320])



client = nlpcloud.Client("distilbert-base-uncased-finetuned-sst-2-english", keys["nlpclous"])
sentiment = client.sentiment(z)

x = sentiment["scored_labels"][0]
text = ""
if x["score"] < 0.9:
  text = "Todays news is NEUTRAL"
else:
  text = f"Todays news is {round(math.log(x['score']*100)/math.log(110)*100,2)}% {x['label']}"    

with open("sentiment", "w") as f:
  f.write(text)  


stop = set(STOPWORDS)
stop.add("Reuters")
stop.add("BBC")
stop.add("AP")
stop.add("Hindustan")
stop.add("Times")
stop.add("NDTV")
stop.add("Indian Express")


im = img.imread("red.jpg")
color = ImageColorGenerator(im)
wordcloud = WordCloud(width = 640, height = 360,
                background_color ='white',
                stopwords = stop,
                color_func=color,
                min_font_size = 10).generate(s)
 
plt.axis("off")
plt.tight_layout(pad = 0)
plt.imshow(wordcloud)
plt.savefig('static/wordcloud.png')

