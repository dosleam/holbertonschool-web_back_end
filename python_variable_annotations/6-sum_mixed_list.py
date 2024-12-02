#!/usr/bin/env python3
"""
Module pour calculer la somme des éléments d'une liste contenant des entiers et des flottants.
"""


from typing import List, Union
"""
Importation des types List et Union depuis le module typing.
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Retourne la somme des éléments de la liste, qui peuvent être des entiers ou des flottants.
    """

    return float(sum(mxd_lst))
