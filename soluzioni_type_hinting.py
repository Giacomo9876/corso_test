# Soluzioni esercizi Type Hinting e Generics

from typing import Optional, Union, Callable, Tuple, Dict, TypeVar, Type, Generic

# ------
def somma(a: int, b: int) -> int:
    return a + b

# ------
def greeting(nome: Optional[str] = None) -> str:
    if nome:
        return f"Ciao, {nome}!"
    return "Ciao, ospite!"

# ------
def to_string(valore: Union[int, float]) -> str:
    return f"Il valore è {valore}"

# ------
def applica_due_volte(x: int, funzione: Callable[[int], int]) -> int:
    return funzione(funzione(x))

# ------
T = TypeVar("T")
def scambia(a: T, b: T) -> Tuple[T, T]:
    return b, a

# ------
class Animale:
    def parla(self):
        return "Sono un animale"

class Cane(Animale):
    def parla(self):
        return "Bau!"

def crea_animale(cls: Type[Animale]) -> Animale:
    return cls()

# ------
class Box(Generic[T]):
    def __init__(self, valore: T):
        self.valore = valore

    def get_valore(self) -> T:
        return self.valore

# ------
Numero = TypeVar("Numero", int, float)
def media(valori: list[Numero]) -> float:
    return sum(valori) / len(valori) if valori else 0.0


