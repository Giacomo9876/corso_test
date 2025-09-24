x = 100              # Scope: GLOBALE (modulo)

def funzione():
    y = 50           # Scope: LOCALE (alla funzione)
    print(len)       # Scope di len: BUILT-IN
    return y

class Classe:
    z = 10           # Scope: CLASSE (variabile di classe)

# ---------------------------------------------------------------

x = "globale"

def esterna():
    x = "enclosing"
    
    def interna():
        x = "locale"
        print(x)        # Stampa: "locale"
    
    interna()
    print(x)           # Stampa: "enclosing"

esterna()
print(x)               # Stampa: "globale"

# Output completo:
# locale
# enclosing
# globale

# ----------------------------------------------------------------


def test():
    a = 1
    b = 2
    # Stampa il namespace locale
    print(locals())  # {'a': 1, 'b': 2}
    
    def inner():
        c = 3
        # Stampa namespace locale di inner
        print(locals())  # {'c': 3}
    
    inner()
    return a + b

# Chiama e osserva i namespace
risultato = test()

# ---------------------------------------------------------------

# Versione corretta:
def calcola_totale_fixed(lista_prezzi):
    # Inizializza totale PRIMA del loop
    totale = 0
    for prezzo in lista_prezzi:
        totale = totale + prezzo
    return totale

# Test
prezzi = [10, 20, 30]
print(calcola_totale_fixed(prezzi))  # Stampa 60

# Alternativa con sum()
def calcola_totale_alternativa(lista_prezzi):
    return sum(lista_prezzi)

# ---------------------------------------------------------------

# Configurazione globale
MAX_TENTATIVI = 3
tentativi_fatti = 0

def tenta_operazione():
    global tentativi_fatti  # Necessario per modificare
    
    # Accesso in lettura (non serve global)
    if tentativi_fatti < MAX_TENTATIVI:
        print("Tentativo permesso")
        # Modifica la globale
        tentativi_fatti += 1
        return True
    return False

# Test: chiama 4 volte e osserva
for i in range(4):
    risultato = tenta_operazione()
    print(f"Tentativo {i+1}: {risultato}")

# Output:
# Tentativo permesso
# Tentativo 1: True
# Tentativo permesso
# Tentativo 2: True
# Tentativo permesso
# Tentativo 3: True
# Tentativo 4: False


# ---------------------------------------------------------------

punteggio = 0
livello = 1

def aggiungi_punti(punti):
    # Modifica punteggio globale
    global punteggio
    punteggio += punti
    
def prossimo_livello():
    # Modifica entrambe le globali
    global punteggio, livello
    livello += 1
    punteggio = 0

# Test il sistema di punteggio
aggiungi_punti(100)
print(f"Punteggio: {punteggio}, Livello: {livello}")  # 100, 1
prossimo_livello()
print(f"Punteggio: {punteggio}, Livello: {livello}")  # 0, 2

# ---------------------------------------------------------------

def crea_contatore(iniziale=0):
    conteggio = iniziale
    
    def incrementa():
        # Usa nonlocal per modificare variabile enclosing
        nonlocal conteggio
        conteggio += 1
        return conteggio
    
    return incrementa

# Test: crea due contatori indipendenti
counter1 = crea_contatore()
counter2 = crea_contatore(100)

print(counter1())  # Stampa 1
print(counter1())  # Stampa 2
print(counter2())  # Stampa 101
print(counter1())  # Stampa 3
print(counter2())  # Stampa 102

# ---------------------------------------------------------------

x = "globale"

def esterna():
    x = "enclosing"
    
    def modifica_enclosing():
        nonlocal x  # Modifica x dell'enclosing
        x = "modificato da inner"
    
    def modifica_globale():
        global x    # Modifica x globale
        x = "globale modificato"
    
    print(f"Prima: {x}")                # enclosing
    modifica_enclosing()
    print(f"Dopo enclosing: {x}")       # modificato da inner
    modifica_globale()
    print(f"Dopo global: {x}")          # modificato da inner (locale non cambia)

esterna()
print(f"Globale finale: {x}")           # globale modificato

# Output:
# Prima: enclosing
# Dopo enclosing: modificato da inner
# Dopo global: modificato da inner
# Globale finale: globale modificato

# -------------------------------------------------------------------------

class Contatore:
    # Variabile di classe
    totale_istanze = 0
    
    def __init__(self, nome):
        # Variabile d'istanza
        self.nome = nome
        self.conteggio = 0
        # Incrementa variabile di classe
        Contatore.totale_istanze += 1
        # O anche: self.__class__.totale_istanze += 1
    
    def incrementa(self):
        # Variabile locale
        incremento = 1
        self.conteggio += incremento
    
    @classmethod
    def quante_istanze(cls):
        return cls.totale_istanze

# Test
c1 = Contatore("A")
c2 = Contatore("B")
print(Contatore.quante_istanze())  # Stampa 2
c3 = Contatore("C")
print(Contatore.quante_istanze())  # Stampa 3

# -------------------------------------------------------------------------

# PROBLEMA 1: Soluzione
valore = 10

def problema1_fixed():
    global valore  # Aggiungi global
    print(valore)  # Ora funziona
    valore = 20

# O evita di modificare:
def problema1_alternativa():
    print(valore)  # Solo lettura, OK
    valore_locale = 20  # Usa nome diverso

# PROBLEMA 2: Soluzione senza global
totale = 100

def problema2(incremento):
    # Non modifica globale, usa valore locale
    nuovo_totale = totale + incremento
    return nuovo_totale

risultato = problema2(50)  # 150

# PROBLEMA 3: Loop scope
for i in range(3):
    x = i * 2

print(x)  # Stampa: 4
# x esiste! In Python le variabili dei loop 
# "fuoriescono" dal loop (diverso da altri linguaggi)

# ---------------------------------------------------------------------------

# REFACTORING: Senza variabili globali
def calcola_meglio(x, y):
    """Tutto in una funzione senza global"""
    risultato_temp = x * 2
    risultato_finale = risultato_temp + y
    return risultato_finale

# Test versione migliorata
risultato = calcola_meglio(5, 3)
print(f"Risultato: {risultato}")  # 13

# Versione ancora migliore con operazioni separate
def moltiplica(x, fattore=2):
    return x * fattore

def somma(a, b):
    return a + b

def calcola_pulito(x, y):
    return somma(moltiplica(x), y)

# O in una riga:
calcola_lambda = lambda x, y: x * 2 + y