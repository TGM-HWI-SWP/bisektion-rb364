import matplotlib.pyplot as plt
import numpy as np
import math

def f_eval(x, formel):
    return eval(formel, {"x": x, "math": math, "np": np})

def plotter_vergleich(formel="x**2 - 3", a_start=1, b_start=2, eps=0.0001):
    # Daten für Bisektion
    bits, berrs, bsol = [], [], []
    a1, b1 = a_start, b_start
    
    # Daten für Regula Falsi
    rits, rerrs, rsol = [], [], []
    a2, b2 = a_start, b_start
    
    # Vorbereitung der Figure mit 2x2 Subplots
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    plt.subplots_adjust(hspace=0.4, wspace=0.3)
    fig.suptitle(f"Vergleich: Bisektion vs. Regula Falsi ({formel})", fontsize=16)

    for it in range(1, 21): # Maximal 20 Schritte
        # --- LOGIK BISEKTION ---
        c_b = (a1 + b1) / 2
        err_b = (b1 - a1) / 2
        bits.append(it)
        berrs.append(err_b)
        bsol.append(c_b)
        
        if f_eval(a1, formel) * f_eval(c_b, formel) < 0: b1 = c_b
        else: a1 = c_b

        # --- LOGIK REGULA FALSI ---
        fa, fb = f_eval(a2, formel), f_eval(b2, formel)
        c_r = (a2 * fb - b2 * fa) / (fb - fa)
        err_r = abs(f_eval(c_r, formel))
        rits.append(it)
        rerrs.append(err_r)
        rsol.append(c_r)
        
        if f_eval(a2, formel) * f_eval(c_r, formel) < 0: b2 = c_r
        else: a2 = c_r

        # --- PLOTTING ---
        # 1. Genauigkeit Bisektion
        ax1.clear()
        ax1.plot(bits, berrs, 'r-o')
        ax1.set_title("Bisektion: Fehler (b-a)/2")
        ax1.set_yscale('log') # Logarithmisch zeigt die Halbierung besser
        ax1.grid(True)

        # 2. Lösung Bisektion
        ax2.clear()
        ax2.plot(bits, bsol, 'r-s')
        ax2.set_title("Bisektion: Näherung x")
        ax2.grid(True)

        # 3. Genauigkeit Regula Falsi
        ax3.clear()
        ax3.plot(rits, rerrs, 'g-o')
        ax3.set_title("Regula Falsi: Fehler |f(c)|")
        ax3.set_yscale('log')
        ax3.grid(True)

        # 4. Lösung Regula Falsi
        ax4.clear()
        ax4.plot(rits, rsol, 'g-s')
        ax4.set_title("Regula Falsi: Näherung x")
        ax4.grid(True)

        plt.pause(0.3)
        
        # Stoppen wenn beide genau genug sind
        if err_b < eps and err_r < eps:
            break

    plt.show()

if __name__ == "__main__":
    plotter_vergleich()