# truncate con una grandezza specificata

# with open("hello.txt", "wb") as fl:
#     fl.truncate(10)  # Trunca il file a 10 byte


# truncate(size) : riduce la dimensione del file a 'size' byte
# Se 'size' non è specificato, il file viene troncato alla posizione corrente 
# Se 'size' è maggiore della dimensione attuale del file, il file viene esteso con byte nulli
# Se 'size' è minore della dimensione attuale del file, il file viene ridotto
# Esempio:  truncate(10) riduce il file a 10 byte
# Esempio:  truncate() senza argomenti riduce il file alla posizione corrente

# -------------------------------------------------------------------------
# truncate con seek 

with open("hello.txt", "r+") as fl:
    contenuto = fl.read()
    print(contenuto)
    print("Lunghezza originale del file:", len(contenuto))

    fl.seek(5)  # Sposta il cursore alla posizione 5
    fl.truncate()  # Trunca il file alla posizione corrente (5 byte)

    fl.seek(0)  # Torna all'inizio del file
    contenuto_troncato = fl.read()
    print(contenuto_troncato)
    print("Lunghezza del file dopo il truncate:", len(contenuto_troncato))

# -------------------------------------------------------------------------

# # svuoto un file con la truncate
# with open("hello.txt", "wb") as fl:
#     fl.truncate(0)  # Trunca il file a 0 byte, svuotandolo

