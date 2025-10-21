import java.io.*;

public class Main
{
	public static void main(String[] args) {
	int a,b,scelta;
	String valore;
    InputStreamReader input=new InputStreamReader(System.in);
    BufferedReader tastiera=new BufferedReader(input);
	try {
        System.out.println("Inserire il primo numero: ");
        valore=tastiera.readLine();
        a=Integer.valueOf(valore).intValue();
        System.out.println("Inserire il secondo numero: ");
        valore=tastiera.readLine();
        b=Integer.valueOf(valore).intValue();
        Calcolatrice c=new Calcolatrice(a,b);
        System.out.println("1. Addizione  2. Sottrazione  3. Moltiplicazione  4. Divisione");
        valore=tastiera.readLine();
        scelta=Integer.valueOf(valore).intValue();
        if (scelta==1){
            System.out.println("La somma vale: "+c.addizione());
        }
        else if (scelta==2){
            System.out.println("La sottrazione vale: "+c.sottrazione());
        }
        else if (scelta==3){
            System.out.println("Il prodotto vale: "+c.moltiplicazione());
        }
        else if (scelta==4){
            System.out.println("Il quoziente vale: "+c.divisione());
        }
        else {
            System.out.println("Numero non valido");
        }
    } catch (IOException e) {
    }
	}
}
