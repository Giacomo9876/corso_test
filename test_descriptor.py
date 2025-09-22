import os

with open('test_descriptor.txt', 'wb') as f:
    f_descriptor = f.fileno()
    print("File descriptor:", f_descriptor)

    os.write(f_descriptor, b'Hello, world!') # Scrive direttamente nel file usando il file descriptor
    os.write(f_descriptor, b'\nThis is a test file using file descriptors.\n')


print("File descriptor scritto con successo.")

# File descriptor: <_io.BufferedWriter name='test_descriptor.txt'>
# accesso in modalità binaria con mode 'wb'
# os.write richiede dati in byte quindi b'...'  
# os.write(file_descriptor, b'dati in byte')