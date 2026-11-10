package domain;

import domain.TipoEscritura;
public class Escritor extends Empleado{
    final TipoEscritura tipoEscritura;

    public Escritor(String nombre, double sueldo,TipoEscritura tipoEscritura){
        super(nombre,sueldo);
        this.tipoEscritura = tipoEscritura;
    }

    @Override
    public String obtenerDetalles(){
        return super.obtenerDetalles()+ " , Tipo Escritura: " + tipoEscritura.getDescripcion(); 
    }

    @Override
    public String toString(){
        return "Escritor: "+ "Tipo de Escritura: "+ tipoEscritura + "}" + " " + super.toString();
    }

    public TipoEscritura getTipoEscritura(){
        return this.tipoEscritura;
    }

}
