x = "variabile globale"

def my_function():
    x = "variabile locale"
    print(x)  # Accessing the global variable

my_function()  # Output: variabile locale
print(x)  # Output: variabile globale