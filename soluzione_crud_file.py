# Mini CRUD file

FILE_NAME = "dati.txt"


def crea():
    """Crea o sovrascrive il file con nuovo contenuto"""
    testo = input("Scrivi il contenuto da inserire nel file:\n")
    with open(FILE_NAME, "w") as f:
        f.write(testo + "\n")
    print("✅ File creato/sovrascritto con successo.")


def leggi():
    """Legge e stampa il contenuto del file"""
    try:
        with open(FILE_NAME, "r") as f:
            contenuto = f.read()
            if contenuto.strip() == "":
                print("⚠️ Il file è vuoto.")
            else:
                print("\n📄 Contenuto del file:")
                print(contenuto)
    except FileNotFoundError:
        print("❌ Il file non esiste. Crea prima un file.")


def aggiorna():
    """Aggiunge nuove righe al file senza cancellare le precedenti"""
    testo = input("Scrivi cosa vuoi aggiungere al file:\n")
    with open(FILE_NAME, "a") as f:
        f.write(testo + "\n")
    print("✏️ Riga aggiunta con successo.")


def cancella():
    """Svuota completamente il file"""
    with open(FILE_NAME, "w") as f:
        f.truncate(0)
    print("❌ File svuotato con successo.")


def menu():
    while True:
        print("\n--- MENU FILE CRUD ---")
        print("1. Crea/Sovrascrivi file")
        print("2. Leggi file")
        print("3. Aggiorna file")
        print("4. Cancella contenuto file")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            crea()
        elif scelta == "2":
            leggi()
        elif scelta == "3":
            aggiorna()
        elif scelta == "4":
            cancella()
        elif scelta == "0":
            print("👋 Uscita dal programma.")
            break
        else:
            print("Opzione non valida.")


if __name__ == "__main__":
    menu()
