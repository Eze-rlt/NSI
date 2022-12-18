def mode_weekend(heure: float) -> str:
    "Fonction qui renvoie le mode de votre chauffage pour le weekend, Robert !"
    assert type(heure) == float, "L'heure entrée doit être un float()"
    mode = "Mode Confort" if 9 <= heure < 22 else "Mode Eco" #RENVOIE LE BON MODE EN FONCTION DE L'HEURE

    assert mode == "Mode Confort" or mode == "Mode Eco", "Erreur lors du mode sortant"
    assert type(mode) == str, "Le type du mode sortant n'est pas une str"
    return mode#RENVOIE LE MODE TROUVE PRECEDEMMENT

def mode_semaine(heure: float) -> str:
    "Fonction qui renvoie le mode de votre chauffage pour la semaine, Robert !"
    assert type(heure) == float, "L'heure entrée doit être un float()"
    mode = "Mode Confort" if (6 <= heure < 9 or 17 <= heure < 22) else "Mode Eco"#RENVOIE LE BON MODE EN FONCTION DE L'HEURE

    assert mode == "Mode Confort" or mode == "Mode Eco", "Erreur lors du mode sortant"
    assert type(mode) == str, "Le type du mode sortant n'est pas une str"

    return mode#RENVOIE LE MODE TROUVE PRECEDEMMENT

def mode(jour: str, heure: float) -> str:
    "Fonction qui renvoie le mode de votre chauffage pour un jour donné, Robert !"
    assert jour.lower() in ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'], "Le jour entré est invalide"
    
    if jour.lower() in ['samedi', 'dimanche']:#REGARDE SI LE MODE EST DANS LE WEEKEND
        return mode_weekend(heure)#APPELLE LA FONCTION WEEKEND CAR C'EST LE WEEKEND POUR ROBERT, PUIS RENVOIE LE MODE TROUVE
    return mode_semaine(heure)#APPELLE LA FONCTION WEEKEND CAR C'EST LA SEMAINE POUR ROBERT, PUIS RENVOIE LE MODE TROUVE
