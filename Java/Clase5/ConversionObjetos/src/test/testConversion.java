package test;

import domain.*;
public class testConversion {

        public static void main(String[] args) {
            Escritor escritor = new Escritor("Juan", 50000, TipoEscritura.CLASICO);
            Empleado empleado = escritor; // Conversión implícita (upcasting)

            System.out.println("Detalles del Empleado:");
            System.out.println(empleado.obtenerDetalles());

            // Para acceder a métodos específicos de Escritor, necesitamos hacer un downcasting
            if (empleado instanceof Escritor) {
                Escritor escritor2 = (Escritor) empleado; // Conversión explícita (downcasting)
                System.out.println("Tipo de Escritura: " + escritor2.getTipoEscritura().getDescripcion());
            }
        }
}
