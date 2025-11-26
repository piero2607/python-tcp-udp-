import time

import socket as sk

sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
puerto=5001
continuar=True
while continuar:
    mensaje=input("Escribe tu mensaje para enviar y (fin) para salir:\n").lower()
    sock.sendto(mensaje.encode(),("127.0.0.1",puerto))
    print("mensaje enviado")

    if mensaje=="fin":
        continuar=False
    time.sleep(1)
sock.close()