# 1. Converti "Hello World" in maiuscolo
print("Hello World".upper())  # HELLO WORLD

# 2. Converti "PYTHON" in minuscolo
print("PYTHON".lower())  # python

# 3. Confronta due stringhe ignorando maiuscole/minuscole
str1 = "Python"
str2 = "PYTHON"
print(str1.lower() == str2.lower())  # True
# O anche:
print(str1.upper() == str2.upper())  # True

# -------------------------------------------------
# 1. Capitalizza "python programming"
print("python programming".capitalize())  # Python programming

# 2. Capitalizza "HELLO WORLD"
print("HELLO WORLD".capitalize())  # Hello world

# 3. Capitalizza ogni frase in "ciao. come stai? tutto bene."
testo = "ciao. come stai? tutto bene."
frasi = testo.split(". ")
frasi_cap = [f.capitalize() for f in frasi]
print(". ".join(frasi_cap))  # Ciao. Come stai? tutto bene.

# -------------------------------------------------

# 1. Converti "la guida di python" in title case
print("la guida di python".title())  # La Guida Di Python

# 2. Sistema il nome "mario rossi"
print("mario rossi".title())  # Mario Rossi

# 3. Correggi "l'arte della programmazione"
print("l'arte della programmazione".title())  # L'Arte Della Programmazione

# -------------------------------------------------

# 1. Inverti il case di "PyThOn"
print("PyThOn".swapcase())  # pYtHoN

# 2. Applica swapcase due volte a "Hello World"
testo = "Hello World"
prima = testo.swapcase()  # hELLO wORLD
seconda = prima.swapcase()  # Hello World (torna all'originale)
print(seconda)

# -------------------------------------------------

# 1. Rimuovi spazi da "  Python  "
print("  Python  ".strip())  # Python

# 2. Rimuovi solo spazi a sinistra da "   Hello   "
print("   Hello   ".lstrip())  # "Hello   "

# 3. Rimuovi asterischi da "***Python***"
print("***Python***".strip("*"))  # Python

# 4. Rimuovi "abc" da "abcHelloabc"
print("abcHelloabc".strip("abc"))  # Hello  

# 5. Rimuovi "xyz" da "xyzHello Worldxyz"
print("xyzHello Worldxyz".strip("xyz"))  # Hello World 

# -------------------------------------------------

# 1. Sostituisci "Java" con "Python" in "Java è bello"
print("Java è bello".replace("Java", "Python"))  # Python è bello

# 2. Sostituisci solo la prima occorrenza di "a" con "@" in "banana"
print("banana".replace("a", "@", 1))  # b@nana

# 3. Rimuovi tutti gli spazi da "H e l l o"
print("H e l l o".replace(" ", ""))  # Hello

# 4. Sostituisci "cat" con "dog" in "The cat sat on the mat"
print("The cat sat on the mat".replace("cat", "dog"))  # The
# dog sat on the mat

# -------------------------------------------------

# 1. Rimuovi "http://" da "http://www.example.com"
print("http://www.example.com".removeprefix("http://"))  # www.example.com

# 2. Rimuovi ".txt" da "documento.txt"
print("documento.txt".removesuffix(".txt"))  # documento

# 3. Rimuovi "Sig." da "Sig. Rossi"
print("Sig. Rossi".removeprefix("Sig. "))  # Rossi

# -------------------------------------------------

# 1. Dividi "apple,banana,cherry" usando la virgola
print("apple,banana,cherry".split(","))  # ['apple', 'banana', 'cherry']

# 2. Dividi "Hello World Python" in parole
print("Hello World Python".split())  # ['Hello', 'World', 'Python']

# 3. Dividi "nome:cognome:età" sui due punti
print("nome:cognome:età".split(":"))  # ['nome', 'cognome', 'età']

# -------------------------------------------------

# 1. Dividi "Riga1\nRiga2\nRiga3" in righe
print("Riga1\nRiga2\nRiga3".splitlines())  # ['Riga1', 'Riga2', 'Riga3']

# 2. Mantieni i newline dividendo "A\nB\nC"
print("A\nB\nC".splitlines(keepends=True))  # ['A\n', 'B\n', 'C']

# -------------------------------------------------

# 1. Unisci ["Python", "è", "facile"] con spazi
print(" ".join(["Python", "è", "facile"]))  # Python è facile

# 2. Unisci ["2024", "12", "25"] con "-"
print("-".join(["2024", "12", "25"]))  # 2024-12-25

# 3. Unisci ["A", "B", "C"] senza separatore
print("".join(["A", "B", "C"]))  # ABC

# -------------------------------------------------

# 1. Dividi "hello@world.com" sul "@"
prima, sep, dopo = "hello@world.com".partition("@")
print(prima)  # hello
print(sep)    # @
print(dopo)   # world.com

# 2. Dividi "Python=Programming" sul "="
prima, sep, dopo = "Python=Programming".partition("=")
print(prima)  # Python
print(dopo)   # Programming

# -------------------------------------------------

# 1. Trova la posizione di "th" in "Python"
print("Python".find("th"))  # 2

