public class Orden {
    private final int idOrden;
    private final Computadora computadoras[]; //ARREGLO DE COMPUTADORAS PARA ALMACENAR LAS COMPUTADORAS DE LA ORDEN
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;

    public Orden() {
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadoras = new Computadora[Orden.MAX_COMPUTADORAS];
    }

    public int getIdOrden() {
        return idOrden;
    }

    //MÉTODO PARA AGREGAR UNA COMPUTADORA A LA ORDEN Recorrer el arreglo de computadoras y agregar la computadora en la primera posición que sea null
    public void agregarComputadora(Computadora computadora) {
        for (int i = 0; i < this.computadoras.length; i++) {
            if (this.computadoras[i] == null) {
                this.computadoras[i] = computadora;
                break;
            }
        }
    }

    //MÉTODO PARA MOSTRAR LA ORDEN Y LAS COMPUTADORAS QUE CONTIENE LA ORDEN Recorrer el arreglo de computadoras y mostrar cada computadora que no sea null
    public void mostrarOrden() {
        System.out.println("Orden #" + this.idOrden);
        System.out.println("Computadoras en la orden:");
        for (Computadora computadora : this.computadoras) {
            if (computadora != null) {
                System.out.println(computadora);
            }
        }
    }

}
