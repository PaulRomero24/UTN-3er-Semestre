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

let gerente1 = new Gerente("Juan", 50000, "Ventas");
console.log(gerente1.obtenerDetalles());//Objeto de la clase Gerente, que hereda de Empleado, 
// y se muestra su información utilizando el método obtenerDetalles() que ha sido sobrescrito en la clase Gerente.

let empleado1 = new Empleado("Ana", 30000);
console.log(empleado1.obtenerDetalles());//Objeto de la clase Empleado, que muestra su información utilizando el método obtenerDetalles() definido en la clase Empleado.