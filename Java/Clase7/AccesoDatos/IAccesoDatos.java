package AccesoDatos;

public interface IAccesoDatos {
    int MAX_REGISTRO = 10; // CONSTANTE, es decir, publico, estatico y final

    //Metodos insertar, listar, actualizar y eliminar son abstractos, es decir, publicos y abstractos
    void insertar();
    void listar();
    void actualizar();
    void eliminar();
}
