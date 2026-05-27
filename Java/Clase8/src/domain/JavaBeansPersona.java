package domain;

import java.io.Serializable;

public class JavaBeansPersona implements Serializable {
    private String nombre;
    private String Apellido;

    public JavaBeansPersona() {
        // Constructor sin argumentos
    }

    public JavaBeansPersona(String nombre, String apellido) {
        this.nombre = nombre;
        this.Apellido = apellido;
    }

//GETTER AND SETTER

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return Apellido;
    }

    public void setApellido(String apellido) {
        Apellido = apellido;
    }

    @Override
    public String toString() {
        return "JavaBeansPersona [nombre=" + nombre + ", Apellido=" + Apellido + "]";
    }

    

}
