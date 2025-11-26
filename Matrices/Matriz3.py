divisas = [
    ["Bolívar Venezolano", 202.78],
    ["Guaraní Paraguayo", 8336.03],
    ["Peso Argentino", 1564.31],
    ["Peso Boliviano", 8.07],
    ["Peso Chileno", 1120.74],
    ["Peso Colombiano", 4562.79],
    ["Peso Uruguayo", 46.60],
    ["Real Brasileño", 6.27],
    ["Sol Peruano", 4.09]
]

continuar=True
while continuar:
    moneda_pais=input("ingresa la moneda a la cual quieras hacer el cambio:\n").lower()
    seguir=True
    for moneda,valor in divisas:
        if moneda_pais==moneda.lower():
            seguir=False
            cantidad=float(input("ingresa la cantidad que deseas canbiar en euros:\n"))
            cambio=cantidad*valor
            print(f"El cambio de los euros es: {cambio:.2f} {moneda}")
            continuar=False
    if  seguir:
        print("moneda no encontrada")


