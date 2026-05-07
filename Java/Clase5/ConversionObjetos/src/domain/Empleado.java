package domain;

public class Empleado {
    protected String nombre;
    protected double sueldo;

    public Empleado(String nombre,double sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }

    public String obtenerDetalles(){
        return "Nombre: " +this.nombre+", Sueldo: "+ this.sueldo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }

    @Override
    public String toString(){
        return "Empleado{ "+ "nombre: "+ nombre + ", sueldo: "+ sueldo +"}";
    }

    @Override
    // El método equals se utiliza para comparar el contenido de los objetos, en este caso, el nombre y el sueldo
    public boolean equals(Object obj){
        if(this == obj){
            return true;
        }
        if(obj == null || getClass() != obj.getClass()){
            return false;
        }
        Empleado empleado = (Empleado) obj;
        return Double.compare(empleado.sueldo, sueldo) == 0 && nombre.equals(empleado.nombre);
    }

    @Override
    // El método hashCode se utiliza para generar un código hash para el objeto, que se utiliza en estructuras de datos como HashMap o HashSet
    public int hashCode() { 
        int result = nombre != null ? nombre.hashCode() : 0;
        long temp = Double.doubleToLongBits(sueldo);
        result = 31 * result + (int) (temp ^ (temp >>> 32));
        return result;
    }
}