📈 Sinüzoidal İşaretlerin Örneklenmesi ve Görselleştirilmesi

Bu proje, sinüzoidal işaretlerin bilgisayar ortamında örneklenerek nasıl temsil edildiğini incelemek amacıyla hazırlanmıştır. Ödev kapsamında farklı frekanslardaki sinüzoidal işaretler üretilmiş, Nyquist örnekleme teoremi dikkate alınarak örneklenmiş ve zaman domeninde görselleştirilmiştir.

Bu projenin temel amaçları şunlardır:

Sürekli zamanlı (analog) sinyallerin bilgisayarda doğrudan gösterilemeyeceğini kavramak

Analog sinyallerin ancak örnekleme (sampling) ile dijital ortama aktarılabildiğini göstermek

Örnekleme frekansının sinyal kalitesi üzerindeki etkisini incelemek

Nyquist örnekleme teoremini uygulamalı olarak öğrenmek

Birden fazla sinüzoidal işaretin toplanmasıyla oluşan karma sinyali gözlemlemek

📌 Temel Frekans (f₀) Seçimi

Her grup için temel frekans 
𝑓
0
f
0
	​

, grup üyelerinin okul numaralarının son iki hanesinin toplanmasıyla belirlenmiştir.

Örnek:

Öğrenci 1 → 24

Öğrenci 2 → 29

Öğrenci 3 → 47

Toplam:

24 + 29 + 47 = 100

Dolayısıyla:

f₀ = 100 Hz

(Not: Önceki örnekte toplam 40 Hz olarak yazılmıştı; bu matematiksel olarak hatalıydı.)

Bu yöntem, her grubun farklı parametrelerle çalışmasını sağlamaktadır.

📐 Üretilen Sinyaller

Hesaplanan 
𝑓
0
f
0
	​

 kullanılarak üç farklı sinüzoidal işaret üretilmiştir:

𝑓
1
=
𝑓
0
f
1
	​

=f
0
	​


𝑓
2
=
𝑓
0
/
2
f
2
	​

=f
0
	​

/2

𝑓
3
=
10
𝑓
0
f
3
	​

=10f
0
	​


Her sinyal için matematiksel ifade:

x(t) = sin(2π f t)

⚙️ Örnekleme Frekansı ve Nyquist Teoremi

Bilgisayar ortamında sinyaller ayrık zamanlı olarak temsil edilir. Bu nedenle sinyallerin örneklenmesi gerekir.

Nyquist örnekleme teoremine göre:

f_s ≥ 2 f_max

Bu çalışmada en yüksek frekans:

f_max = f_3 = 10 f_0

Dolayısıyla minimum örnekleme frekansı:

f_s ≥ 20 f_0

Grafiklerin daha düzgün elde edilebilmesi ve aliasing oluşmaması için örnekleme frekansı güvenli tarafta seçilmiştir:

f_s = 50 f_0

Bu seçim Nyquist kriterini fazlasıyla sağlamaktadır ve özellikle yüksek frekanslı f₃ sinyalinde bozulmayı engellemektedir.

⏱️ Zaman Penceresi Seçimi

Her sinyalin en az 3 tam periyodunun gözlemlenebilmesi için zaman ekseni dinamik olarak ayarlanmıştır.

Bir sinyalin periyodu:

T = 1 / f

Bu nedenle her sinyal için zaman aralığı:

t ∈ [0, 3T]

şeklinde belirlenmiştir.

➕ Sinyal Toplama

Üç sinüzoidal işaret toplanarak karma bir sinyal elde edilmiştir:

x_toplam(t) = x₁(t) + x₂(t) + x₃(t)

Bu işlem, gerçek hayatta karşılaşılan çok bileşenli sinyallerin nasıl oluştuğunu göstermek amacıyla yapılmıştır.

📞 DTMF (Dual-Tone Multi-Frequency) Sinyal Üretimi

Bu proje, telefon tuş takımında kullanılan DTMF (Dual-Tone Multi-Frequency) sistemini sayısal sinyal işleme prensipleriyle modellemektedir. Kullanıcı etkileşimli bir arayüz üzerinden tuşa basıldığında, ilgili DTMF sinyali üretilmekte, zaman domeninde görselleştirilmekte ve hoparlörden ses olarak çalınmaktadır.

Bu projenin amaçları:

İki sinüzoidal işaretin toplanmasıyla anlamlı bilgi üretildiğini göstermek

Telefon tuş seslerinin matematiksel modelini uygulamak

Nyquist örnekleme teoremini dijital ses üretiminde kullanmak

Kullanıcı etkileşimli bir GUI geliştirmek

Üretilen sinyali hem grafik hem ses olarak sunmak

📌 DTMF Nedir?

DTMF sisteminde her telefon tuşu biri düşük, diğeri yüksek frekans grubundan seçilen iki sinüzoidal sinyalin toplamı ile temsil edilir:

x(t) = sin(2π f_low t) + sin(2π f_high t)

İki sinyalin toplamı maksimum ±2 genliğe ulaşabileceği için clipping oluşmaması amacıyla sinyal ölçeklendirilmiştir:

x(t) = 0.5 [ sin(2π f_low t) + sin(2π f_high t) ]

📊 DTMF Frekans Tablosu
    1209   1336   1477   1633  

697 1 2 3 A
770 4 5 6 B
852 7 8 9 C
941 * 0 # D

⚙️ Örnekleme Frekansı Seçimi

DTMF sisteminde en yüksek frekans 1633 Hz’dir.

Nyquist teoremine göre:

f_s ≥ 2 × 1633 = 3266 Hz

Bu nedenle uygulamada:

fs = 8000 Hz

seçilmiştir.

8000 Hz değeri hem Nyquist kriterini sağlamaktadır hem de telekomünikasyon sistemlerinde kullanılan standart örnekleme frekansıdır.

⏱️ Sinyal Süresi

Her tuş basımı için sinyal süresi:

T = 0.25 saniye

Örnek sayısı:

N = f_s × T

Bu süre, DTMF tonunun net ve anlaşılır duyulması için yeterlidir.

🖥️ Uygulama Özellikleri

Python + Tkinter ile telefon tuş takımı arayüzü

Tuşa basıldığında:

İlgili DTMF sinyalinin üretilmesi

Zaman domeninde grafik çizimi

Hoparlörden ses çıktısı

(Opsiyonel) FFT ile frekans domeni analizi

🛠️ Kullanılan Teknolojiler

Python 3

NumPy

Matplotlib

sounddevice

Tkinter

▶️ Kurulum

Komut satırında aşağıdaki komut çalıştırılmalıdır:

pip install numpy matplotlib sounddevice
