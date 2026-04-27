import math

def f_eval(x: float, formel: str) -> float:
    return eval(formel, {"x": x, "math": math, "sin": math.sin, "cos": math.cos, "sqrt": math.sqrt, "exp": math.exp, "log": math.log})

def solver():
    print("--- Aufgabe 5: Bisektions-Solver ---")
    try:
        formel = input("Gib die Funktion f(x) ein (z.B. x**2 - 3): ")
        a = float(input("Untere Intervallgrenze (a): "))
        b = float(input("Obere Intervallgrenze (b): "))
        epsilon = float(input("Genauigkeit (z.B. 0.0001): "))

        if f_eval(a, formel) * f_eval(b, formel) >= 0:
            print("Fehler: Das Vorzeichen an den Grenzen muss unterschiedlich sein!")
            return

        iteration = 0
        while (b - a) / 2 > epsilon:
            iteration += 1
            c = (a + b) / 2
            if f_eval(c, formel) == 0:
                break
            elif f_eval(a, formel) * f_eval(c, formel) < 0:
                b = c
            else:
                a = c
        
        print(f"Ergebnis nach {iteration} Iterationen: {(a + b) / 2}")
    except Exception as e:
        print(f"Fehler bei der Berechnung: {e}")

if __name__ == "__main__":
    solver()