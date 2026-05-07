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

## Clase 5
    Vemos las conversion de objetos (downcasting y upcasting),clases object ,clases abstractas

### Conversion de Objetos
- **Upcasting**: Es la conversión de un objeto de una subclase a un tipo de su superclase. Es segura y se realiza automáticamente, ya que la subclase es un tipo de su superclase.
- **Downcasting**: Es la conversión de un objeto de una superclase a un tipo de su subclase. Es insegura y requiere una conversión explícita, ya que no todas las instancias de la superclase son necesariamente instancias de la subclase.

### Clases Object
La clase `Object` es la superclase raíz de todas las clases en Java. Todos los objetos en Java heredan de `Object`, lo que significa que tienen acceso a sus métodos, como `toString()`, `equals()`, `hashCode()`, entre otros.
* `equals()` es un método que se utiliza para comparar dos objetos en Java. Por defecto, el método `equals()` en la clase `Object` compara las referencias de los objetos, lo que significa que solo devuelve `true` si ambos objetos son la misma instancia. Sin embargo, muchas clases sobrescriben este método para proporcionar una comparación basada en el contenido de los objetos, lo que permite comparar objetos de manera más significativa.
* `hashCode()` es un método que devuelve un valor entero que representa el código hash del objeto. Este código se utiliza principalmente en estructuras de datos como `HashMap` y `HashSet` para almacenar y recuperar objetos de manera eficiente. Es importante que si se sobrescribe el método `equals()`, también se sobrescriba el método `hashCode()` para mantener la coherencia entre ambos métodos.

### Clases Abstractas
Una clase abstracta en Java es una clase que no puede ser instanciada y que puede contener métodos abstractos (métodos sin implementación) y métodos concretos (métodos con implementación). Las clases abstractas se utilizan para definir una plantilla para otras clases, permitiendo que las subclases proporcionen implementaciones específicas para los métodos abstractos.