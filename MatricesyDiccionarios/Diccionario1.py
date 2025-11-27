
custom={}
clave=input("ingresa el nombre de la clave:\n")
opciones=(input("ingresa la opcion de valor(str/int/float/lista):\n"))
match opciones:
    case "str":
        valor=input("introduce el valor:\n")
        if valor is None or valor.strip()=="" or valor.isdigit():
            print("error invalido")
        else:
            custom[clave]=valor
    case "int":
        try:
            valor=int(input("Ingresa el valor:\n"))
            custom[clave]=valor
        except ValueError as e:
            print("debe ser numero" ,e)
    case "float":
        try:
            valor=float(input("ingresa el valor float:\n"))
            custom[clave]=valor
        except ValueError as e:
            print("debe ser un float " ,e)
    case "lista":
        lista=[]
        seguir=True
        while seguir:
            valor=input("ingresa el valor para la lista:\n")
            lista.append(valor)
            if input("deseas seguir metiendo en la lista(si/no):\n").lower() !="si":
                seguir=False
        custom[clave]=lista
print(custom)
