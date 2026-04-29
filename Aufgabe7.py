import matplotlib.pyplot as plt
import numpy as np
import math

def f_eval(x, formel):
    # Wichtig: Wir fügen math.cosh und math.sinh hinzu, damit Aufgabe 9 funktioniert
    context = {
        "x": x, 
        "np": np, 
        "math": math, 
        "sin": np.sin, 
        "cos": np.cos, 
        "cosh": math.cosh, 
        "sinh": math.sinh,
        "exp": np.exp, 
        "sqrt": np.sqrt
    }
    return eval(formel, {"__builtins__": None}, context)

# Wir fügen Standardwerte (=None) in die Klammern ein
def plotter_vergleich(formel=None, a_input=None, b_input=None, eps=None):
    print("\n--- Numerik Visualisierung ---")
    
    # Falls die Werte NICHT von außen (Aufgabe 9) kommen, fragt er nach:
    if formel is None:
        formel = input("1. Funktion f(x) eingeben: ")
    if a_input is None:
        a_input = float(input("2. Untere Grenze (a): "))
    if b_input is None:
        b_input = float(input("3. Obere Grenze (b): "))
    if eps is None:
        eps = float(input("4. Genauigkeit (z.B. 0.0001): "))

    # Vorzeichenprüfung
    if f_eval(a_input, formel) * f_eval(b_input, formel) >= 0:
        print("\nFEHLER: f(a) und f(b) haben das gleiche Vorzeichen!")
        return

    # Daten-Listen
    bits, berrs, bsol = [], [], []
    rits, rerrs, rsol = [], [], []
    
    a1, b1 = a_input, b_input
    a2, b2 = a_input, b_input

    plt.ion()
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    fig.suptitle(f"Vergleich für $f(x) = {formel}$", fontsize=14)

    for it in range(1, 51):
        # --- BISEKTION ---
        c_b = (a1 + b1) / 2
        err_b = (b1 - a1) / 2
        bits.append(it)
        berrs.append(err_b)
        bsol.append(c_b)
        
        if f_eval(a1, formel) * f_eval(c_b, formel) < 0: b1 = c_b
        else: a1 = c_b

        # --- REGULA FALSI ---
        fa, fb = f_eval(a2, formel), f_eval(b2, formel)
        if abs(fb - fa) < 1e-14: break
        c_r = (a2 * fb - b2 * fa) / (fb - fa)
        err_r = abs(f_eval(c_r, formel))
        rits.append(it)
        rerrs.append(err_r)
        rsol.append(c_r)
        
        if f_eval(a2, formel) * f_eval(c_r, formel) < 0: b2 = c_r
        else: a2 = c_r

        # --- PLOT UPDATE ---
        for ax in [ax1, ax2, ax3, ax4]: ax.clear()
        
        ax1.semilogy(bits, berrs, 'r-o', markersize=4)
        ax1.set_title("Bisektion: Fehler")
        ax1.grid(True)
        
        ax2.plot(bits, bsol, 'r-s', markersize=4)
        ax2.set_title("Bisektion: Nullstelle")
        ax2.grid(True)

        ax3.semilogy(rits, rerrs, 'g-o', markersize=4)
        ax3.set_title("Regula Falsi: Fehler")
        ax3.grid(True)

        ax4.plot(rits, rsol, 'g-s', markersize=4)
        ax4.set_title("Regula Falsi: Nullstelle")
        ax4.grid(True)

        plt.pause(0.1)
        if err_b < eps and err_r < eps: break

    plt.ioff()
    print(f"Bisektion: {c_b:.6f}, Regula Falsi: {c_r:.6f}")
    plt.show()

if __name__ == "__main__":
    plotter_vergleich()