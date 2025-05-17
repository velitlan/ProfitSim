import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

#Konstante Werte
MAX_STUECKZAHL = 1000
SCHRITTWEITE = 50

def break_even(fixkosten, variable_kosten, preis):
    if preis <= variable_kosten:
        raise ValueError("Der Preis muss größer als die variablen Kosten sein.")
    return fixkosten / (preis - variable_kosten)

def gewinn_berechnen(stückzahl, fixkosten, variable_kosten, preis):
    return (preis - variable_kosten) * stückzahl - fixkosten

def berechnen():
    try:
        #Eingabewerte abrufen und validieren
        fixkosten = float(entry_fixkosten.get())
        variable_kosten = float(entry_variable_kosten.get())
        preis = float(entry_preis.get())

        if fixkosten < 0 or variable_kosten < 0 or preis <= 0:
            raise ValueError("Alle Werte müssen positiv sein und der Preis größer als 0.")
        bep = break_even(fixkosten, variable_kosten, preis)
        messagebox.showinfo("Ergebnis", f"Break-Even-Punkt liegt bei {bep:.2f} Stück")
        stückzahlen = list(range(0, max(MAX_STUECKZAHL, int(bep) + 100), SCHRITTWEITE))
        gewinne = [gewinn_berechnen(s, fixkosten, variable_kosten, preis) for s in stückzahlen]

        #Plot erstellen
        plt.figure(figsize=(8, 5))
        plt.plot(stückzahlen, gewinne, label='Gewinn', color='blue')
        plt.axhline(0, color='red', linestyle='--', label='Gewinn = 0')
        plt.axvline(bep, color='green', linestyle='--', label='Break-Even-Punkt')
        plt.title("Gewinnsimulation")
        plt.xlabel("Stückzahl")
        plt.ylabel("Gewinn (€)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError as e:
        messagebox.showerror("Fehler", str(e))

#GUI erstellen
root = tk.Tk()
root.title("Kostenanalyse-Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

#Eingabefelder für Fixkosten, variable Kosten und Preis
tk.Label(frame, text="Fixkosten (€):").grid(row=0, column=0, sticky="e", pady=5)
entry_fixkosten = tk.Entry(frame, width=20)
entry_fixkosten.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Variable Kosten/Stück (€):").grid(row=1, column=0, sticky="e", pady=5)
entry_variable_kosten = tk.Entry(frame, width=20)
entry_variable_kosten.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Verkaufspreis/Stück (€):").grid(row=2, column=0, sticky="e", pady=5)
entry_preis = tk.Entry(frame, width=20)
entry_preis.grid(row=2, column=1, pady=5)

tk.Button(frame, text="Berechnen", command=berechnen, width=20, bg="lightblue").grid(row=3, column=0, columnspan=2, pady=10)

#Hauptloop starten
root.mainloop()