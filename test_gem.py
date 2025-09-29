# import copy

# nums = [1, 2, 3, 4, 5]
# vals = copy.copy(nums)
# del vals[1:2]
# print(nums)
# print(vals)

# from typing import Generic, TypeVar

# T = TypeVar("T")

# class Box(Generic[T]):
#     def __init__(self, valore: T):
#         self.valore= valore

#     def get_valore(self) -> T:
#         return self.valore


# scatola_int= Box(10)
# scatola_str = Box("ciao")
# print(scatola_int.get_valore()) # int
# print(scatola_str.get_valore()) # str

# from typing import TypeVar, Generic

# K = TypeVar("K")
# V = TypeVar("V")

# class Pair(Generic[K, V]):
#     def __init__(self, key: K, value: V):
#         self.key = key
#         self.value = value

#     def get_key(self) -> K:
#         return self.key

#     def get_value(self) -> V:
#         return self.value
    
# pair = Pair("id", 123)
# print(pair.get_key())   # str
