import math
# Wir importieren die Rechenlogik aus Aufgabe 5 und den Plotter aus Aufgabe 7
from Aufgabe5 import bisektion_logik
from Aufgabe7 import plotter_vergleich

def loese_seil_problem():
    print("\n" + "="*50)
    print("   AUFGABE 9: BERECHNUNG DER KETTENLINIE")
    print("="*50)
    
    # Gegebene Werte aus der Aufgabenstellung
    w = 100  # Spannweite (Abstand der Masten)
    h = 10   # Maximaler Durchhang in der Mitte
    
    # Die Formel für den Durchhang lautet: h = a * cosh(w/2a) - a
    # Umgestellt als Nullstellenproblem: f(a) = a * cosh(50/a) - a - 10 = 0
    f_seil = lambda a: a * math.cosh(w / (2 * a)) - a - h
    
    print(f"Suche Krümmungsradius 'a' im Intervall [50, 200]...")
    
    # Schritt 1: Berechne den Krümmungsradius a mit der Logik aus Aufgabe 5
    a_geloest = bisektion_logik(f_seil, 50, 200, 0.0001)
    
    if a_geloest:
        print(f"\nERGEBNIS GEFUNDEN:")
        print(f"-> Krümmungsradius a: {a_geloest:.4f}")
        
        # Schritt 2: Berechne die Seillänge l mit der sinh-Formel
        # l = 2a * sinh(w / 2a)
        laenge = 2 * a_geloest * math.sinh(w / (2 * a_geloest))
        print(f"-> Gesamtlänge der Leitung l: {laenge:.4f} Meter")
        
        print("\nStarte nun die Vergleichs-Animation (Bisektion vs. Regula Falsi)...")
        
        # Schritt 3: Starte die Animation aus Aufgabe 7 mit der Seil-Funktion
        # Wir übergeben die Formel als Text für die Grafikbeschriftung
        formel_text = "x * math.cosh(50/x) - x - 10"
        plotter_vergleich(formel_text, 50, 200, 0.0001)
        
    else:
        print("Fehler: In diesem Intervall wurde keine Lösung gefunden.")

if __name__ == "__main__":
    loese_seil_problem()