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

        plt.plot(stückzahlen, gewinne, label='Gewinn')
        plt.axhline(0, color='red', linestyle='--', label='Gewinn = 0')
        plt.axvline(bep, color='green', linestyle='--', label='Break-Even-Punkt')
        plt.title("Gewinnsimulation")
        plt.xlabel("Stückzahl")
        plt.ylabel("Gewinn (€)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Fehler", "Bitte gültige Zahlen eingeben.")

#GUI erstellen
root = tk.Tk()
root.title("Kostenanalyse-Tool")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

#Eingabefelder
tk.Label(frame, text="Fixkosten (€):").grid(row=0, column=0, sticky="e", pady=5)
entry_fixkosten = tk.Entry(frame, width=20)
entry_fixkosten.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Variable Kosten/Stück (€):").grid(row=1, column=0, sticky="e", pady=5)
entry_variable_kosten = tk.Entry(frame, width=20)
entry_variable_kosten.grid(row=1, column=1, pady=5)

tk.Label(frame, text="Verkaufspreis/Stück (€):").grid(row=2, column=0, sticky="e", pady=5)
entry_preis = tk.Entry(frame, width=20)
entry_preis.grid(row=2, column=1, pady=5)

# Berechnen-Button
tk.Button(frame, text="Berechnen", command=berechnen, width=20, bg="lightblue").grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()