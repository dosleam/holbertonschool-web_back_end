#!/usr/bin/env python3

"""
Module pour calculer la longueur de chaque élément dans une liste d'éléments séquentiels.
"""


from typing import Iterable, Sequence, List, Tuple

"""
Importation des types nécessaires depuis le module typing.
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Retourne une liste de tuples contenant chaque élément et sa longueur.
    """

    return [(i, len(i)) for i in lst]
