package excepciones;


public class OperacionExcepcion extends RuntimeException {
    //Constructor que recibe un mensaje de error personalizado
    public OperacionExcepcion(String mensaje) {
        super(mensaje);
    }

}
