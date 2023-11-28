def alarme(heure_alarme):
    hour,minute,second = heure_alarme
    formatted_alarme = f"{hour:02d}:{minute:02d}:{second:02d}"
    print(formatted_alarme)

def saisir_alarme():
    hour = int(input("Veuillez saisir l'heure de l'alarme : "))
    minute = int(input("Veuillez saisir les minutes de l'alarme : "))
    second = int(input("Veuillez saisir les secondes de l'alarme : "))
    return hour, minute, second