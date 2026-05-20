package test;

import AccesoDatos.*;

public class TestInterface {
    public static void main(String[] args) {
        System.out.println("Test de interfaces");

        // No se pueden crear objetos de una interfaz
        // IAccesoDatos datos = new IAccesoDatos();

        // Se puede crear objetos de las clases que implementan la interfaz
        // ImplementacionMySql datos = new ImplementacionMySql();
        // datos.insertar();
        // datos.listar();
        // datos.actualizar();
        // datos.eliminar();

        // Polimorfismo: Se puede usar la interfaz como tipo de referencia
        IAccesoDatos datos = new AccesoDatos.ImplementacionOracle();
        //datos.insertar();
        //datos.listar();
        //datos.actualizar();
        //datos.eliminar();
        imprimir(datos);
    }

    public static void imprimir(IAccesoDatos datos) {
        datos.listar();
    }
}
