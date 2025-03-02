import praw
from textblob import TextBlob
import matplotlib.pyplot as plt


reddit = praw.Reddit(
    client_id="jPWcyiuijkgzftreVsICMA",
    client_secret="x51QzHrXoPAOI8XfPW21z_5fp79C7g",
    user_agent="VibeCodingScraper/1.0 (by u/Far-Strength-2949)"
)


subreddit = reddit.subreddit("all")
posts = []
for post in subreddit.search("Modern Yazılım Geliştirmede Yapay Zeka", limit=1500):
    posts.append(post.title)


pozitif = 0
negatif = 0
nötr = 0

for post in posts:
    analiz = TextBlob(post)
    duygu = analiz.sentiment.polarity
    if duygu > 0:
        pozitif += 1
    elif duygu < 0:
        negatif += 1
    else:
        nötr += 1


etiketler = 'Pozitif', 'Negatif', 'Nötr'
boyutlar = [pozitif, negatif, nötr]
renkler = ['gold', 'lightcoral', 'lightskyblue']

plt.pie(boyutlar, labels=etiketler, colors=renkler, autopct='%1.1f%%', startangle=140)
plt.axis('equal') 
plt.title("Yazılım Geliştirmede Yapay Zeka Konusunda Reddit Gönderilerinin Sentiment Analizi")
plt.show()
