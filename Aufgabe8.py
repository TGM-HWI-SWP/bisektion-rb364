import math

def bisektion(f, a, b, eps):
    if f(a) * f(b) >= 0: return None
    while (b - a) / 2 > eps:
        c = (a + b) / 2
        if f(c) == 0: return c
        if f(a) * f(c) < 0: b = c
        else: a = c
    return (a + b) / 2

def aufgabe8():
    print("--- AUFGABE 8: Theorie-Polynom P4(x) ---")
    # P4(x) = x^4 - 5x^2 + 4
    p4 = lambda x: x**4 - 5*x**2 + 4
    
    # Test im Intervall [1.5, 2.5] -> Nullstelle bei x=2
    res = bisektion(p4, 1.5, 2.5, 0.0001)
    print(f"Berechnete Nullstelle für P4(x) im Intervall [1.5, 2.5]: {res}")

if __name__ == "__main__":
    aufgabe8()