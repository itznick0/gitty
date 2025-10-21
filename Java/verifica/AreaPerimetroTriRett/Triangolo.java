public class Triangolo {
    private double cateto1;
    private double cateto2;
    private double ipotenusa;

    public Triangolo(double cateto1, double cateto2, double ipotenusa) {
        this.cateto1 = cateto1;
        this.cateto2 = cateto2;
        this.ipotenusa = ipotenusa;
    }

    public double area() {
        return (cateto1 * cateto2) / 2;
    }

    public double perimetro() {
        return cateto1 + cateto2 + ipotenusa;
    }
}