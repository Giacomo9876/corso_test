import sys

if sys.stdout.isatty():
    print("Standard output is a terminal.")
    print("sto scrivendo su terminale")
else:
    print("l'output effettuato con script viene reindirizzato su un file")