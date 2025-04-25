import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

def break_even(fixkosten, variable_kosten, preis):
    return fixkosten / (preis - variable_kosten)

def gewinn_berechnen(stückzahl, fixkosten, variable_kosten, preis):
    return (preis - variable_kosten) * stückzahl - fixkosten

def berechnen():
    try:
        fixkosten = float(entry_fixkosten.get())
        variable_kosten = float(entry_variable_kosten.get())
        preis = float(entry_preis.get())

        bep = break_even(fixkosten, variable_kosten, preis)
        messagebox.showinfo("Ergebnis", f"Break-Even-Punkt liegt bei {bep:.2f} Stück")

        stückzahlen = list(range(0, 1001, 50))
        gewinne = [gewinn_berechnen(s, fixkosten, variable_kosten, preis) for s in stückzahlen]

        plt.plot(stückzahlen, gewinne)
        plt.axhline(0, color='red', linestyle='--')
        plt.axvline(bep, color='green', linestyle='--')
        plt.title("Gewinnsimulation")
        plt.xlabel("Stückzahl")
        plt.ylabel("Gewinn (€)")
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

#GUI erstellen
root = tk.Tk()
root.title("Kostenanalyse-Tool")

tk.Label(root, text="Fixkosten eingeben:").pack()
entry_fixkosten = tk.Entry(root)
entry_fixkosten.pack()
tk.Label(root, text="Variable Kosten pro Stück:").pack()
entry_variable_kosten = tk.Entry(root)
entry_variable_kosten.pack()
tk.Label(root, text="Verkaufspreis pro Stück:").pack()
entry_preis = tk.Entry(root)
entry_preis.pack()
tk.Button(root, text="Berechnen", command=berechnen).pack()
root.mainloop()