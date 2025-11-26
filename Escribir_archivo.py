import socket as sk

def escribirArchivo(texto):
    with open("archivo.txt","a") as f:
        f.write(texto+"\n")

sock=sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
sock.bind(("127.0.0.1",6001))

while True:
    datos,direccion=sock.recvfrom(1024)
    info=datos.decode()
    escribirArchivo(info)
    print("guardado" ,info)
