#!/usr/bin/env python3

"""
Module pour retourner un tuple contenant une chaîne de caractères et le carré d'un entier ou flottant.
"""


from typing import Union, Tuple

"""
Importation des types Union et Tuple depuis le module typing.
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Retourne un tuple avec la chaîne de caractères k et le carré de v sous forme de flottant.
    """

    return (k, float(v ** 2))
