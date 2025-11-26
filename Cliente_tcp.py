import socket as sk

sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
sock.connect(("127.0.0.1",4000))
mensaje=input("escribe el mensaje:\n")
sock.send(mensaje.encode())
sock.close()