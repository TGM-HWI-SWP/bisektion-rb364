import math

def f_eval(x, formel):
    return eval(formel, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "sqrt": math.sqrt, "exp": math.exp})

def bisektion_logik(f, a, b, eps, print_table=False):
    if f(a) * f(b) >= 0:
        return None
    
    if print_table:
        print("\n" + "-"*65)
        print(f"{'It.':<4} | {'a':<12} | {'b':<12} | {'Mitte c':<12} | {'f(c)':<12}")
        print("-"*65)

    it = 0
    while (b - a) / 2 > eps:
        it += 1
        c = (a + b) / 2
        fc = f(c)
        
        if print_table:
            print(f"{it:<4} | {a:<12.6f} | {b:<12.6f} | {c:<12.6f} | {fc:<12.6f}")

        if fc == 0: break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    if print_table: print("-" * 65)
    return (a + b) / 2

def solver():
    print("\n--- AUFGABE 5: Bisektionsverfahren ---")
    try:
        formel = input("Funktion f(x) (z.B. x**2 - 3): ")
        a = float(input("Intervallgrenze a: "))
        b = float(input("Intervallgrenze b: "))
        eps = float(input("Genauigkeit (z.B. 0.001): "))

        f_objekt = lambda x: f_eval(x, formel)
        
        # Hier setzen wir print_table=True, damit die Tabelle im Einzeltest erscheint
        ergebnis = bisektion_logik(f_objekt, a, b, eps, print_table=True)

        if ergebnis is not None:
            print(f"Ergebnis: {ergebnis:.6f}")
        else:
            print("Fehler: Kein Vorzeichenwechsel im Intervall!")
            
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    solver()