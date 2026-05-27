package test;

import domain.*;

public class testJavaBeans {
    public static void main(String[] args) {
        // Crear una instancia de JavaBeansPersona
        JavaBeansPersona persona = new JavaBeansPersona();
        
        // Establecer valores utilizando los setters
        persona.setNombre("Juan");
        persona.setApellido("Pérez");
        
        // Obtener valores utilizando los getters
        String nombre = persona.getNombre();
        String apellido = persona.getApellido();
        
        // Imprimir la información de la persona
        System.out.println("Nombre: " + nombre);
        System.out.println("Apellido: " + apellido);
        
        // Imprimir la representación en cadena del objeto
        System.out.println(persona.toString());
    }
}
