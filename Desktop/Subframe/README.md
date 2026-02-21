# DTMF and Signals Project

Bu depo, DTMF (Dual-Tone Multi-Frequency) sinyallerini üretmek ve görüntülemek
üzere iki Python örneği içerir. Proje, "Signals and Systems" dersindeki ödev
çalışması için hazırlanmıştır.

## Dosyalar

- `gorev1.py`: Basit sinüzoidal sinyallerin oluşturulması ve çizilmesi.
- `gorev2.py`: Tkinter tabanlı bir GUI ile DTMF tuş sinyallerinin üretilmesi,
  opsiyonel FFT görüntüleme ve ses çalma.

## Kullanım

1. Python 3 yüklü olmalı.
2. Gerekli paketleri kurun:
   ```bash
   pip install numpy matplotlib sounddevice
   ```
3. `gorev1.py` veya `gorev2.py` dosyalarını çalıştırın:
   ```bash
   python gorev1.py
   python gorev2.py
   ```

`gorev2.py` çalışırken sesin duyulabilmesi için ses cihazınızın bağlı ve
çalışıyor olması gerekir.

## GitHub

Repo: `https://github.com/salihalbayrak/signs_and_systems_group7` (ya da
isim değiştiyse `odev1`)

Bu README, depo içeriğini açıklamak ve çalıştırma adımlarını sunmak için
hazırlanmıştır.