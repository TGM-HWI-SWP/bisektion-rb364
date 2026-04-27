import math

def f_eval(x, formel):
    return eval(formel, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "exp": math.exp})

def regula_falsi_logik(f, a, b, eps, print_table=False):
    it = 0
    c = a
    
    if print_table:
        print("\n" + "-"*65)
        print(f"{'It.':<4} | {'a':<12} | {'b':<12} | {'Schnitt c':<12} | {'f(c)':<12}")
        print("-"*65)

    while it < 100:
        it += 1
        fa, fb = f(a), f(b)
        if (fb - fa) == 0: break
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        if print_table:
            print(f"{it:<4} | {a:<12.6f} | {b:<12.6f} | {c:<12.6f} | {fc:<12.6f}")

        if abs(fc) < eps:
            break
            
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    if print_table: print("-" * 65)
    return c

def solver2():
    print("\n--- AUFGABE 6: Regula Falsi ---")
    try:
        formel = input("Funktion f(x): ")
        a = float(input("Grenze a: "))
        b = float(input("Grenze b: "))
        eps = float(input("Genauigkeit: "))

        f_objekt = lambda x: f_eval(x, formel)
        ergebnis = regula_falsi_logik(f_objekt, a, b, eps, print_table=True)
        print(f"Ergebnis: {ergebnis:.6f}")
    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    solver2()