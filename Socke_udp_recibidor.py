import socket as sk

sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
sock.bind(("127.0.0.1",5001))

print("servidor udp escuchando")

while True:
    datos,direccion=sock.recvfrom(1024)
    print(f"Mensaje: " ,datos.decode(), "/desde " ,direccion)