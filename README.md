Yazılım Geliştirmede Yapay Zeka Konusunda Reddit Gönderilerinin Sentiment Analizi
Bu proje, Reddit API'si kullanarak "Modern Yazılım Geliştirmede Yapay Zeka" başlığıyla ilgili 1500 Reddit gönderisini toplar ve metin tabanlı sentiment analizi yapar. Sonuçlar, pozitif, negatif ve nötr duygu kategorilerine ayrılır ve görselleştirilir.

İçindekiler
Proje Hakkında
Kullanılan Teknolojiler
Kurulum ve Çalıştırma
Gereksinimler
Reddit API Bağlantısı
Çalıştırma
Proje Detayları
Analiz Sonuçları
Görselleştirme
Katkıda Bulunma
Lisans
Proje Hakkında
Bu proje, Reddit platformundan 1500 gönderi başlığı çekip bu başlıklar üzerinde TextBlob kütüphanesi ile sentiment analizi yapar. Sentiment analizi sonucunda başlıklar pozitif, negatif ve nötr olarak sınıflandırılır. Sonuçlar, Matplotlib kütüphanesi kullanılarak bir pasta grafiği ile görselleştirilir.

Kullanılan Teknolojiler
Python: Proje için kullanılan ana programlama dili.
Praw (Python Reddit API Wrapper): Reddit API'si ile etkileşim için kullanılır.
TextBlob: Sentiment analizi yapabilmek için kullanılır.
Matplotlib: Analiz sonuçlarını görselleştirmek için kullanılır.
Kurulum ve Çalıştırma
Gereksinimler
Projeyi çalıştırmak için aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:

bash
Kopyala
Düzenle
pip install praw textblob matplotlib
Reddit API Bağlantısı
Reddit API'sine bağlanabilmek için, aşağıdaki bilgileri temin etmeniz gerekmektedir:

client_id: Reddit API anahtarınız
client_secret: Reddit API gizli anahtarınız
user_agent: Kullanıcı tanımlayıcı bir ajans ismi
Bu bilgileri Reddit API üzerinden alabilirsiniz. Alınan bu bilgileri proje dosyasına yerleştirmeniz gerekir.

Çalıştırma
Projeyi çalıştırmak için:

Bu proje dosyasını bilgisayarınıza indirin.
Yukarıda belirttiğimiz Reddit API bilgilerini doğru bir şekilde client_id, client_secret ve user_agent alanlarında belirtin.
Aşağıdaki komut ile projeyi çalıştırın:
bash
Kopyala
Düzenle
python sentiment_analysis_reddit.py
Proje çalıştırıldığında, Reddit gönderilerinin başlıkları üzerinde sentiment analizi yapılacak ve bir pasta grafiği ile görselleştirilecektir.

Proje Detayları
Proje, Reddit platformunda "Modern Yazılım Geliştirmede Yapay Zeka" başlığıyla ilgili gönderilerin başlıklarını toplar. TextBlob kullanarak, her bir başlık üzerinde sentiment analizi yapılır. Analiz sonuçları, başlığın pozitif, negatif veya nötr duygu taşıyıp taşımadığını belirler.

Analiz Sonuçları
Sentiment analizi sonuçları üç kategoriye ayrılır:

Pozitif: Pozitif duygusal içerik taşıyan başlıklar.
Negatif: Negatif duygusal içerik taşıyan başlıklar.
Nötr: Nötr duygusal içerik taşıyan başlıklar.
Bu üç kategori, sayılarla ifade edilerek pasta grafiği şeklinde görselleştirilir.

Görselleştirme
Sonuçlar, Matplotlib kullanılarak aşağıdaki şekilde görselleştirilir:

Pozitif duygu içeren başlıklar altın sarısı renk ile,
Negatif duygu içeren başlıklar açık kırmızı renk ile,
Nötr duygu içeren başlıklar ise açık mavi renk ile gösterilir.
Pasta grafiği, her kategorinin yüzdesini görsel olarak sunar.

Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin. Yardımcı olmak veya önerilerde bulunmak için proje ile ilgili herhangi bir soruyu açabilirsiniz.

Lisans
Bu proje, MIT Lisansı ile lisanslanmıştır.
