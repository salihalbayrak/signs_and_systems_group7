# Sinüzoidal İşaretlerin Örneklenmesi ve DTMF Uygulaması

Bu proje, sinüzoidal işaretlerin bilgisayar ortamında örneklenmesi ve DTMF (Dual-Tone
Multi-Frequency) sinyal üretimi üzerine hazırlanmıştır. Aşağıdaki iki ödev içermektedir:

1. **Ödev 1**: Temel frekans `f0` ile üç farklı sinüzoidal sinyal (`f1=f0`, `f2=f0/2`,
   `f3=10*f0`) üretilir, Nyquist örnekleme teoremi çerçevesinde örneklenir ve grafik
   olarak çizilir. Ayrıca sinyaller toplanarak karma bir sinyal elde edilir.

2. **Ödev 2**: Telefon tuş takımı arayüzü (Tkinter) üzerinden DTMF tonları üretilir.
   Her tuşa ait iki sinüzoidal sinyal toplanır ve ses olarak çalınır. İsteğe bağlı olarak
   FFT ile frekans domeni analizi yapılabilir.

## Kullanılan Teknolojiler

- Python 3
- NumPy
- Matplotlib
- sounddevice
- Tkinter

## Kurulum

```bash
pip install numpy matplotlib sounddevice
```

## Çalıştırma

- `gorev1.py`: Ödev 1 için sinyallerin üretimi ve grafikleri
- `gorev2.py`: DTMF arayüzü

Dosyaları çalıştırmak için Python interpretatörünü kullanabilirsiniz:

```bash
python Desktop/Subframe/gorev1.py
python Desktop/Subframe/gorev2.py
```
