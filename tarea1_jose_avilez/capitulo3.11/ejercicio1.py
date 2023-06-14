# Reescribe el programa del calculo de slario para darle al empleado
# 1.5 veces la tarifa horario para todas las horas trabajadas que excedan de 40.

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