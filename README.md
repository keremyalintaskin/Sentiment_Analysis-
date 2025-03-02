Yazılım Geliştirmede Yapay Zeka Konusunda Reddit Gönderilerinin Sentiment Analizi
Bu proje, Reddit API'si kullanarak "Modern Yazılım Geliştirmede Yapay Zeka" başlığıyla ilgili 1500 Reddit gönderisini toplayıp, metin bazlı sentiment analizi yapmaktadır. Ardından bu analiz sonuçlarını görselleştirir. Kullanılan sentiment analizi algoritması, metinlerin pozitif, negatif veya nötr duygu içerip içermediğini belirler.

Kullanılan Teknolojiler
Python: Programlama dili
Praw (Python Reddit API Wrapper): Reddit API ile etkileşim için
TextBlob: Sentiment analizi için
Matplotlib: Sonuçların görselleştirilmesi için
Kurulum ve Çalıştırma
Gereksinimler
Projeyi çalıştırmadan önce aşağıdaki Python kütüphanelerini yüklemeniz gerekir:

bash
Kopyala
Düzenle
pip install praw textblob matplotlib
Reddit API Bağlantısı
Reddit API'sine bağlanabilmek için client_id, client_secret ve user_agent bilgilerinizi almanız gerekir. Reddit API üzerinden bir uygulama oluşturup bu bilgileri edinmeniz gerekmektedir.

client_id: Reddit API anahtarı
client_secret: Reddit API gizli anahtarı
user_agent: Kullanıcı tanımlayıcı bir ajans ismi
Bu bilgileri reddit objesini oluştururken kodun içinde belirttiğiniz gibi kullanabilirsiniz.

Çalıştırma
Proje dosyasını bilgisayarınıza indirin.
API bilgilerinizi doğru bir şekilde yerleştirdiğinizden emin olun.
Kod dosyasını çalıştırarak Reddit gönderilerinin başlıkları üzerinde sentiment analizi yapın.
bash
Kopyala
Düzenle
python sentiment_analysis_reddit.py
Proje çalıştırıldığında, Reddit gönderilerinin sentiment analizine ait sonuçlar bir pasta grafiği ile görselleştirilecektir.

Proje Detayları
Bu proje, Reddit üzerinden "Modern Yazılım Geliştirmede Yapay Zeka" konusundaki gönderilerin başlıklarını toplar. Sonra, bu başlıklar üzerinde TextBlob kütüphanesi ile sentiment analizi yapılır. Bu analiz, başlıkların pozitif, negatif ve nötr duygu içerip içermediğini belirler ve her bir kategorinin sayısal değerlerini toplar.

Son olarak, bu sonuçlar Matplotlib ile bir pasta grafiği şeklinde görselleştirilir.

Analiz Sonuçları
Pozitif: Gönderilerin pozitif duygusal içerik taşıyan başlıkları
Negatif: Gönderilerin negatif duygusal içerik taşıyan başlıkları
Nötr: Gönderilerin nötr duygusal içerik taşıyan başlıkları
Görselleştirme
Sonuçlar, bir pasta grafiği ile görselleştirilir. Grafikte:

Pozitif duygu içeren başlıklar altın renk ile,
Negatif duygu içeren başlıklar açık kırmızı renk ile,
Nötr duygu içeren başlıklar ise açık mavi renk ile gösterilmektedir.
Katkıda Bulunma
Bu projeye katkıda bulunmak isterseniz, lütfen bir pull request gönderin. Yardımcı olmak veya önerilerde bulunmak için proje ile ilgili herhangi bir soruyu açabilirsiniz.

Lisans
Bu proje, MIT Lisansı ile lisanslanmıştır.
