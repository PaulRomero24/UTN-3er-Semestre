package test;

import aritmetica.Aritmetica;
import excepciones.OperacionExcepcion;

public class testExcepciones1 {

    public static void main(String[] args) {
        int resultado = 0;
        try {
            resultado = Aritmetica.division(10, 0);

        //Para anidar varias excepciones, se debe colocar primero la mas especifica y
        //luego la mas general siguiendo la jerarquia de clases, es decir, 
        //primero las excepciones hijas y luego las padres
        
        } catch (OperacionExcepcion e) {
            System.out.println("Ocurrion un error desde operacionExcepcion");
            System.out.println(e.getMessage());
        }catch (Exception e) {
            System.out.println("Ocurrio un error desde Exception");
            System.out.println(e.getMessage());
        }
        finally {
            System.out.println("Esto se ejecuta siempre, haya o no una excepcion");
        }
        System.out.println("El resultado es: " + resultado);
        
    }
}
