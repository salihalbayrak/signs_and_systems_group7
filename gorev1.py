import numpy as np
import matplotlib.pyplot as plt

# ====== 1) f0 hesabı (örnek) ======
f0 = 100  # kendi grubuna göre değiştir

# ====== 2) frekanslar ======
f1 = f0
f2 = f0 / 2
f3 = 10 * f0

# ====== 3) örnekleme frekansı (Nyquist üstü) ======
# f_max = f3 = 10*f0  => Nyquist: fs >= 2*f3 = 20*f0
# Daha güvenli seçim:
fs = 50 * f0

def make_signal(f, fs):
    """f frekanslı sinyal için 3 periyotluk zaman vektörü ve sinüs üretir."""
    T = 1 / f
    t = np.arange(0, 3*T, 1/fs)
    x = np.sin(2*np.pi*f*t)
    return t, x

# ====== 4) sinyaller ======
t1, x1 = make_signal(f1, fs)
t2, x2 = make_signal(f2, fs)
t3, x3 = make_signal(f3, fs)

# Toplamı çizmek için ortak bir zaman seçelim:
# En uzun pencere f2'de (en düşük frekans), o yüzden t_sum = t2 seçmek mantıklı.
# Ancak x1 ve x3'ü t2 üzerinde yeniden üretmeliyiz:
t_sum = t2
x1_sum = np.sin(2*np.pi*f1*t_sum)
x2_sum = np.sin(2*np.pi*f2*t_sum)
x3_sum = np.sin(2*np.pi*f3*t_sum)
x_sum = x1_sum + x2_sum + x3_sum

# ====== 5) grafikler ======
plt.figure(figsize=(10, 9))

plt.subplot(4, 1, 1)
plt.plot(t1, x1)
plt.title(f"x1(t) = sin(2π·{f1}·t)  (3 periyot)")
plt.xlabel("t (s)")
plt.ylabel("Genlik")
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t2, x2)
plt.title(f"x2(t) = sin(2π·{f2}·t)  (3 periyot)")
plt.xlabel("t (s)")
plt.ylabel("Genlik")
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t3, x3)
plt.title(f"x3(t) = sin(2π·{f3}·t)  (3 periyot)")
plt.xlabel("t (s)")
plt.ylabel("Genlik")
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t_sum, x_sum)
plt.title("x_sum(t) = x1(t) + x2(t) + x3(t)")
plt.xlabel("t (s)")
plt.ylabel("Genlik")
plt.grid(True)

plt.tight_layout()
plt.show()