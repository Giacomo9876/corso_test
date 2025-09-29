import re

def trova_cifre(testo):
    return re.findall(r'\d', testo)

# Test
testo = "Ho 5 gatti, 3 cani e 12 pesci"
print(trova_cifre(testo))  # ['5', '3', '1', '2']

# ------------------------------------------------

import re

def valida_cap(cap):
    pattern = r'^\d{5}$'
    return bool(re.match(pattern, cap))

# Test
print(valida_cap("00100"))  # True
print(valida_cap("1234"))   # False
print(valida_cap("abcde"))  # False

# ----------------------------------------------------

import re

def normalizza_spazi(testo):
    return re.sub(r'\s+', ' ', testo).strip()

# Test
testo = "Ciao    mondo   come     stai"
print(normalizza_spazi(testo))  # "Ciao mondo come stai"

# ----------------------------------------------------

import re

def parole_maiuscole(testo):
    return re.findall(r'\b[A-Z][a-z]+', testo)

# Test
testo = "Mario e Luigi vivono a Roma con Anna"
print(parole_maiuscole(testo))  # ['Mario', 'Luigi', 'Roma', 'Anna']

# ---------------------------------------------------

import re

def valida_telefono(telefono):
    patterns = [
        r'^\d{3}-\d{7}$',           # 339-1234567
        r'^\d{2}-\d{8}$',           # 02-12345678
        r'^\+39\s\d{3}\s\d{7}$'     # +39 339 1234567
    ]
    
    for pattern in patterns:
        if re.match(pattern, telefono):
            return True
    return False

# Test
print(valida_telefono("339-1234567"))     # True
print(valida_telefono("02-12345678"))     # True
print(valida_telefono("+39 339 1234567")) # True
print(valida_telefono("123-456"))         # False

# -----------------------------------------------------

import re

def estrai_hashtag(testo):
    return re.findall(r'#\w+', testo)

# Test
testo = "Amo #Python e #regex! #coding è fantastico"
print(estrai_hashtag(testo))  # ['#Python', '#regex', '#coding']

# --------------------------------------------------------

import re

def censura_carta_credito(testo):
    def sostituisci_carta(match):
        numero = match.group()
        # Rimuovi tutti i separatori
        solo_cifre = re.sub(r'[^\d]', '', numero)
        if len(solo_cifre) == 16:
            # Mantieni formato originale ma con asterischi
            separatori = re.findall(r'[^\d]', numero)
            ultimi_4 = solo_cifre[-4:]
            
            if '-' in numero:
                return f"****-****-****-{ultimi_4}"
            elif ' ' in numero:
                return f"**** **** **** {ultimi_4}"
            else:
                return f"************{ultimi_4}"
        return numero
    
    # Pattern per 16 cifre con possibili separatori
    pattern = r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'
    return re.sub(pattern, sostituisci_carta, testo)

# Test
testo = "La mia carta è 1234-5678-9012-3456"
print(censura_carta_credito(testo))  # "La mia carta è ****-****-****-3456"

# -----------------------------------------------------

import re

def estrai_domini(urls):
    domini = []
    for url in urls:
        # Pattern per estrarre il dominio
        match = re.search(r'://(?:www\.)?([^/]+)', url)
        if match:
            domini.append(match.group(1))
    return domini

# Test
urls = [
    "https://www.google.com/search", 
    "http://facebook.com/profile", 
    "https://youtube.com"
]
print(estrai_domini(urls))  # ["google.com", "facebook.com", "youtube.com"]

# -----------------------------------------------------------------------------

import re

def formatta_telefono(telefono):
    # Rimuovi tutti i caratteri non numerici
    solo_numeri = re.sub(r'[^\d]', '', telefono)
    
    # Formatta in base alla lunghezza
    if len(solo_numeri) == 10:  # Numero cellulare
        return f"{solo_numeri[:3]}-{solo_numeri[3:]}"
    elif len(solo_numeri) == 9:  # Numero fisso
        return f"{solo_numeri[:2]}-{solo_numeri[2:]}"
    else:
        return telefono  # Restituisci originale se formato non riconosciuto

# Test
print(formatta_telefono("339 123-4567"))   # "339-1234567"
print(formatta_telefono("(02) 1234 567"))  # "02-1234567"