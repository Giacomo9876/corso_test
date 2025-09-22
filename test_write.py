with open("hello.txt", "w+") as fl:
    fl.write("Hello, World!")
    fl.seek(10)  # mi sposto per inserire del testo
    fl.write("Aggiunta di testo.")
    fl.seek(0)  # Torna all'inizio del file per leggere ciò che è stato scritto
    contenuto = fl.read()
    print(contenuto)


def aggiungi_testo_centro(risultato_input):

    with open("hello.txt", "r+") as fl:

        fl.write("Inizio. Fine.") # Scrivo un testo iniziale

        contenuto = fl.read()
        print("Contenuto originale:", contenuto)

        fl.seek(7)  # Mi sposto alla posizione 7
        fl.write(risultato_input)  # Sovrascrivo da quella posizione
        
        fl.seek(0)  # Torna all'inizio del file per leggere ciò che è stato scritto
        nuovo_contenuto = fl.read()
        print("Contenuto dopo l'inserimento:", nuovo_contenuto)



a = input("Vuoi aggiungere del testo al centro del file? ")
aggiungi_testo_centro(a)





