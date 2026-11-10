package domain;

public class Rectangulo extends FiguraGeometrica {
    //Constructor
    public Rectangulo() {
        super("Rectangulo");
    }

    @Override
    public void dibujar() {
        System.out.println("Se imprime un rectangulo"+ getClass().getSimpleName());
    }
}
