# Clases de JAVA

## Clase1

Usamos el mismo diagrama UML que en la clase de JavaScript, pero con sintaxis de Java.

Creamos una diferentes clases con herencia para representar la carga de datos de la venta de una PC.

## Clase2

### Argumentos variables
El método con argumentos variables debe ser el último parámetro.Los parametros con argumentos variables se tratan como un arreglo dentro del método.
Un arreglo es un objeto, por lo que se puede pasar un arreglo directamente al método con argumentos variables

### Bloques estáticos

Los bloques estáticos se ejecutan una sola vez cuando la clase se carga. Se utilizan para inicializar variables estáticas o realizar tareas de configuración que solo necesitan hacerse una vez.

### Enumeraciones
Las enumeraciones (enums) son un tipo de dato especial que representa un conjunto de constantes. Se utilizan para definir un conjunto fijo de valores que una variable puede tomar, lo que mejora la legibilidad y la seguridad del código.

## Clase3

### Auto-boxing y Unboxing
El auto-boxing es la conversión automática que realiza Java entre tipos primitivos y sus correspondientes clases wrapper. Por ejemplo, convertir un int a Integer. El unboxing es el proceso inverso, donde Java convierte automáticamente una clase wrapper a su tipo primitivo correspondiente.

### Ciclo For-each
El ciclo for-each es una forma simplificada de iterar sobre colecciones y arreglos en Java. Permite recorrer cada elemento de una colección sin necesidad de usar un índice o un iterador explícito.

### Modificadores de acceso a clases
Los métodos de acceso pueden ser privados, protegidos, o públicos, dependiendo de la visibilidad que se desee para cada uno.
- **Privado**: Solo accesible dentro de la misma clase.
- **Protegido**: Accesible dentro del mismo paquete y por las subclases.
- **Público**: Accesible desde cualquier parte del programa.    
- **Paquete**: Accesible solo dentro del mismo paquete (sin modificador de acceso).
- Default: Si no se especifica un modificador de acceso, el método es accesible solo dentro del mismo paquete.

## Clase 4

Aprendemos conceptos de sobreescritura y polimorfismo en JAVA

### Sobreescritura(@Override)

La sobreescritura de métodos (method overriding) en Java permite a una subclase proporcionar una implementación específica de un método ya definido en su superclase. Es clave para el polimorfismo, asegurando que se ejecute el comportamiento de la clase hija en tiempo de ejecución. El método debe tener el mismo nombre, parámetros y tipo de retorno.

### Polimorfismo

El polimorfismo en Java es un pilar de la programación orientada a objetos (POO) que permite a objetos de distintas clases responder de formas diferentes a un mismo mensaje o método. Se logra mediante herencia e interfaces, permitiendo que una referencia de una superclase apunte a subclases, mejorando la flexibilidad y reutilización del código