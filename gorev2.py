import numpy as np
import tkinter as tk
from tkinter import ttk
import sounddevice as sd

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# =========================================================
# 1) DTMF frekans tablosu (standart)
# =========================================================
DTMF = {
    "1": (697, 1209), "2": (697, 1336), "3": (697, 1477), "A": (697, 1633),
    "4": (770, 1209), "5": (770, 1336), "6": (770, 1477), "B": (770, 1633),
    "7": (852, 1209), "8": (852, 1336), "9": (852, 1477), "C": (852, 1633),
    "*": (941, 1209), "0": (941, 1336), "#": (941, 1477), "D": (941, 1633),
}

# =========================================================
# 2) Sinyal üretme fonksiyonu
# =========================================================
def generate_dtmf_tone(key: str, fs: int, duration: float):
    """
    Bir tuşa ait DTMF sinyalini üretir:
      x(t) = 0.5*(sin(2π f_low t) + sin(2π f_high t))

    Neden 0.5?
      İki sinüs toplanınca genlik 2'ye çıkabilir -> clipping olmasın diye.
    """
    f_low, f_high = DTMF[key]
    t = np.arange(0, duration, 1/fs)

    x = 0.5 * (np.sin(2*np.pi*f_low*t) + np.sin(2*np.pi*f_high*t))

    # Ses kütüphanesi float32 sever:
    return t, x.astype(np.float32), f_low, f_high

# =========================================================
# 3) (Opsiyonel) FFT ile frekans domeni göstermek
# =========================================================
def compute_fft(x: np.ndarray, fs: int):
    """
    FFT: Zaman domenindeki sinyalin frekans bileşenlerini görmek için.
    Amaç: DTMF’de iki baskın tepe (f_low ve f_high) var mı göstermek.
    """
    N = len(x)
    X = np.fft.rfft(x)  # pozitif frekanslar
    freqs = np.fft.rfftfreq(N, d=1/fs)
    mag = np.abs(X)
    return freqs, mag

# =========================================================
# 4) GUI Uygulaması
# =========================================================
class DTMFApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DTMF Telefon Tuş Takımı - Ödev 2")
        self.geometry("1000x650")

        # Varsayılanlar (hocanın önerisine uygun)
        self.fs_var = tk.IntVar(value=8000)
        self.dur_var = tk.DoubleVar(value=0.25)
        self.show_fft_var = tk.BooleanVar(value=False)

        self._build_ui()
        self._build_plot()

    def _build_ui(self):
        top = ttk.Frame(self, padding=10)
        top.pack(fill="x")

        ttk.Label(top, text="Örnekleme Frekansı (Hz):").pack(side="left")
        ttk.Combobox(top, textvariable=self.fs_var, values=[8000, 44100], width=8, state="readonly").pack(side="left", padx=6)

        ttk.Label(top, text="Süre T (sn):").pack(side="left", padx=(10, 0))
        ttk.Combobox(top, textvariable=self.dur_var, values=[0.2, 0.25, 0.3, 0.5], width=8, state="readonly").pack(side="left", padx=6)

        ttk.Checkbutton(top, text="FFT Göster (Opsiyonel)", variable=self.show_fft_var, command=self._toggle_fft).pack(side="left", padx=10)

        self.info_lbl = ttk.Label(top, text="Bir tuşa basın.", foreground="#444")
        self.info_lbl.pack(side="left", padx=10)

        # Tuş takımı
        pad = ttk.Frame(self, padding=10)
        pad.pack(side="left", fill="y")

        keys = [
            ["1", "2", "3", "A"],
            ["4", "5", "6", "B"],
            ["7", "8", "9", "C"],
            ["*", "0", "#", "D"],
        ]

        for r, row in enumerate(keys):
            for c, k in enumerate(row):
                btn = ttk.Button(pad, text=k, command=lambda kk=k: self.on_keypress(kk))
                btn.grid(row=r, column=c, padx=6, pady=6, ipadx=16, ipady=10)

    def _build_plot(self):
        # Matplotlib figure (zaman domeni)
        self.fig = Figure(figsize=(7.5, 5.5), dpi=100)
        self.ax_time = self.fig.add_subplot(2, 1, 1)
        self.ax_time.set_title("Zaman Domeni: x(t)")
        self.ax_time.set_xlabel("t (s)")
        self.ax_time.set_ylabel("Genlik")
        self.ax_time.grid(True)

        # FFT opsiyonel eksen
        self.ax_fft = self.fig.add_subplot(2, 1, 2)
        self.ax_fft.set_title("Frekans Domeni (FFT)")
        self.ax_fft.set_xlabel("f (Hz)")
        self.ax_fft.set_ylabel("|X(f)|")
        self.ax_fft.grid(True)

        # Başta FFT kapalı gibi davranalım
        self.ax_fft.set_visible(False)
        self.fig.tight_layout()

        canvas_frame = ttk.Frame(self, padding=10)
        canvas_frame.pack(side="right", fill="both", expand=True)

        self.canvas = FigureCanvasTkAgg(self.fig, master=canvas_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def _toggle_fft(self):
        show = self.show_fft_var.get()
        self.ax_fft.set_visible(show)
        self.fig.tight_layout()
        self.canvas.draw_idle()

    def on_keypress(self, key: str):
        fs = int(self.fs_var.get())
        dur = float(self.dur_var.get())

        t, x, f_low, f_high = generate_dtmf_tone(key, fs, dur)

        # 1) Ses çal
        sd.stop()
        sd.play(x, fs)

        # 2) Zaman domeni grafiği çiz (anlık)
        self.ax_time.clear()
        self.ax_time.plot(t, x)
        self.ax_time.set_title(f"Zaman Domeni: Tuş '{key}'  (f_low={f_low} Hz, f_high={f_high} Hz)")
        self.ax_time.set_xlabel("t (s)")
        self.ax_time.set_ylabel("Genlik")
        self.ax_time.grid(True)

        # 3) FFT (opsiyonel)
        if self.show_fft_var.get():
            freqs, mag = compute_fft(x, fs)
            self.ax_fft.clear()
            self.ax_fft.plot(freqs, mag)
            self.ax_fft.set_title("Frekans Domeni (FFT) - İki baskın tepe beklenir")
            self.ax_fft.set_xlabel("f (Hz)")
            self.ax_fft.set_ylabel("|X(f)|")
            self.ax_fft.set_xlim(0, 2000)  # DTMF bandı için yeterli
            self.ax_fft.grid(True)

        self.fig.tight_layout()
        self.canvas.draw_idle()

        self.info_lbl.config(text=f"Tuş: {key} → {f_low} Hz + {f_high} Hz, fs={fs}, T={dur}s")


if __name__ == "__main__":
    app = DTMFApp()
    app.mainloop()