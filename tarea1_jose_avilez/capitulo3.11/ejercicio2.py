# Reescribe el programa del salario usando try y except, de mode que el
# programa sea capaz de gestionar entradas no numericas con elegancia, mostrando
# un mensaje y saliendo del programa. A continuacion se muestran dos ejecuciones
# del programa.

try:
    horas = float(input("Introduzca las Horas: "))
    tarifa = float(input("Introduzca la Tarifa por hora: "))

    horasCut = 40.00
    horasOver = 0.00
    salario = 0.00

    if horas > horasCut:
        horasOver = horas - horasCut
        
    if horasOver > 0:
        salario = (horasCut * tarifa) + (horasOver * (tarifa * 1.5))
    else:
        salario = horas * tarifa
          
    print("Salario:", salario)
except:
    print("Error, por favor introduzca un numero")