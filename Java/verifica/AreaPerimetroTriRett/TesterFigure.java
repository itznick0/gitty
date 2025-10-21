import java.io.*;

public class TesterFigure {
    public static void main(String[] args) throws IOException {
        InputStreamReader input = new InputStreamReader(System.in);
        BufferedReader keyboard = new BufferedReader(input);

        // Rettangolo
        System.out.print("Inserisci la base del rettangolo: ");
        double base = Double.valueOf(keyboard.readLine()).doubleValue();
        System.out.print("Inserisci l'altezza del rettangolo: ");
        double altezza = Double.valueOf(keyboard.readLine()).doubleValue();
        Rettangolo r = new Rettangolo(base, altezza);

        // Triangolo rettangolo (tutti i lati forniti dall'utente)
        System.out.print("Inserisci il primo cateto del triangolo: ");
        double cateto1 = Double.valueOf(keyboard.readLine()).doubleValue();
        System.out.print("Inserisci il secondo cateto del triangolo: ");
        double cateto2 = Double.valueOf(keyboard.readLine()).doubleValue();
        System.out.print("Inserisci l'ipotenusa del triangolo: ");
        double ipotenusa = Double.valueOf(keyboard.readLine()).doubleValue();
        Triangolo t = new Triangolo(cateto1, cateto2, ipotenusa);

        double areaRett = r.area();
        double perimRett = r.perimetro();
        double areaTri = t.area();
        double perimTri = t.perimetro();

        System.out.println("\nRettangolo - Area: " + areaRett + ", Perimetro: " + perimRett);
        System.out.println("Triangolo - Area: " + areaTri + ", Perimetro: " + perimTri);

        if (perimRett > perimTri) {
            System.out.println("Il rettangolo ha il perimetro maggiore.");
        } else if (perimTri > perimRett) {
            System.out.println("Il triangolo ha il perimetro maggiore.");
        } else {
            System.out.println("I perimetri sono uguali.");
        }

        if (areaRett > areaTri) {
            System.out.println("Il rettangolo ha l'area maggiore.");
        } else if (areaTri > areaRett) {
            System.out.println("Il triangolo ha l'area maggiore.");
        } else {
            System.out.println("Le aree sono uguali.");
        }
    }
}