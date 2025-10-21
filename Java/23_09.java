class Cerchio{
    private double raggio;
    public static double PI_GRECO = 3.1415926535;
    
    public Cerchio(double r){
        raggio=r;}
        
    public double perimetro(){
        return raggio*2*PI_GRECO;
    }
        
    public double area(){
        return raggio*raggio*PI_GRECO;
    }
    
    public static double getPI_GRECO(){
        return PI_GRECO;
    }
}

class Main {
    public static void main(String[] args) {
        Cerchio c=new Cerchio(2);
        System.out.println("Perimetro = "+c.perimetro());
        System.out.println("Area = "+c.area());
        System.out.println("Ricordiamo che il pigraco vale "+Cerchio.getPI_GRECO());
    }
}