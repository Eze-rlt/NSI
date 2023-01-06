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


def molkky(score_restant: int, nbe_points_marqués: int, nbe_zéros: int) -> str:
    """Programme qui affiche le nouveau score ou signale une éventuelle victoire ou défaite."""
    assert type(score_restant) == type(nbe_points_marqués) == type(nbe_zéros) == int, 'Les valeurs entrées doivent être des int()'
    assert 0 <= nbe_points_marqués <= 12, 'Ce score marqué est impossible'
    assert 0 < score_restant <= 51, 'Ce score restant est impossible'
    assert 0 <= nbe_zéros <= 2, "Le nombre de zéro entré doit être 0, 1 ou 2"

    score_restant = score_restant-nbe_points_marqués

    if nbe_zéros == 2 and nbe_points_marqués == 0:
        return "Vous avez fait 3 fois 0 à la suite, vous êtes éliminés."
    elif score_restant == 0:
        return "Vous avez gagnés !!!"
    elif score_restant < 0:
        return "Vous avez dépassés 51, votre score revient à 25."
    return "Vous avez actuellement " + str(51-score_restant) + " points. Il vous manque donc " + str(score_restant) + " points pour gagner."
