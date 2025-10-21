import java.io.*;

public class Main
{
	public static void main(String[] args) {
	    int h, min;
	    Orologio o;
		String valore;
        InputStreamReader input=new InputStreamReader(System.in);
        BufferedReader tastiera=new BufferedReader(input); 
        try {
            o=new Orologio();
            o.visualizza();
            
            System.out.println("Inserire le ore: ");
            valore=tastiera.readLine();
            h=Integer.valueOf(valore).intValue();
            o=new Orologio(h);
            o.visualizza();
            
            System.out.println("Inserire le ore: ");
            valore=tastiera.readLine();
            h=Integer.valueOf(valore).intValue();
            System.out.println("Inserire i minuti: ");
            valore=tastiera.readLine();
            min=Integer.valueOf(valore).intValue();
            o=new Orologio(h,min);
            o.visualizza();
            
            System.out.println("Inserire le ore della sveglia: ");
            valore=tastiera.readLine();
            h=Integer.valueOf(valore).intValue();
            System.out.println("Inserire i minuti della sveglia: ");
            valore=tastiera.readLine();
            min=Integer.valueOf(valore).intValue();
            o.sveglia(h,min);
        } catch(IOException e){}
	}
}
