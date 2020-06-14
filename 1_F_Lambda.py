"""
También se les conoce como funciones anónimas u on the go,
on demand, online

Una función lambda es una función
anónima y se utilizan para abreviar y ahorrarnos tiempo,
consiste en resumir una función normal en una expresión
lambda, todo lo que podemos hacer con una expresión lambda
se puede hacer con una función normal, pero no al revés

"""
"""
Supongamos que vamos a utilizar está función 15 o más veces

Bajo ese escenario la función lambda nos va a servir ya que nos 
permite que funciones sencillas se puedan resumir aún mas
la sintaxis

Si es una función con muchos bucles,muchos cálculos,condicionales 
no se podrá resumir

SINTAXIS lambda valores: operacion con valores


"""
"""
def area_triangulo(base,altura):
	return (base*altura)/2

triangulo1 = area_triangulo(5,7)
triangulo2 = area_triangulo(9,6)

print(triangulo1,triangulo2)

"""

#Simplificando la sintaxis con lambda
#Creamos una variable y establecemos los parámetros que va a recibir esa funcion anónima
#Podemos usar el número de parámetros que queramos
#los dos puntos son el return 

area_triangulo = lambda base,altura:(base*altura)/2


print(area_triangulo(7,5))
print(area_triangulo(9,6))

