import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

MAX_STUECKZAHL = 1000
SCHRITTWEITE = 50
FELDER = [
    ("Fixkosten (€):", "fixkosten"),
    ("Variable Kosten/Stück (€):", "variable_kosten"),
    ("Verkaufspreis/Stück (€):", "preis_stueck")
]

def break_even(fixkosten, variable_kosten, preis):
    if preis <= variable_kosten:
        raise ValueError("Der Preis muss größer als die variablen Kosten sein.")
    return fixkosten / (preis - variable_kosten)

def gewinn_berechnen(stueckzahl, fixkosten, variable_kosten, preis):
    return (preis - variable_kosten) * stueckzahl - fixkosten

def plot_gewinn(stueckzahlen, gewinne, bep):
    plt.figure(figsize=(8, 5))
    plt.plot(stueckzahlen, gewinne, label="Gewinn", color="blue")
    plt.axhline(0, color="red", linestyle="--", label="Gewinn = 0")
    plt.axvline(bep, color="green", linestyle="--", label="Break-Even-Punkt")
    plt.title("Gewinnsimulation")
    plt.xlabel("Stückzahl")
    plt.ylabel("Gewinn (€)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

def parse_inputs():
    try:
        fixkosten = float(entries["fixkosten"].get())
        variable_kosten = float(entries["variable_kosten"].get())
        preis_stueck = float(entries["preis_stueck"].get())
        if fixkosten < 0 or variable_kosten < 0 or preis_stueck <= 0:
            raise ValueError("Alle Werte müssen positiv sein und der Preis größer als 0.")
        return fixkosten, variable_kosten, preis_stueck
    except ValueError:
        raise ValueError("Bitte geben Sie gültige Zahlen ein.")

def berechnen():
    try:
        fixkosten, variable_kosten, preis = parse_inputs()
        bep = break_even(fixkosten, variable_kosten, preis)
        messagebox.showinfo("Ergebnis", f"Break-Even-Punkt: {bep:.2f} Stück")
        max_stueck = max(MAX_STUECKZAHL, int(bep) + 100)
        stueckzahlen = list(range(0, max_stueck, SCHRITTWEITE))
        gewinne = [gewinn_berechnen(s, fixkosten, variable_kosten, preis) for s in stueckzahlen]
        plot_gewinn(stueckzahlen, gewinne, bep)
    except ValueError as e:
        messagebox.showerror("Fehler", str(e))

root = tk.Tk()
root.title("Kostenanalyse-Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

entries = {}
for idx, (label_text, key) in enumerate(FELDER):
    tk.Label(frame, text=label_text).grid(row=idx, column=0, sticky="e", pady=5)
    entry = tk.Entry(frame, width=20)
    entry.grid(row=idx, column=1, pady=5)
    entries[key] = entry

tk.Button(
    frame,
    text="Berechnen",
    command=berechnen,
    width=20,
    bg="lightblue"
).grid(row=len(FELDER), column=0, columnspan=2, pady=10)

root.mainloop()