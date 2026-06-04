import java.util.Scanner;

public class CalculadoraUTN {

    static Scanner entrada = new Scanner(System.in); // Un solo Scanner compartido

    public static void main(String[] args) {
        while (true) {
            System.out.println("********* Aplicacion Calculadora *********");
            System.out.println("""
                    1- Suma
                    2- Resta
                    3- Multiplicacion
                    4- Division
                    5- Salir
                    """);
            System.out.print("Digite la operacion que desea realizar: ");

            try {
                int eleccion = Integer.parseInt(entrada.nextLine());

                switch (eleccion) {
                    case 1 -> suma();
                    case 2 -> resta();
                    case 3 -> multiplicacion();
                    case 4 -> division();
                    case 5 -> {
                        System.out.println("Hasta luego!");
                        return; // Termina el programa
                    }
                    default -> System.out.println("Opcion invalida. Intente de nuevo.");
                }

            } catch (NumberFormatException e) {
                System.out.println("Entrada invalida. Ingrese un numero.");
            }

            System.out.println();
        }
    }

    public static void suma() {
        double acumulado = leerNumero("Ingresa el primer valor: ");
        acumulado += leerNumero("Ingresa el segundo valor: ");

        while (true) {
            System.out.print("¿Desea seguir sumando? (1- Si / 2- No): ");
            int respuesta = Integer.parseInt(entrada.nextLine());
            if (respuesta == 1) {
                acumulado += leerNumero("Ingresa el siguiente valor: ");
            } else {
                break;
            }
        }

        System.out.println("Resultado: " + acumulado);
    }

    public static void resta() {
        double resultado = leerNumero("Ingresa el primer valor: ");
        resultado -= leerNumero("Ingresa el segundo valor: ");
        System.out.println("Resultado: " + resultado);
    }

    public static void multiplicacion() {
        double resultado = leerNumero("Ingresa el primer valor: ");
        resultado *= leerNumero("Ingresa el segundo valor: ");
        System.out.println("Resultado: " + resultado);
    }

    public static void division() {
        double dividendo = leerNumero("Ingresa el dividendo: ");
        double divisor   = leerNumero("Ingresa el divisor: ");

        if (divisor == 0) {
            System.out.println("Error: no se puede dividir por cero.");
        } else {
            System.out.println("Resultado: " + (dividendo / divisor));
        }
    }

    // Método auxiliar para leer y validar un número
    public static double leerNumero(String mensaje) {
        while (true) {
            System.out.print(mensaje);
            try {
                return Double.parseDouble(entrada.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Valor invalido. Ingrese un numero.");
            }
        }
    }
}