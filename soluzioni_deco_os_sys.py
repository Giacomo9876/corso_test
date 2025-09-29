import os
import sys
import time
from functools import wraps

# --- Decoratori ---
# 1. Decoratore stampa inizio/fine
def inizio_fine(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Inizio")
        result = f(*args, **kwargs)
        print("Fine")
        return result
    return wrapper

# 2. Decoratore conteggio chiamate
def conta_chiamate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.chiamate += 1
        print(f"Chiamata numero {wrapper.chiamate}")
        return f(*args, **kwargs)
    wrapper.chiamate = 0
    return wrapper

# 3. Decoratore tempo di esecuzione
def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"Tempo: {end-start:.4f} secondi")
        return result
    return wrapper

# 4. Decoratore con parametro n
def ripeti(n):
    def decoratore(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                f(*args, **kwargs)
        return wrapper
    return decoratore

# 5. Decoratore con controllo ruolo
def solo_admin(f):
    @wraps(f)
    def wrapper(ruolo, *args, **kwargs):
        if ruolo != "admin":
            print("Accesso negato")
            return None
        return f(ruolo, *args, **kwargs)
    return wrapper

# 6. Decoratore cache
def memoize(f):
    cache = {}
    @wraps(f)
    def wrapper(*args):
        if args in cache:
            print("Risultato preso dalla cache")
            return cache[args]
        result = f(*args)
        cache[args] = result
        return result
    return wrapper

# --- OS ---
# 7. Controllo percorso
def controlla_percorso(path):
    if os.path.isfile(path):
        print("È un file")
    elif os.path.isdir(path):
        print("È una cartella")
    else:
        print("Non esiste")

# 8. Backup file .txt
def backup_txt():
    os.makedirs("backup", exist_ok=True)
    for file in os.listdir("."):
        if file.endswith(".txt"):
            os.system(f"cp {file} backup/")

# 9. Elenco file con dimensioni
def lista_file(path="."):
    for file in os.listdir(path):
        full = os.path.join(path, file)
        if os.path.isfile(full):
            print(f"{file}: {os.path.getsize(full)} byte")

# --- SYS ---
# 10. Somma da CLI
def somma_cli():
    if len(sys.argv) < 3:
        print("Uso: python script.py a b")
        return
    a, b = int(sys.argv[1]), int(sys.argv[2])
    print(f"Somma: {a+b}")

# 11. Info interprete
def info_interprete():
    print("Versione:", sys.version)
    print("Piattaforma:", sys.platform)
    print("Path moduli:", sys.path)

# 12. Leggi file da CLI
def leggi_file():
    if len(sys.argv) < 2:
        print("Uso: python script.py <file>")
        return
    with open(sys.argv[1]) as f:
        for riga in f:
            sys.stdout.write(riga)

# --- Mix finale ---
def logger(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print(f"[{time.ctime()}] Chiamata a {f.__name__}")
        return f(*args, **kwargs)
    return wrapper

@logger
def analizza_percorso(path):
    if os.path.isfile(path):
        print(f"{path} è un file di {os.path.getsize(path)} byte")
    elif os.path.isdir(path):
        print(f"{path} è una cartella con contenuti:")
        for e in os.listdir(path):
            print(" -", e)
    else:
        print("Percorso non valido")

def main():
    if len(sys.argv) < 2:
        print("Uso: python script.py <percorso>")
        return
    analizza_percorso(sys.argv[1])

if __name__ == "__main__":
    main()
