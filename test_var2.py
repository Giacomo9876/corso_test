class Persona:
    specie = "Homo sapiens"   # variabile di classe

    def __init__(self, nome):
        self.nome = nome      # variabile di istanza

p1 = Persona("Luca")
p2 = Persona("Maria")

print(p1.specie)  # Homo sapiens
print(p2.specie)  # Homo sapiens

Persona.specie = "Homo sapiens sapiens"  # modifico la variabile di classe

print(p1.specie)  # Homo sapiens sapiens
print(p2.specie)  # Homo sapiens sapiens


# self : cambia la variabile di istanza collegata a quell'oggetto quindi modifichi solo quell'oggetto

# variabile di classe : dentro la classe ma fuori da i metodi, se un istanza modifica essa la modifica
# avviene su tutte(tranne se viene sovrascritta p1.specie localmente)