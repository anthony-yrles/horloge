import time
from heure import *
from alarme import *
from pause import *

heure_tuple = saisir_heure()
heure_alarme = saisir_alarme()
mode = choisir_mode()

running = True

while running:
    if pause():
        print("Horloge en pause. Appuyez sur 'b' pour reprendre.")
        while not keyboard.is_pressed("b"):
            pass
        print("Reprise de l'horloge.")
    afficher_heure_mode(heure_tuple, mode)

    time.sleep(1)  # Pause le programme pendant 1 seconde
    heure_tuple = (
        (heure_tuple[0] + (heure_tuple[1] + (heure_tuple[2] + 1) // 60) // 60) % 24,
        (heure_tuple[1] + (heure_tuple[2] + 1) // 60) % 60,
        (heure_tuple[2] + 1) % 60,)

    if heure_tuple == heure_alarme:
        print("Il est l'heure de se lever")
