import socket as sk
import time

sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
puerto=6001
continuar=True
while continuar:
    mensaje=input("escribe el mensaje:\n")
    sock.sendto(mensaje.encode(),("127.0.0.1",puerto))
    if mensaje=="fin":
        continuar=False
    time.sleep(1)
sock.close()