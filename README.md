# Yazılım Geliştirmede Yapay Zeka Konusunda Reddit Gönderilerinin Sentiment Analizi

Bu proje, Reddit API'si kullanarak "Modern Yazılım Geliştirmede Yapay Zeka" başlığıyla ilgili 1500 Reddit gönderisini toplar ve metin tabanlı sentiment analizi yapar. Sonuçlar, pozitif, negatif ve nötr duygu kategorilerine ayrılır ve görselleştirilir.

## İçindekiler
- [Proje Hakkında](#proje-hakkında)
- [Kullanılan Teknolojiler](#kullanılan-teknolojiler)
- [Kurulum ve Çalıştırma](#kurulum-ve-çalıştırma)
  - [Gereksinimler](#gereksinimler)
  - [Reddit API Bağlantısı](#reddit-api-bağlantısı)
  - [Çalıştırma](#çalıştırma)
- [Proje Detayları](#proje-detayları)
  - [Analiz Sonuçları](#analiz-sonuçları)
  - [Görselleştirme](#görselleştirme)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Proje Hakkında
Bu proje, Reddit platformundan 1500 gönderi başlığı çekip bu başlıklar üzerinde TextBlob kütüphanesi ile sentiment analizi yapar. Sentiment analizi sonucunda başlıklar pozitif, negatif ve nötr olarak sınıflandırılır. Sonuçlar, Matplotlib kütüphanesi kullanılarak bir pasta grafiği ile görselleştirilir.

## Kullanılan Teknolojiler
- **Python**: Proje için kullanılan ana programlama dili.
- **Praw (Python Reddit API Wrapper)**: Reddit API'si ile etkileşim için kullanılır.
- **TextBlob**: Sentiment analizi yapabilmek için kullanılır.
- **Matplotlib**: Analiz sonuçlarını görselleştirmek için kullanılır.

## Kurulum ve Çalıştırma

### Gereksinimler
Projeyi çalıştırmak için aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:
```bash
pip install praw textblob matplotlib
```

### Reddit API Bağlantısı
Reddit API'sine bağlanabilmek için, aşağıdaki bilgileri temin etmeniz gerekmektedir:

client_id: Reddit API anahtarınız  
client_secret: Reddit API gizli anahtarınız  
user_agent: Kullanıcı tanımlayıcı bir ajans ismi  

Bu bilgileri Reddit API üzerinden alabilirsiniz. Alınan bu bilgileri proje dosyasına yerleştirmeniz gerekir.

### Çalıştırma
Projeyi çalıştırmak için:

1. Bu proje dosyasını bilgisayarınıza indirin.
2. Yukarıda belirttiğimiz Reddit API bilgilerini doğru bir şekilde client_id, client_secret ve user_agent alanlarında belirtin.
3. Aşağıdaki komut ile projeyi çalıştırın:
4. ```bash
   python sentiment_analysis_reddit.py
   ```

Proje çalıştırıldığında, Reddit gönderilerinin başlıkları üzerinde sentiment analizi yapılacak ve bir pasta grafiği ile görselleştirilecektir.

## Proje Detayları

### Analiz Sonuçları
Sentiment analizi sonuçları üç kategoriye ayrılır:
- **Pozitif**: Pozitif duygusal içerik taşıyan başlıklar.
- **Negatif**: Negatif duygusal içerik taşıyan başlıklar.
- **Nötr**: Nötr duygusal içerik taşıyan başlıklar.

Bu üç kategori, sayılarla ifade edilerek pasta grafiği şeklinde görselleştirilir.

### Görselleştirme
Sonuçlar, Matplotlib kullanılarak aşağıdaki şekilde görselleştirilir:
- **Pozitif** duygu içeren başlıklar altın sarısı renk ile,
- **Negatif** duygu içeren başlıklar açık kırmızı renk ile,
- **Nötr** duygu içeren başlıklar ise açık mavi renk ile gösterilir.

Pasta grafiği, her kategorinin yüzdesini görsel olarak sunar.

![sentiment_analys_gorsel](https://github.com/user-attachments/assets/27ea097d-5bd2-439a-9902-825fd8bab706)

## Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin. Yardımcı olmak veya önerilerde bulunmak için proje ile ilgili herhangi bir soruyu açabilirsiniz.

## Lisans
Bu proje, MIT Lisansı ile lisanslanmıştır.

