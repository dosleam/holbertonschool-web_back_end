#!/usr/bin/env python3
"""
Module pour retourner une fonction qui multiplie un nombre par un facteur donné.
"""


from typing import Callable
"""
Importation du type Callable depuis le module typing.
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Retourne une fonction qui multiplie un nombre donné par 'multiplier'.
    """

    return lambda x: x * multiplier
