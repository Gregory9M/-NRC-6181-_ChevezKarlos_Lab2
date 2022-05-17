def saludo(estudiante):
     print("Bienvenido sr," , estudiante)
def diametro(circunferencia,pi):
     diametro=circunferencia/pi
     print("El diametro del circulo es: ",diametro)#esta funcion nos ayuda a poder saber cual es el diametro del circulo
def circunferencia2(diametro2,pi):
     circunferencia2=diametro2*pi
     print("La circunferencia del circulo es: ",circunferencia2)#usando esta funcion podemos determinar la circunferencia del circulo
def area(pi,radio):
     area=pi*radio**2
     print("El area del circulo es: ",area)#con esta funcion sabreamos cual es el area de circulo
pi=float("3.1416")
circunferencia=float(input("Ingrese el valor de la circunferencia: "))
Ingrese el valor de la circunferencia: 18.84
diamtro2=float(input("Ingrese el calor del diametro: "))
Ingrese el calor del diametro: 15
radio=float(input("Ingrese el valor del radio del circulo: "))
Ingrese el valor del radio del circulo: 8
estudiante=str(input("Ingrese los nombre y apellido del estudiante: "))
Ingrese los nombre y apellido del estudiante: KarloS Gregory Chevez
saludo(estudiante)
Bienvenido sr. KarloS Gregory Chevez
diametro(circunferencia,pi)
El diametro del circulo es:  5.99694423223835
circunferencia2(diamtro2,pi)
La circunferencia del circulo es:  47.124
area(pi,radio)
El area del circulo es:  201.0624