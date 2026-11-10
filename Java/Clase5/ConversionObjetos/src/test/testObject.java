package test;

import domain.*;

public class testObject {

    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 5000);
        Empleado empleado2 = new Empleado("Juan", 5000);

        System.out.println("empleado1: " + empleado1);
        System.out.println("empleado2: " + empleado2);

        if (empleado1 == empleado2) {
            System.out.println("Las referencias son iguales");
        } else {
            System.out.println("Las referencias son diferentes");
        }

        // Para comparar el contenido de los objetos, se debe sobrescribir el método equals en la clase Empleado
        //Esto es hashcode, no es necesario para comparar el contenido, pero es una buena práctica sobrescribirlo junto con equals
        if (empleado1.equals(empleado2)) {
            System.out.println("Los objetos son iguales");
        } else {
            System.out.println("Los objetos son diferentes");
        }
    }
}
