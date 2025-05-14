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

        # --- parametry sygnału ---
        self.fs = 1000.0  # częstotliwość próbkowania [Hz]
        self.T_obs = 1.0  # czas obserwacji [s]
        N = int(self.fs * self.T_obs)
        self.t = np.linspace(0, self.T_obs, N, endpoint=False)

        # --- sekcja 1 ---
        # ( variable, "label" )
        self.variables = [
            # sinusoida 1
            (tk.StringVar(value="4.0"), "Częstotliwość [Hz]:"),
            (tk.StringVar(value="4.0"), "Test")
        ]
        # dodawanie do okienka
        for var in self.variables:
            tk.Label(left_panel, text=var[1]).pack(anchor=tk.W)
            tk.Entry(left_panel, textvariable=var[0], width=10).pack(padx=5, pady=5)
        # dodawanie listener'ów (Enter i zmiana focusu)
        for child in left_panel.winfo_children():
            for seq in ("<Return>", "<FocusOut>"):
                child.bind(seq, self.update_plot)

        # --- wykres ---
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=right_panel)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # --- pierwsze rysowanie ---
        self.update_plot()

    def update_plot(self, event=None):
        # ddczyt i walidacja fs
        text = self.variables[0][0].get().replace(",", ".")
        try:
            f = float(text)
            if f <= 0:
                raise ValueError
        except ValueError:
            f = 4.0
        self.variables[0][0].set(f"{f:.2f}")

        # generowanie sygnału: y(t) = sin(2π * f * t)
        y = np.sin(2 * np.pi * f * self.t)

        # rysowanie
        self.ax.clear()
        self.ax.plot(self.t, y, lw=1)
        # self.ax.set_title(f"Sinus: $f = {f:.2f}\\,$Hz")
        self.ax.set_xlabel("Czas [s]")
        self.ax.set_ylabel("Amplituda")
        self.ax.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    app = App()
    # app.geometry("900x500")
    app.mainloop()
