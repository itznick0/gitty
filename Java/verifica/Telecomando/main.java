public class Tester {
    public static void main(String[] args) {
        Telecomando t = new Telecomando();

        t.impostaCanale(3);    // imposta il canale su 3
        t.aumentaVolume();     // volume a 1
        t.aumentaVolume();     // volume a 2
        t.aumentaVolume();     // volume a 3
        t.aumentaVolume();     // volume a 4

        System.out.println("Canale impostato: " + t.getCanale());
        System.out.println("Volume impostato: " + t.getVolume());
    }
}