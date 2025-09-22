# with open("hello.txt", "r") as fl:
#     fl.seek(10)  # Sposta il cursore alla posizione 10
#     v = fl.read()      # Legge da quella posizione
#     print(v)


# seek(posizione) : sposta il cursore alla posizione specificata
# seek(0) : riporta il cursore all'inizio del file
# seek(10) : sposta il cursore alla posizione 10 (l'undicesimo carattere, contando da 0)
# seek(offset, whence) : sposta il cursore di 'offset' byte, dove 'whence' può essere:
#    0 : dall'inizio del file (default)
#    1 : dalla posizione corrente
#    2 : dalla fine del file

# with open("hello.txt", "r") as fl:
#     fl.seek(0, 0)           # va all'inizio
#     fl2 = fl.seek(10, 1)  # sposta di 10 byte dalla posizione corrente
#     fl3 = fl.seek(-5, 2)  # sposta di -5 byte dalla fine del file



with open("hello.txt", "r") as fl:
    fl.seek(50)          
    porzione_testo = fl.read()
    print(porzione_testo)


with open("hello.txt", "r") as fl:
    posizionamento = fl.tell()
    print("Posizione iniziale del cursore:", posizionamento)
    fl.seek(12)          
    posizione_aggiornata = fl.tell()
    print("Posizione aggiornata del cursore:", posizione_aggiornata)


with open("hello.txt", "r") as fl:
    contenuto_completo = fl.read()
    fl.seek(0)  # Torna all'inizio del file
    contenuto_completo = fl.readlines()
    print(contenuto_completo)