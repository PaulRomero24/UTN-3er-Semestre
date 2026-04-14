public class MundoPc {
    public static void main(String[] args) {
        //CREAR COMPONENTES
        Monitor monitor1 = new Monitor("HP", 15.6);
        Teclado teclado1 = new Teclado("USB", "HP");
        Raton raton1 = new Raton("USB", "HP");
        Computadora computadora1 = new Computadora("HP", monitor1, teclado1, raton1);

        Monitor monitor2 = new Monitor("Dell", 17);
        Teclado teclado2 = new Teclado("Bluetooth", "Dell");
        Raton raton2 = new Raton("Bluetooth", "Dell");
        Computadora computadora2 = new Computadora("Dell", monitor2, teclado2, raton2);

        //CREAR ORDENES
        Orden orden1 = new Orden();
        orden1.agregarComputadora(computadora1);
        orden1.agregarComputadora(computadora2);
        orden1.mostrarOrden();

        Orden orden2 = new Orden();
        orden2.agregarComputadora(computadora1);
        orden2.mostrarOrden();
    }
}
