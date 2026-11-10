# CLASES DE JAVASCRIPT

## Clase1 :

Creamos un diagrama de clases para representar una jerarquia de clases en JavaScript. En donde creamos clases para representar la venta de productos de una PC(MUNDOPC). Donde relacionamos las clases con herencia y dependencia para cargar los perifericos y la pc a una clase de venta.

## Clase2 :

Modo de uso estricto en JavaScript. En esta clase se muestra como usar el modo estricto para evitar errores comunes en JavaScript, como el uso de variables no declaradas o la asignación de valores a variables constantes.

Se crea una clase de Empleado con un método para obtener detalles del empleado, y luego se crea una clase de Gerente que hereda de Empleado y sobrescribe el método para incluir información adicional sobre el departamento del gerente. Esto es Poo en JavaScript, donde se utilizan clases y herencia para organizar el código de manera más estructurada y reutilizable.

## Clase3 :
En esta clase se muestra el concepto de polimorfismo en JavaScript, donde se puede utilizar el mismo método para diferentes tipos de objetos. En este caso, se crea una función imprimir que acepta un objeto de tipo Empleado o Gerente y llama al método obtenerDetalles() para mostrar la información del objeto. Además, se utiliza el operador instanceof para determinar el tipo de objeto.

## Clase4 :
Vemos como manejar errores con try-catch en JavaScript.Se utiliza un bloque try-catch para manejar ese error y mostrar un mensaje adecuado al usuario. 
El bloque try-catch es una estructura de control de flujo que permite manejar errores de manera elegante y evitar que el programa se detenga abruptamente debido a un error no manejado. En este caso, se intenta ejecutar un código que puede generar un error, y si ocurre un error, se captura en el bloque catch y se muestra un mensaje al usuario.

## Clase5 :
Funciones Arrows en JavaScript. En esta clase se muestra cómo utilizar funciones flecha para escribir funciones de manera más concisa. Las funciones flecha son una forma más corta de escribir funciones anónimas y tienen un comportamiento diferente con respecto al contexto de `this`. Se muestra cómo usar funciones flecha para simplificar el código y mejorar la legibilidad.
Solo pueden ser llamadas luego de ser declaradas, no pueden ser utilizadas antes de su declaración. Esto se debe a que las funciones flecha no se elevan (hoisting) como las funciones tradicionales, lo que significa que no están disponibles para su uso antes de su declaración en el código. Por lo tanto, es importante declarar las funciones flecha antes de intentar utilizarlas para evitar errores de referencia.

## Clase6 :

***operacion asincrona:*** Es una operación que se ejecuta de manera independiente al flujo principal del programa, lo que permite que el programa continúe ejecutándose mientras se espera a que la operación asíncrona se complete. Esto es especialmente útil para operaciones que pueden tomar un tiempo considerable, como solicitudes de red o acceso a bases de datos, ya que evita que el programa se bloquee mientras espera la respuesta.
### Funciones de tipo CallBack 
En esta clase se muestra cómo utilizar funciones de tipo callback para manejar operaciones asíncronas. Las funciones de tipo callback son funciones que se pasan como argumentos a otras funciones y se ejecutan después de que se completa una operación asíncrona, como una solicitud de red o una operación de lectura/escritura de archivos. Se muestra cómo usar funciones de tipo callback para manejar el flujo de ejecución en situaciones asíncronas y evitar bloqueos en el programa.
### Funciones de tipo SetTimeOut
En esta clase se muestra cómo utilizar la función setTimeout para programar la ejecución de una función después de un cierto período de tiempo. La función setTimeout es una función incorporada en JavaScript que permite ejecutar una función después de un retraso especificado en milisegundos. Se muestra cómo usar setTimeout para crear temporizadores y programar tareas que deben ejecutarse después de un cierto tiempo, lo que es útil para crear efectos de animación, retrasar la ejecución de código o realizar tareas periódicas.
### Funciones de tipo SetInterval
En esta clase se muestra cómo utilizar la función setInterval para programar la ejecución de una función de manera repetitiva a intervalos regulares. La función setInterval es una función incorporada en JavaScript que permite ejecutar una función cada cierto período de tiempo especificado en milisegundos. Se muestra cómo usar setInterval para crear temporizadores que se ejecutan de manera continua, lo que es útil para crear efectos de animación, actualizar datos en tiempo real o realizar tareas periódicas sin necesidad de intervención manual.