# Casi strani ma importanti
print(float('inf'))   # infinite
print(float('-inf'))  # -infinite
print(float('nan'))   # nan (not a number)
print(float('nan') == float('nan'))  # False
print(float('nan') is float('nan'))  # False
print(float('nan') != float('nan'))  # True
print(type(float('nan')))  # <class 'float'>
print(int(float('nan')))  # Errore ValueError
print(int(float('inf')))  # Errore OverflowError
print(int(float('-inf'))) # Errore OverflowError
print(str(float('inf')))  # "inf"
print(str(float('-inf'))) # "-inf"
print(str(float('nan')))  # "nan"
print(bool(float('inf')))  # True
print(bool(float('-inf'))) # True
print(bool(float('nan')))  # True