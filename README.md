#1) Haz una clase llamada Persona que siga las siguientes condiciones:

 Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que
se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo.
Si quieres añadir algún atributo puedes hacerlo.

 Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0 números,
cadena vacía para String, etc.). Sexo será hombre por defecto, usa una constante para ello.

 Se implantarán varios constructores:

o Un constructor por defecto.
o Un constructor con el nombre, edad y sexo, el resto por defecto.
o Un constructor con todos los atributos como parámetro.

 Los métodos que se implementaran son:

calcularIMC(): calculara si la persona está en su peso ideal (peso en kg/(altura^2 en m)), si
esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número
entre 20 y 25 (incluidos), significa que está por debajo de su peso ideal la función devuelve un
0 y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un
1. Te recomiendo que uses constantes para devolver estos valores.

esMayorDeEdad (): indica si es mayor de edad, devuelve un booleano.

comprobar Sexo(char sexo): comprueba que el sexo introducido es correcto. Si no es
correcto, será H. No será visible al exterior.

string(): devuelve toda la información del objeto.

generad NI(): genera un número aleatorio de 8 cifras, genera a partir de este su número
su letra correspondiente. Este método será invocado cuando se construya el objeto.
Puedes dividir el método para que te sea más fácil. No será visible al exterior.

 Métodos que muestren cada parámetro, excepto de DNI.

Ahora, crea una clase ejecutable que haga lo siguiente:

 Pide por teclado el nombre, la edad, sexo, peso y altura.

 Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por
teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último por
defecto, para este último utiliza los métodos set para darle a los atributos un valor.

 Para cada objeto, deberá comprobar si está en su peso ideal, tiene sobrepeso o por debajo de su peso
ideal con un mensaje.

 Indicar para cada objeto si es mayor de edad.

 Por último, mostrar la información de cada objeto.

Puedes usar métodos en la clase ejecutable, para que sea más fácil.

2) Crearemos una superclase llamada Electrodoméstico con las siguientes características:
 Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso. Indica que se
podrán heredar.

 Por defecto, el color será blanco, el consumo energético sera F, el precioBase es de 100 € y el peso de
5 kg. Usa constantes para ello.

 Los colores disponibles son blancos, negro, rojo, azul y gris. No importa si el nombre está en
mayúsculas o en minúsculas.

 Los constructores que se implementarán serán

o Un constructor por defecto.
o Un constructor con el precio y peso. El resto por defecto.
o Un constructor con todos los atributos.

 Los métodos que implementara serán:

o Métodos de todos los atributos.
o comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es
correcta usara la letra por defecto. Se invocará al crear el objeto y no sera visible.
o comprobarColor(String color): comprueba que el color es correcto, sino lo es usa el color
por defecto. Se invocará al crear el objeto y no será visible.
o precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño,
también. Esta es la lista de precios:

![image](https://github.com/jRestrepo23/Taller3_herenciasmultiples/assets/161361508/07ec70f1-a9d4-4b45-b899-06b1aebdf796)

Crearemos una subclase llamada Lavadora con las siguientes características:

 Su atributo es carga, además de los atributos heredados.
 Por defecto, la carga es de 5 kg. Usa una constante para ello.
 Los constructores que se implementarán serán:

o Un constructor por defecto.
o Un constructor con el precio y peso. El resto por defecto.
o Un constructor con la carga y el resto de atributos heredados. Recuerda que debes llamar al
constructor de la clase padre.
 Los métodos que se implementara serán:

o Método get de carga.
o precioFinal():, si tiene una carga mayor de 30 kg, aumentara el precio 50 €, sino es así no se
incrementara el precio. Llama al método padre y añade el código necesario. Recuerda que las
condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.
Crearemos una subclase llamada Television con las siguientes características:

 Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano), ademas de los atributos
heredados.
 Por defecto, la resolución sera de 20 pulgadas y el sintonizador sera false.

 Los constructores que se implementarán serán:

o Un constructor por defecto.
o Un constructor con el precio y peso. El resto por defecto.
o Un constructor con la resolución, sintonizador TDT y el resto de atributos heredados.
Recuerda que debes llamar al constructor de la clase padre.

 Los métodos que se implementara serán:

o Método que devuelva la resolución y sintonizador TDT.
o precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un
30% y si tiene un sintonizador TDT incorporado, aumentara 50 €. Recuerda que las
condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio.

Ahora crea una clase ejecutable que realice lo siguiente:

 Crea un array de Electrodomesticos de 10 posiciones.
 Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
 Ahora, recorre este array y ejecuta el método precioFinal().
 Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones, por un lado, el de
las lavadoras por otro y la suma de los Electrodomesticos (puedes crear objetos Electrodomestico,
pero recuerda que Television y Lavadora también son electrodomésticos). Recuerda el uso operador
instanceof.

Por ejemplo, si tenemos un Electrodoméstico con un precio final de 300, una lavadora de 200 y una
televisión de 500, el resultado final será de 1000 (300+200+500) para electrodomésticos, 200 para lavadora y
500 para televisión



