import socket as sk

sock=sk.socket(sk.AF_INET,sk.SOCK_STREAM)
sock.bind(("127.0.0.1",4000))
sock.listen()
print("Servidor TCP esperando conexiones...")

conexion, direccion = sock.accept()
print("Cliente conectado:", direccion)
continuar=True
while continuar:
    datos=conexion.recv(1024)
    if not datos:
        continuar=False
    print("Mensaje" , datos.decode())

