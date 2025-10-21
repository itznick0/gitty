public class Telecomando {
    private int canale;
    private int volume;

    public Telecomando() {
        canale = 1;   // canale di default
        volume = 0;   // volume di default
    }

    public Telecomando(int canale, int volume) {
        this.canale = canale;
        this.volume = volume;
    }

    public void aumentaVolume() {
        volume++;
    }

    public void diminuisciVolume() {
        if (volume > 0)
            volume--;
    }

    public void piu() {
        canale++;
    }

    public void meno() {
        if (canale > 1)
            canale--;
    }

    public void impostaCanale(int c) {
        if (c > 0)
            canale = c;
    }

    public int getCanale() {
        return canale;
    }

    public int getVolume() {
        return volume;
    }
}