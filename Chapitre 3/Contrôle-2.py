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
