"""Any y Sets."""

from typing import Any, Iterable


def superposicion_basico(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:  # noqa: E501
    """Toma dos listas y devuelve un booleano en base a si tienen al menos 1
    elemento en común.

    Restricciones:
        - Utilizar dos bucles FOR anidados.
        - Utilizar dos returns.
    """
    esComun = False
    for x in lista_1:
        for y in lista_2:
            if x == y:
                esComun = True
    return esComun


# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_basico(test_list, (2, "world", 35.20))
assert not superposicion_basico(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_in(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando un sólo bucle y el operador IN.

    Restricciones:
        - Utilizar un único bucle FOR.
        - Utilizar dos returns.
    """
    esComun = False
    for x in lista_1:
        if x in lista_2:
            esComun = True
    return esComun

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_in(test_list, (2, "world", 35.20))
assert not superposicion_in(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_any(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando la funcion any.

    Restricciones:
        - No utilizar bucles.
        - Utilizar una comprensión.
        - La solución debe tener 1 línea.

    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return any([x == y for x in lista_1 for y in lista_2])

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_any(test_list, (2, "world", 35.20))
assert not superposicion_any(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN


###############################################################################


def superposicion_set(lista_1: Iterable[Any], lista_2: Iterable[Any]) -> bool:
    """Re-Escribir utilizando conjuntos (sets).

    Restricciones:
        - Resolver sólo utilizando operaciones de conjuntos
        - No utilizar ANY, ALL, FOR, IF ni COMPRENSIONES

    Referencia: https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset  # noqa: E501
    """
    conj1 = set(lista_1)
    conj2 = set(lista_2)
    return not conj1.isdisjoint(conj2)

# NO MODIFICAR - INICIO
test_list = [1, "hello", 35.20]
assert superposicion_set(test_list, (2, "world", 35.20))
assert not superposicion_set(test_list, (2, "world", 30.85))
# NO MODIFICAR - FIN
