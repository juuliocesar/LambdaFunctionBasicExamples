#También sirve para hacer labores de formato

destacar_valor = lambda comision:"¡{}!$".format(comision)

nuevo_formato = lambda salario: f"{salario}$$"


comision_Ana = 15585
salario_Enrique = 12000

print(destacar_valor(comision_Ana))
print(nuevo_formato(salario_Enrique))