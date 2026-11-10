class Empleado {
    constructor(nombre, salario) {
        this.nombre = nombre;
        this.salario = salario;
    }

    obtenerDetalles() {
        return `Empleado: Nombre: ${this.nombre}, Salario: ${this.salario}`;
    }
}

class Gerente extends Empleado {
    constructor(nombre, salario, departamento) {
        super(nombre, salario);
        this.departamento = departamento;
    }

    obtenerDetalles() {
        return `Gerente: Nombre: ${this.nombre}, Salario: ${this.salario}, Departamento: ${this.departamento}`;
    }
}

function imprimir(tipo){
    console.log(tipo.obtenerDetalles());
    if (tipo instanceof Gerente) {
        console.log("Es un gerente");
        console.log("Departamento: " + tipo.departamento);
    } else if (tipo instanceof Empleado) {
        console.log("Es un empleado");
    }
    else if (tipo instanceof Object) {
        console.log("Es un objeto");
    }
}

let gerente1 = new Gerente("Juan", 50000, "Ventas");
console.log(gerente1.obtenerDetalles());//Objeto de la clase Gerente, que hereda de Empleado, 
// y se muestra su información utilizando el método obtenerDetalles() que ha sido sobrescrito en la clase Gerente.

let empleado1 = new Empleado("Ana", 30000);
console.log(empleado1.obtenerDetalles());//Objeto de la clase Empleado, que muestra su información utilizando el método obtenerDetalles() definido en la clase Empleado.



/* EL polimorfismo permite que un mismo método se comporte de manera diferente según la clase del objeto que lo invoca 
*/


imprimir(gerente1);//Se llama a la función imprimir() pasando el objeto gerente1 como argumento,
// lo que demuestra el polimorfismo, ya que la función puede aceptar objetos de diferentes clases (Empleado y Gerente) y llamar al método obtenerDetalles() correspondiente a cada clase.

imprimir(empleado1);//Se llama a la función imprimir() pasando el objeto empleado1 como argumento,
// lo que demuestra el polimorfismo, ya que la función puede aceptar objetos de diferentes clases (Empleado y Gerente) y llamar al método obtenerDetalles() correspondiente a cada clase.
