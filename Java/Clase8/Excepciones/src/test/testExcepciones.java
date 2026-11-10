package test;

public class testExcepciones {
    public static void main(String[] args) {
        int resultado = 0;
            resultado = 10/0; 
            // Esto es conocido como una excepcion de tipo ArithmeticException,
            //  que ocurre cuando se intenta dividir un numero entre cero.Hereda de la clase RuntimeException, 
            // lo que significa que es una excepcion no verificada (unchecked exception).
            System.out.println("La variable de resultado es: " + resultado);
    }
}