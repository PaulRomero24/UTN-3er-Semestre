
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Listado {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();

        //MENU
        var salir = false;
        while(!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            }catch(Exception e){
                System.out.println("Ocurrio un error "+ e.getMessage());
            }
            System.out.println();
        }
    }

    private static void mostrarMenu(){
        //MOSTRAMOS LAS OPCIONES
        System.out.println(
            """
                ***********LISTADO DE PERSONAS************
                1- Agregar
                2- Listar
                3- Salir        
                    """
        );
        System.out.println("Digite una de las opciones: ");
    }

    private static boolean ejecutarOperacion(Scanner entrada,List<Persona>personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //REVISAMOS LA OPCION A DIGITAR CON UN SWITCH

        switch(opcion){
            case 1 -> {
                System.out.println("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.println("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.println("Digite el correo: ");
                var email = entrada.nextLine();
                //Creamos  el objeto persona
                var persona = new Persona(nombre, tel, email);
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+ "elementos ");
            }
            case 2 -> {
                System.out.println("Listado de personas: ");
                //Mejoras de lambda y el metodo de referencia
                //personas.forEach((persona)-> System.out.println(persona));
                personas.forEach(System.out::println);
            }
            case 3 -> {
                System.out.println("Hasta pronto");
                salir = true;
            }
            default -> System.out.println("Opcion incorrecta: "+opcion);
        }
        return salir;
    }
}
