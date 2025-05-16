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


            # sinusoida 1
            (tk.StringVar(value="1.00"), "Amplituda_1"),
            (tk.StringVar(value="0.00"), "Faza_1 [PI]"),
            (tk.StringVar(value="4.0"), "Częstotliwość_1 [Hz]:"),

            # sinusoida 2
            (tk.StringVar(value="1.00"), "Amplituda_2"),
            (tk.StringVar(value="0.00"), "Faza_2 [PI]"),
            (tk.StringVar(value="4.0"), "Częstotliwość_2 [Hz]:"),
        ]
        # dodawanie do okienka
        for var in self.variables:
            tk.Label(left_panel, text=var[1]).pack(anchor="w")
            tk.Entry(left_panel, textvariable=var[0], width=10).pack(padx=0, pady=5)
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
        # ddczyt i walidacja zmiennych

        fs = float(self.variables[0][0].get().replace(",", "."))
        t_obs = float(self.variables[1][0].get().replace(",", "."))
        a = float(self.variables[2][0].get().replace(",", "."))
        phi = float(self.variables[3][0].get().replace(",", "."))
        f = float(self.variables[4][0].get().replace(",", "."))

        a_2 = float(self.variables[5][0].get().replace(",", "."))
        phi_2 = float(self.variables[6][0].get().replace(",", "."))
        f_2 = float(self.variables[7][0].get().replace(",", "."))

        # punkty w czasie
        t = np.linspace(0, t_obs, int(fs * t_obs), endpoint=False)

        # generowanie sygnału 1: y(t) = A * sin(2π * f * t  + phi)
        y = a * np.sin(2 * np.pi * f * t + phi*np.pi)
        # generowanie sygnału 2
        y_2 = a_2 * np.sin(2 * np.pi * f_2 * t + phi_2 * np.pi)

        # rysowanie
        self.ax.clear()
        self.ax.plot(t, y + y_2, lw=1)
        # self.ax.set_title(f"Sinus: $f = {f:.2f}\\,$Hz")
        self.ax.set_xlabel("Czas [s]")
        self.ax.set_ylabel("Amplituda")
        self.ax.grid(True)
        self.canvas.draw()


if __name__ == "__main__":
    app = App()
    app.geometry("900x500")
    app.mainloop()
