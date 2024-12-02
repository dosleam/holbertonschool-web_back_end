#!/usr/bin/env python3
"""
Module pour calculer la somme des éléments d'une liste de flottants.
"""


from typing import List
"""
Importation du type List depuis le module typing.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Retourne la somme des éléments de la liste d'entrées.
    """

    return sum(input_list)  # Calcule et retourne la somme des éléments de la liste.
