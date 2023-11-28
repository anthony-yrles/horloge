
def saisir_heure():
    hour = int(input("Veuillez saisir l'heure : "))
    minute = int(input("Veuillez saisir les minutes : "))
    second = int(input("Veuillez saisir les secondes : "))
    return hour, minute, second

def choisir_mode():
    mode = input("Si vous voulez un mode d'affichage 24h tappez 24 sinon tappez 12 : ").lower()
    if mode != "24" and mode != "12":
        mode = input("Si vous voulez un mode d'affichage 24h tappez 24 sinon tappez 12 : ").lower()
    return mode

def afficher_heure_mode(heure_tuple, mode):
    hour, minute, second = heure_tuple
    if mode == "24":
        formatted_time = f"{hour:02d}:{minute:02d}:{second:02d}"
    else:
        am_pm = "AM" if hour < 12 else "PM"
        formatted_hour = hour if hour <= 12 else hour - 12
        formatted_time = f"{formatted_hour:02d}:{minute:02d}:{second:02d} {am_pm}"

    print(formatted_time)
