class Calcolatrice
{
    int a,b;
    
    public Calcolatrice(int a, int b)
    {
        this.a=a;
        this.b=b;
    }
    
    public int addizione()
    {
        return a+b;
    }
    
    public int sottrazione()
    {
        return a-b;
    }
    
    public int moltiplicazione()
    {
        return a*b;
    }
    
    public int divisione()
    {
        try{
            return a/b;
        } catch(Exception e){
            System.out.println("Divisione per 0");
            return 0;
        }
    }
}