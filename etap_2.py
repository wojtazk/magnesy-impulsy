import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App(tk.Tk):
    def __init__(self):
        # --- inicjalizacja ---
        super().__init__()
        self.title("Anteniarstwo stosowane: projekt nr 3")

        # --- ikonka ---
        icon = tk.PhotoImage(file="icon.png")
        self.iconphoto(True, icon)

        # --- layout: lewy panel i prawy panel ---
        left_panel = tk.Frame(self, padx=10, pady=10)
        left_panel.pack(side="left", fill="y")

        right_panel = tk.Frame(self)
        right_panel.pack(side="right", fill="both", expand=True)

        # --- sekcja 1 ---
        # ( variable, "label" )
        self.variables = [
            # parametry sygnału
            (tk.StringVar(value="1000.00"), "Częstotliwość próbkowania [Hz]"),
            (tk.StringVar(value="1.00"), "Czas obserwacji [s]"),

            # Mambo-dżambo
            (tk.StringVar(value="1.00"), "A: "),
            (tk.StringVar(value="1.00"), "K: "),
            (tk.StringVar(value="1.00"), "t_1: "),
            (tk.StringVar(value="1.00"), "t_2: "),
            (tk.StringVar(value="1.00"), "n: "),
            (tk.StringVar(value="4.0"), "f:"),
            (tk.StringVar(value="0.00"), "φ"),
        ]
        # dodawanie do okienka
        for var in self.variables:
            tk.Label(left_panel, text=var[1]).pack(anchor="w")
            tk.Entry(left_panel, textvariable=var[0], width=10).pack(
                padx=0, pady=5
            )
        # dodawanie listener'ów (Enter i zmiana focusu)
        for child in left_panel.winfo_children():
            for seq in ("<Return>", "<FocusOut>"):
                child.bind(seq, self.update_plot)

        # --- dropdowny ---
        bottom_panel = tk.Frame(left_panel, pady=10)
        bottom_panel.pack(side="bottom", fill="x")

        # wybór okna
        self.win_var = tk.StringVar(value="Rectangular")
        win_options = ["Rectangular", "Hann", "Hamming"]
        tk.Label(bottom_panel, text="Okno:").pack(side="left")
        tk.OptionMenu(bottom_panel, self.win_var, *win_options).pack(
            side="left", padx=5
        )
        self.win_var.trace("w", lambda *a: self.update_plot())

        # wybór dziedziny
        self.dom_var = tk.StringVar(value="Czas")
        dom_options = ["Czas", "Częstotliwość"]
        tk.Label(bottom_panel, text="Dziedzina:").pack(side="left", padx=0)
        tk.OptionMenu(bottom_panel, self.dom_var, *dom_options).pack(
            side="left", padx=0
        )
        self.dom_var.trace("w", lambda *a: self.update_plot())

        # --- wykres ---
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_panel)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # --- pierwsze rysowanie ---
        self.update_plot()

    def update_plot(self, event=None):
        # ddczyt i walidacja zmiennych
        fs = float(self.variables[0][0].get().replace(",", "."))
        t_obs = float(self.variables[1][0].get().replace(",", "."))

        a = float(self.variables[2][0].get().replace(",", "."))
        k = float(self.variables[3][0].get().replace(",", "."))
        t_1 = float(self.variables[4][0].get().replace(",", "."))
        t_2 = float(self.variables[5][0].get().replace(",", "."))
        f = float(self.variables[6][0].get().replace(",", "."))
        phi = float(self.variables[7][0].get().replace(",", "."))

        # punkty w czasie
        t = np.linspace(0, t_obs, int(fs * t_obs), endpoint=False)

        # generowanie sygnału 1: y(t) = A * sin(2π * f * t  + phi)
        y = a * np.sin(2 * np.pi * f * t + phi * np.pi)

        # przygotowanie okna
        w_type = self.win_var.get()
        if w_type == "Hann":
            w = np.hanning(len(y))
        elif w_type == "Hamming":
            w = np.hamming(len(y))
        else:
            w = np.ones(len(y))

        # rysowanie
        self.ax.clear()
        if self.dom_var.get() == "Czas":
            self.ax.plot(t, y, lw=1)
            self.ax.set_xlabel("Czas [s]")
            self.ax.set_ylabel("Amplituda")
        else:
            y = np.fft.fft(y * w)
            f_axis = np.fft.fftfreq(len(y), 1 / fs)
            pos = f_axis >= 0

            # normalizacja FFT
            y /= len(y)

            self.ax.plot(f_axis[pos], np.abs(y[pos]), lw=1)
            self.ax.set_xlabel("Częstotliwość [Hz]")
            self.ax.set_ylabel("Amplituda")

        self.ax.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    app = App()
    app.geometry("900x500")
    app.mainloop()
