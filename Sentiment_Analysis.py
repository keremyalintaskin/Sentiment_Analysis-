import praw
from textblob import TextBlob
import matplotlib.pyplot as plt

# Reddit API'ye bağlanma
reddit = praw.Reddit(
    client_id="jPWcyiuijkgzftreVsICMA",
    client_secret="x51QzHrXoPAOI8XfPW21z_5fp79C7g",
    user_agent="VibeCodingScraper/1.0 (by u/Far-Strength-2949)"
)

# "Modern Yazılım Geliştirmede Yapay Zeka" başlığıyla arama yap
subreddit = reddit.subreddit("all")
posts = []
for post in subreddit.search("Modern Yazılım Geliştirmede Yapay Zeka", limit=1500):
    posts.append(post.title)

# Sentiment analizi yapalım
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

# Sonuçları görselleştirelim
etiketler = 'Pozitif', 'Negatif', 'Nötr'
boyutlar = [pozitif, negatif, nötr]
renkler = ['gold', 'lightcoral', 'lightskyblue']

plt.pie(boyutlar, labels=etiketler, colors=renkler, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Eşit dağılımda çizim
plt.title("Yazılım Geliştirmede Yapay Zeka Konusunda Reddit Gönderilerinin Sentiment Analizi")
plt.show()
