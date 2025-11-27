
nombre_personalizado=input("ingresa el nombre principal para diccionario:\n")
diccionario_principal={nombre_personalizado:[]}
continuar=True
while continuar:
    print(f"agregar nombre de diccionario para {nombre_personalizado} diccionario principal ")
    custom={}
    clave=input("ingresa el nombre de la clave:\n")
    opciones=input("valores disponibles str/int/float/lista:\n")
    match opciones:
        case "str":
            valor=input("ingresa el valor:\n")
            if valor is None or valor.strip()=="" or valor.isdigit():
                print("dato ingresado incorrecto")
            else:
                custom[clave]=valor
        case "int":
            try:
                valor=int(input("Ingresa el valor entero:\n"))
                custom[clave]=valor
            except ValueError as e:
                print("dato invalido" ,e)
        case "float":
            try:
                valor=float(input("ingresa el valor flotante"))
                custom[clave]=valor
            except ValueError as e:
                print("dato invalido",e)
        case "lista":
            lista=[]
            seguir=True
            while seguir:
                valor=input("ingresa el valor que deseas ingresar:\n")
                lista.append(valor)
                if input("deseas seguir ingresando(si/no):\n").lower()!="si":
                    seguir=False
            custom[clave]=lista

    diccionario_principal[nombre_personalizado].append(custom)
    print(diccionario_principal)
    if input("\n¿Agregar otro elemento? (si/no): ").lower() != "si":
        continuar = False

print(f"\n🎉 {diccionario_principal.upper()} FINALIZADO:")
print(diccionario_principal)
