public class Computadora {
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;
    //CONSTRUCTOR VACIO PARA INICIALIZAR EL ID DE LA COMPUTADORA
    private Computadora() {
        this.idComputadora = ++Computadora.contadorComputadoras;
    }
    //CONSTRUCTOR PARA INICIALIZAR LOS ATRIBUTOS DE LA COMPUTADORA
    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton) {
        this();
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }
    //GETTER AND SETTER PARA LOS ATRIBUTOS DE LA COMPUTADORA
    public int getIdComputadora() {
        return idComputadora;
    }

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public Monitor getMonitor() {
        return monitor;
    }
    public void setMonitor(Monitor monitor) {
        this.monitor = monitor;
    }
    public Teclado getTeclado() {
        return teclado;
    }
    public void setTeclado(Teclado teclado) {
        this.teclado = teclado;
    }
    public Raton getRaton() {
        return raton;
    }
    public void setRaton(Raton raton) {
        this.raton = raton;
    }
    //TO STRING PARA MOSTRAR LOS ATRIBUTOS DE LA COMPUTADORA
    @Override
    public String toString() {
        return """
               Computadora{
                idComputadora=""" + idComputadora +
                "\n nombre='" + nombre + '\'' +
                "\n monitor=" + monitor +
                "\n teclado=" + teclado +
                "\n raton=" + raton +
                '}';
    }

}
