package test;

import domain.*;
public class testAbstract {

    public static void main(String[] args) {
        //FiguraGeometrica figura = new FiguraGeometrica("Figura"); //No se puede instanciar una clase abstracta
        FiguraGeometrica figura = new Rectangulo();
        System.out.println("figura = " + figura);
        figura.dibujar();
    }
}
