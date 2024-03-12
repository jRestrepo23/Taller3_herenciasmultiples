class persona:
    
    def __init__(self, nombre="", edad=0, dni="", sexo="H", peso=0, altura=0):
        self.nombre = nombre
        self.edad = edad
        self.generarDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
    
    def segundoConstructor(self):
        self.nombre = str(input("Digite su nombre:"))
        self.edad = int(input("Digite su edad:"))
        self.generarDNI()
        self.sexo = str(input("Digite su sexo (M o F):"))
        self.peso = 0
        self.altura= 0
    
    def contructor(self, nombre, edad, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.generarDNI()
        self.sexo = sexo
        self.peso = peso
        self.altura= altura

    def calcularIMC(self):
        import math
        pesoIdeal = -1
        debajo = 0
        sobrepeso = 1
        self.imc = round(self.peso/math.pow(self.altura,2),1)
        if self.imc < 20 :
            return pesoIdeal,print("Esta por debajo de su peso ideal")
        elif self.imc >= 20 and self.imc <= 25 :
            return debajo, print("Esta en su peso ideal")
        else:
            return sobrepeso, print("Usted tiene sobrepeso")
        
    
    def esMayorDeEdad(self):
        mayorDeEdad = False
        if self.edad >= 18 :
            return mayorDeEdad == True , print("Usted es mayor de edad")
        else:
            return mayorDeEdad, print("Usted no es mayor de edad")
        
        
        
    def comprobarSexo(self):
        if self.sexo == "M" or self.sexo == "F" :
            return self.sexo
        else:
            return self.sexo == "M"
        
    def generarDNI(self):
        from random import randint
        numero = randint(10000000,99999999)        
        dniChars = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
        letra = dniChars[numero%23]
        self.dni = repr(numero) + letra
        
    def string(self):     
        print("Informacion de la persona:", sep=" ")
        print("Nombre:", self.nombre)
        print("Sexo:",self.sexo)
        print("Edad:", self.edad)
        print("Peso:", self.peso)
        print("Altura:", self.altura)
    
    def getNombre(self):
        print("Nombre:", self.nombre)

    def getSexo(self):
        print("Sexo:",self.sexo)
    
    def getEdad(self):
        print("Edad:", self.edad)
    
    def getPeso(self):
        print("Peso:", self.peso)
        
    def getAltura(self):
        print("Altura:", self.altura)
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def setSexo(self, sexo):
        self.sexo = sexo
    
    def setEdad(self, edad):
        self.edad = edad
    
    def setPeso(self, peso):
        self.peso = peso
        
    def setAltura(self, altura):
        self.altura = altura
        
class ejecutable(persona):
    
    def contructorTeclado(self):
        self.nombre = str(input("Digite su nombre:"))
        self.edad = int(input("Digite su edad:"))
        self.generarDNI()
        self.sexo = str(input("Digite su sexo (M o F):"))
        self.peso = float(input("Digite su peso:"))
        self.altura = float(input('Digite su altura:'))
    
     


objeto1 = ejecutable()
objeto1.contructorTeclado()
objeto1.calcularIMC()
objeto1.esMayorDeEdad()

print("°°°°°°°°°°°°°°°°°°°°°°°°°°°")
objeto2 = persona()
objeto2.segundoConstructor()
objeto2.setPeso(80)
objeto2.setAltura(1.90)
objeto2.calcularIMC()
objeto2.esMayorDeEdad()
print("°°°°°°°°°°°°°°°°°°°°°°°°°°°")

objeto3 = persona()
objeto3.setNombre("juan")
objeto3.setEdad(20)
objeto3.setAltura(1.60)
objeto3.setPeso(70)
objeto3.setSexo("M")
objeto3.calcularIMC()
objeto3.esMayorDeEdad()

print("°°°°°°°°°°°°°°°°°°°°°°°°°°°")
objeto1.string()
objeto2.string()
objeto3.string()



class electrodomestico:
    
    def __init__(self, precioBase=100,color="blanco",consumo="F",peso=5):
        if color in ("blanco", "negro", "rojo", "azul", "gris"):
            self.color=color
        self.precioBase = precioBase
        self.ConsumoEnergetico(consumo)
        self.peso = peso


    def porDefecto(self, precioBase=100,color="blanco",consumo="F",peso=5):
        
        self.color=color
        self.precioBase = precioBase
        self.ConsumoEnergetico(consumo)
        self.peso = peso

    
    def segundoConstructor(self, precioBase, peso, color="blanco",consumo="F"):
        self.color= color
        self.precioBase = precioBase
        self.ConsumoEnergetico(consumo)
        self.peso = peso

    def constructor(self, precio, color, consumo , peso):
        self.precioBase = precio
        self.color = color
        self.ConsumoEnergetico(consumo)
        self.peso = peso
        
    def getPreciobase (self):
        print("precio base: ", self.precioBase)
    
    def getColor(self):
        print("Color: ", self.color)
    
    def getCosumo_enegetico(self):
        print("Consumo energetico: ", self.consumo)
    
    def getPeso(self):
        print("Peso: ", self.peso)
    
    def setPreciobase(self, precioBase):
        self.precioBase = precioBase
        
    def setColor(self, color):
        self.color = color
    
    def setConsumo_enegetico(self,consumo):
        self.consumo = consumo
    
    def setPeso(self, peso):
        self.peso = peso
    
    def ConsumoEnergetico(self, letra):
        if letra in ("A","B","C","D","E","F"):
            self.consumo = letra
        
    def precioFinal(self):
        if self.consumo == "A":
            self.precioBase = self.precioBase + 100
        elif self.consumo == "B":
            self.precioBase = self.precioBase + 80
        elif self.consumo == "C":
            self.precioBase = self.precioBase + 60
        elif self.consumo == "D":
            self.precioBase = self.precioBase + 50
        elif self.consumo == "E":
            self.precioBase = self.precioBase + 30
        elif self.consumo == "F":
            self.precioBase = self.precioBase + 10

        if 0 < self.peso < 20:
            self.precioBase = self.precioBase + 10
        elif 20 < self.peso < 49:
            self.precioBase = self.precioBase + 50

class lavadora(electrodomestico):
    
    def __init__(self, precioBase=100, color="blanco", consumo="F", peso=5, carga=5):
        super().__init__(precioBase, color, consumo, peso)
        self.carga = carga
    
    def getCarga(self):
        print("Carga: ", self.carga)
    
    def precioFinal(self):
        electrodomestico.precioFinal(self)
        if self.carga > 30:
            self.precioBase = self.precioBase + 50
            
class television(electrodomestico):
    
    def __init__(self, precioBase=100,color="blanco",consumo="F",peso=5,resolucion=20, sintonizador_TDT= False):
        super().__init__(precioBase, color, consumo, peso)
        self.resolucion = resolucion
        self.sintonizador_TDT = sintonizador_TDT
    
    def definicionTV(self):
        print("Resolucion: ", self.resolucion)
        print("Sintonizador TDT: ", self.sintonizador_TDT)
        
    def precioFinal(self):
        electrodomestico.precioFinal(self)
        if self.resolucion > 40:
            self.precioBase = self.precioBase*1.3 
        if self.sintonizador_TDT == True :
            self.precioBase = self.precioBase + 50 
            
todos = ()
todos = list(todos)
            
todos.insert(-1, electrodomestico(consumo="A", peso=78))
todos.insert(-1, electrodomestico(consumo="A", peso=15))
todos.insert(-1, lavadora(consumo="E", peso=50, carga=32))
todos.insert(-1, lavadora(consumo="A", peso=50, carga=64))
todos.insert(-1, television(sintonizador_TDT=False, resolucion=40))
todos.insert(-1, television(sintonizador_TDT=False, resolucion=50)) 

tv,lavad,electodom = 0,0,0
i = 0
for check in todos:
    i+=1
    check.precioFinal()
    
    if isinstance(check,television):
        tv += check.precioBase
    elif isinstance(check,lavadora):
        lavad += check.precioBase
    else:
        electodom += check.precioBase      
    
print("Total Televisiones: " + repr(tv))
print("Total Lavadoras: " + repr(lavad))
print("Total Electrodomesticos varios: " + repr(electodom))

print("Total: " + repr(tv+lavad+electodom))