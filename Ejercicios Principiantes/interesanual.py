cantidad= input(print("Cuanto dinero quiere invertir: "))
cantidad = float(cantidad)

interes = input(print("El interes que desea ganar: "))
interes = (float(interes))/100

years= float(input(print("El numero de años: ")))

valorF = cantidad*(1+interes*years)

print("El valor Futuro es: "+ str(valorF))