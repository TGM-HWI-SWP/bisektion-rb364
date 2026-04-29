import math

def f_eval(x, formel):
    # Ermöglicht die Berechnung von x basierend auf deiner Texteingabe
    return eval(formel, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "sqrt": math.sqrt, "exp": math.exp})

def bisektion_logik(f_str, a, b, eps):
    # Wir definieren eine interne Hilfsfunktion, die f_eval nutzt
    f = lambda x: f_eval(x, f_str)
    
    if f(a) * f(b) >= 0:
        print("Fehler: Kein Vorzeichenwechsel im gewählten Intervall [a, b]!")
        return None
    
    print("\n" + "-"*65)
    print(f"{'It.':<4} | {'a':<12} | {'b':<12} | {'Mitte c':<12} | {'f(c)':<12}")
    print("-"*65)

    it = 0
    while (b - a) / 2 > eps:
        it += 1
        c = (a + b) / 2
        fc = f(c)
        
        print(f"{it:<4} | {a:<12.6f} | {b:<12.6f} | {c:<12.6f} | {fc:<12.6f}")

        if fc == 0: break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    print("-" * 65)
    return (a + b) / 2

def aufgabe8_flexibel():
    print("\n--- AUFGABE 8: Flexibler Polynom-Solver ---")
    try:
        # Hier kannst du jetzt deine Werte selbst eingeben
        formel = input("1. Funktion f(x) (z.B. x**4 - 5*x**2 + 4): ")
        a = float(input("2. Untere Grenze a: "))
        b = float(input("3. Obere Grenze b: "))
        eps = float(input("4. Genauigkeit (z.B. 0.0001): "))

        ergebnis = bisektion_logik(formel, a, b, eps)
        
        if ergebnis is not None:
            print(f"\nERGEBNIS: Die Nullstelle liegt bei ca. {ergebnis:.6f}")
            
    except Exception as e:
        print(f"Fehler bei der Eingabe oder Berechnung: {e}")

if __name__ == "__main__":
    aufgabe8_flexibel()