# 2. Trova "Java" in "Python Programming" (gestisci il caso non trovato)
pos = "Python Programming".find("Java")
if pos == -1:
    print("Non trovato")
else:
    print(f"Trovato in posizione {pos}")

# 3. Trova la seconda occorrenza di "o" in "Hello World"
testo = "Hello World"
prima = testo.find("o")  # 4
seconda = testo.find("o", prima + 1)  # 7
print(seconda)

# -------------------------------------------------

# 1. Verifica se "Python" inizia con "Py"
print("Python".startswith("Py"))  # True

# 2. Verifica se "script.py" finisce con ".py"
print("script.py".endswith(".py"))  # True

# 3. Verifica se "image.jpg" finisce con ".jpg" o ".png"
print("image.jpg".endswith((".jpg", ".png")))  # True

# -------------------------------------------------

# 1. Conta quante "a" in "banana"
print("banana".count("a"))  # 3

# 2. Conta quante parole in "Hello World Python"
print(len("Hello World Python".split()))  # 3

# 3. Conta quanti punti in "192.168.1.1"
print("192.168.1.1".count("."))  # 3

# -------------------------------------------------

# 1. Verifica se "12345" contiene solo numeri
print("12345".isdigit())  # True

# 2. Verifica se "Hello" contiene solo lettere
print("Hello".isalpha())  # True

# 3. Verifica se "Python3" è alfanumerico
print("Python3".isalnum())  # True

# -------------------------------------------------

# 1. Verifica se "PYTHON" è tutto maiuscolo
print("PYTHON".isupper())  # True

# 2. Verifica se "hello" è tutto minuscolo
print("hello".islower())  # True

# 3. Verifica se "Hello World" è in title case
print("Hello World".istitle())  # True

# -------------------------------------------------

# 1. Verifica se "   " contiene solo spazi
print("   ".isspace())  # True

# 2. Verifica se "\t\n" contiene solo whitespace
print("\t\n".isspace())  # True

# 3. Verifica se "" è solo spazi
print("".isspace())  # False (stringa vuota ritorna False)

# -------------------------------------------------

# 1. Centra "Python" in 20 caratteri
print("Python".center(20))  # "       Python       "

# 2. Allinea "Test" a sinistra in 10 caratteri con "-"
print("Test".ljust(10, "-"))  # Test------

# 3. Allinea "42" a destra in 5 caratteri con "0"
print("42".rjust(5, "0"))  # 00042

# -------------------------------------------------

# 1. Padda "42" a 5 cifre con zeri
print("42".zfill(5))  # 00042

# 2. Padda "-7" a 4 cifre mantenendo il segno
print("-7".zfill(4))  # -007

# 3. Crea codice prodotto "123" come "PRD00123"
numero = "123"
codice = "PRD" + numero.zfill(5)
print(codice)  # PRD00123

# -------------------------------------------------

# 1. Espandi tab in "A\tB\tC" con dimensione 4
print("A\tB\tC".expandtabs(4))  # A   B   C

# 2. Allinea "Nome\tCognome\tEtà"
print("Nome\tCognome\tEtà".expandtabs(10))  # Nome      Cognome   Età

# -------------------------------------------------

# 1. Converti "Café" in bytes UTF-8
bytes_data = "Café".encode('utf-8')
print(bytes_data)  # b'Caf\xc3\xa9'

# 2. Decodifica b'Python' in stringa
stringa = b'Python'.decode('utf-8')
print(stringa)  # Python

# -------------------------------------------------

# 1. Sostituisci vocali con numeri: a→1, e→2, i→3, o→4, u→5
vocali = "aeiou"
numeri = "12345"
tabella = str.maketrans(vocali, numeri)
print("hello world".translate(tabella))  # h2ll4 w4rld

# 2. Rimuovi tutta la punteggiatura da "Hello, World!"
import string
rimuovi_punt = str.maketrans('', '', string.punctuation)
print("Hello, World!".translate(rimuovi_punt))  # Hello World

# -------------------------------------------------

# 1. Estrai i primi 3 caratteri di "Python"
print("Python"[:3])  # Pyt

# 2. Estrai gli ultimi 2 caratteri di "Programming"
print("Programming"[-2:])  # ng

# 3. Inverti la stringa "Hello"
print("Hello"[::-1])  # olleH

# -------------------------------------------------

# 1. Prendi ogni secondo carattere di "Python"
print("Python"[::2])  # Pto

# 2. Prendi caratteri a indici pari di "ABCDEF"
print("ABCDEF"[::2])  # ACE

# -------------------------------------------------

password = "Python123"
valida = (
    len(password) >= 8 and
    any(c.isalpha() for c in password) and
    any(c.isdigit() for c in password)
)
print(f"Password valida: {valida}")  # True

# OR
# Versione migliorata con controllo spazi
password = "Python123"

# Requisiti:
# - almeno 8 caratteri
# - almeno una lettera
# - almeno un numero
# - nessuno spazio

valida = (
    len(password) >= 8 and
    any(ch.isalpha() for ch in password) and
    any(ch.isdigit() for ch in password) and
    not any(ch.isspace() for ch in password)  # niente spazi
)

print(f"Password valida: {valida}")

