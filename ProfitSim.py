import matplotlib.pyplot as plt

def break_even(fixkosten, variable_kosten, preis):
    return fixkosten / (preis - variable_kosten)

def gewinn_berechnen(stückzahl, fixkosten, variable_kosten, preis):
    return (preis - variable_kosten) * stückzahl - fixkosten

def main():
    print("Kostenanalyse-Tool")
    fixkosten = float(input("Fixkosten eingeben: "))
    variable_kosten = float(input("Variable Kosten pro Stück: "))
    preis = float(input("Verkaufspreis pro Stück: "))

    bep = break_even(fixkosten, variable_kosten, preis)
    print(f"Break-Even-Punkt liegt bei {bep:.2f} Stück")

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

if __name__ == "__main__":
    main()