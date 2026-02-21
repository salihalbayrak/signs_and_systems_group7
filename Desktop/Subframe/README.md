# 📈 Sinüzoidal İşaretlerin Örneklenmesi ve Görselleştirilmesi 

Bu proje, sinüzoidal işaretlerin bilgisayar ortamında *örneklenerek*
nasıl temsil edildiğini incelemek amacıyla hazırlanmıştır.
Ödev kapsamında farklı frekanslardaki sinüzoidal işaretler üretilmiş,
Nyquist örnekleme teoremi dikkate alınarak örneklenmiş
ve zaman domeninde görselleştirilmiştir.


Bu projenin temel amaçları şunlardır:

- Sürekli zamanlı (analog) sinyallerin bilgisayarda *doğrudan gösterilemeyeceğini* kavramak  
- Analog sinyallerin ancak *örnekleme (sampling)* ile dijital ortama aktarılabildiğini göstermek  
- Örnekleme frekansının sinyal kalitesi üzerindeki etkisini incelemek  
- *Nyquist örnekleme teoremini* uygulamalı olarak öğrenmek  
- Birden fazla sinüzoidal işaretin *toplanmasıyla* oluşan karma sinyali gözlemlemek  

---

## 📌 Temel Frekans (f₀) Seçimi

Her grup için temel frekans \( f_0 \), grup üyelerinin okul numaralarının
son iki hanesinin toplanmasıyla belirlenmiştir.

Örnek:
- Öğrenci 1 → 24  
- Öğrenci 2 → 29  
- Öğrenci 3 → 47  

\[
f_0 = 29 + 24 + 47 = 40 \text{ Hz}
\]

Bu yöntem, her grubun farklı parametrelerle çalışmasını sağlamaktadır.

---

## 📐 Üretilen Sinyaller

Hesaplanan \( f_0 \) kullanılarak üç farklı sinüzoidal işaret üretilmiştir:

- \( f_1 = f_0 \)
- \( f_2 = \frac{f_0}{2} \)
- \( f_3 = 10 f_0 \)

Her sinyal için matematiksel ifade:

\[
x(t) = \sin(2\pi f t)
\]

---

## ⚙️ Örnekleme Frekansı ve Nyquist Teoremi

Bilgisayar ortamında sinyaller ayrık zamanlı olarak temsil edilir.
Bu nedenle sinyallerin *örneklenmesi* gerekir.

Nyquist örnekleme teoremine göre:

\[
f_s \ge 2 f_{max}
\]

Bu çalışmada en yüksek frekans:
\[
f_{max} = f_3 = 10 f_0
\]

Dolayısıyla minimum örnekleme frekansı:
\[
f_s \ge 20 f_0
\]

Grafiklerin bozulmadan ve daha düzgün elde edilebilmesi için
örnekleme frekansı güvenli tarafta seçilmiştir:

\[
f_s = 50 f_0
\]

Bu seçim sayesinde aliasing oluşmamış ve sinyaller doğru şekilde temsil edilmiştir.

---

## ⏱️ Zaman Penceresi Seçimi

Her sinyalin *en az 3 tam periyodunun* gözlemlenebilmesi için
zaman ekseni dinamik olarak ayarlanmıştır.

Bir sinyalin periyodu:
\[
T = \frac{1}{f}
\]

Her sinyal kendi periyoduna göre:
\[
t \in [0, 3T]
\]
aralığında çizilmiştir.

---

## ➕ Sinyal Toplama

Üç sinüzoidal işaret toplanarak karma bir sinyal elde edilmiştir:

\[
x_{toplam}(t) = x_1(t) + x_2(t) + x_3(t)
\]

Bu adım, gerçek hayatta karşılaşılan çok bileşenli sinyallerin
nasıl oluştuğunu göstermek amacıyla yapılmıştır.


----------------------------------------------------------------------------------


# 📞 DTMF (Dual-Tone Multi-Frequency) Sinyal Üretimi 

Bu proje, telefon tuş takımında kullanılan **DTMF (Dual-Tone Multi-Frequency)**
sistemini sayısal sinyal işleme prensipleriyle modellemektedir.
Kullanıcı etkileşimli bir arayüz üzerinden tuşa basıldığında,
ilgili DTMF sinyali üretilmekte, zaman domeninde görselleştirilmekte
ve hoparlörden ses olarak çalınmaktadır.

---



Bu projenin amaçları:

- İki sinüzoidal işaretin toplanmasıyla **anlamlı bilgi** üretildiğini göstermek  
- Telefon tuş seslerinin matematiksel modelini uygulamak  
- Nyquist örnekleme teoremini dijital ses üretiminde kullanmak  
- Kullanıcı etkileşimli bir **GUI** geliştirmek  
- Üretilen sinyali hem **grafik** hem **ses** olarak sunmak  

---

## 📌 DTMF Nedir?

DTMF, her telefon tuşunun biri düşük, diğeri yüksek frekanstan seçilen
iki sinüzoidal sinyalin toplamı ile temsil edildiği bir sistemdir:

\[
x(t)=\sin(2\pi f_{low}t)+\sin(2\pi f_{high}t)
\]

Genlik taşmasını önlemek için sinyal ölçeklenmiştir:

\[
x(t)=0.5\left(\sin(2\pi f_{low}t)+\sin(2\pi f_{high}t)\right)
\]

---

## 📊 DTMF Frekans Tablosu

|        | 1209 Hz | 1336 Hz | 1477 Hz | 1633 Hz |
|--------|---------|---------|---------|---------|
| 697 Hz | 1 | 2 | 3 | A |
| 770 Hz | 4 | 5 | 6 | B |
| 852 Hz | 7 | 8 | 9 | C |
| 941 Hz | * | 0 | # | D |

---

## ⚙️ Örnekleme Frekansı Seçimi

DTMF sisteminde en yüksek frekans **1633 Hz**’dir.
Nyquist teoremine göre:

\[
f_s \ge 2 \cdot 1633 = 3266 \text{ Hz}
\]

Bu nedenle uygulamada:

- **fs = 8000 Hz** (telekom standardı)
- (opsiyonel: 44100 Hz)

kullanılmıştır.

---

## ⏱️ Sinyal Süresi

Her tuş basımı için süre:

- **T = 0.25 s**

Örnek sayısı:

\[
N = f_s \cdot T
\]

Bu değer, sinyalin net duyulması için yeterlidir.

---

## 🖥️ Uygulama Özellikleri

- Python + Tkinter ile telefon tuş takımı arayüzü
- Tuşa basıldığında:
  - İlgili DTMF sinyalinin üretilmesi
  - Zaman domeninde grafik çizimi
  - Hoparlörden ses çıktısı
- (Opsiyonel) FFT ile frekans domeni analizi

---

## 🛠️ Kullanılan Teknolojiler

- **Python 3**
- **NumPy**
- **Matplotlib**
- **sounddevice**
- **Tkinter**

---

## ▶️ Kurulum

bash
pip install numpy matplotlib sounddevice
