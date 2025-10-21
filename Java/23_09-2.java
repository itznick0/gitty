public class Termometro {
    private double temperatura;
    public Termometro() {
        temperatura = 0.0;    }
    public Termometro(double temperaturaIniziale) {
        temperatura = temperaturaIniziale;    }
    public Termometro incrementa() {
        return new Termometro(temperatura + 1.0);    }
    public Termometro decrementa() {
        return new Termometro(temperatura - 1.0);    }
    public double getTemperatura() {
        return temperatura;    }
    public String toString() {
        return "Temperatura attuale: " + temperatura + "°C";    }
    public static void main(String[] args) {
        Termometro t1 = new Termometro();
        System.out.println("Termometro 1 (default): " + t1);
        t1 = t1.incrementa();
        System.out.println("Dopo incremento: " + t1);
        t1 = t1.decrementa();
        System.out.println("Dopo decremento: " + t1);
        System.out.println();
        Termometro t2 = new Termometro(25.5);
        System.out.println("Termometro 2 (iniziale 25.5°C): " + t2);
        t2 = t2.incrementa().incrementa();
        System.out.println("Dopo due incrementi: " + t2);
        t2 = t2.decrementa();
        System.out.println("Dopo un decremento: " + t2);
        double temp = t2.getTemperatura();
        System.out.println("Temperatura attuale di t2: " + temp + "°C");
    }
}