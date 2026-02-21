# Sinüzoidal İşaretlerin Örneklenmesi ve DTMF Uygulaması

Bu depo, elektrik mühendisliği veya bilgisayar mühendisliği dersleri kapsamında hazırlanan
iki ayrı sinyal işleme ödevini içerir. Amaç hem temel frekanslı sinyallerin örneklenmesi
ile ilgili teoriyi pekiştirmek hem de pratikte DTMF ton üretimini gösterebilmektir.

> 🚩 **Not:** Dosyalar `gorev1.py` ve `gorev2.py` isimleriyle repo kökünde bulunur. Bu
> README belgesi de kök dizinde yer almalıdır.

---

## 📘 Ödev 1 – Örnekleme ve Sinüs Sinyalleri

Bu script (`gorev1.py`) aşağıdaki adımları gerçekleştirir:

1. Kullanıcı grubunun temel frekansı `f0` belirlenir (örnek olarak 100 Hz yazılmıştır).
2. Üç sinüs sinyali tanımlanır:
   - `f1 = f0`
   - `f2 = f0 / 2`
   - `f3 = 10 * f0`
3. Nyquist örnekleme teoremi (`fs >= 2 * f_max`) göz önüne alınarak örnekleme frekansı
   seçilir. Bu proje için güvenli bir değer olarak `fs = 50 * f0` kullanılmıştır.
4. Her sinyal için üç periyotluk zaman penceresi üzerinden örnekler alınır ve
   matplotlib ile çizilir.
5. Tüm sinyallerin toplam değeri hesaplanarak dördüncü bir grafik olarak gösterilir.

### Kullanım
```bash
python gorev1.py
```
Çalıştırıldığında dört alt pencerede zaman domeni grafikleri açılır. Kod içinde `f0`,
`fs` gibi parametreler kolayca düzenlenebilir.

### Teorik Arka Plan
- **Periyot**: `T = 1 / f`
- **Nyquist Teoremi**: `fs >= 2 * f_max`; burada `f_max` en yüksek bileşen frekansıdır.
- **Karma Sinyal**: `x_sum(t) = x1(t) + x2(t) + x3(t)`. Farklı frekanslı bileşenlerin
  toplamı genellikle karmaşık dalgalar üretir.

---

## 📗 Ödev 2 – DTMF Telefon Tuş Takımı

`gorev2.py` dosyası, bir telefon tuş takımının DTMF tonlarını üretmek için interaktif
gorünüm sağlar. Tkinter ile basit bir GUI oluşturulur ve kullanıcı tuşa bastığında ilgili
ses çalınır.

### Özellikler
- Standart DTMF frekans tablosu kullanılır (4x4 matris).
- Her tuşa ait iki sinüs (bir alçak bir yüksek) toplanır: `x(t) = 0.5[sin(2π f_low t) + sin(2π f_high t)]`.
- Ses `sounddevice` kütüphanesi ile çalınır.
- Opsiyonel olarak FFT (Fast Fourier Transform) hesaplanıp gösterilebilir.
- Örnekleme frekansı ve ton süresi arayüz üzerinden seçilebilir.

### Kullanım
```bash
python gorev2.py
```
Açılan pencerede bir tuşa basın; hem zaman domeni grafiği güncellenecek hem de
ton duyulacaktır. FFT seçeneği işaretlendiğinde frekans alanı analizi de görüntülenir.

### DTMF Frekans Tablosu
```
       1209   1336   1477   1633
697    1      2      3      A
770    4      5      6      B
852    7      8      9      C
941    *      0      #      D
```

- En yüksek frekans 1633 Hz olduğundan Nyquist için `fs ≥ 3266 Hz` gerekir; proje
  için 8000 Hz seçilmiştir (telekomünikasyonda standart).

---

## 🛠️ Kurulum

Projenin çalışması için aşağıdaki Python paketleri gereklidir:

```bash
pip install numpy matplotlib sounddevice
```

> Tkinter genellikle Python ile birlikte gelir; eğer sisteminizde yoksa
> "tkinter" paketini veya ilgili sistem kütüphanesini yüklemelisiniz.

---

## 📁 Proje Dosya Yapısı

```
signal/             # workspace kökü
├─ gorev1.py         # Ödev 1: örnekleme ve sinüs sinyalleri
├─ gorev2.py         # Ödev 2: DTMF GUI uygulaması
└─ README.md         # Bu açıklayıcı belge
```

---

Geri kalan notları, geliştirme önerilerini veya sorunları GitHub üzerinde issue
olarak açabilirsiniz. Başarılar! 🎓
