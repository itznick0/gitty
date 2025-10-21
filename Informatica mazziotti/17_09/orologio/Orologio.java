class Orologio
{
    private int h, min;
    
    Orologio()
    {
        h=9;
        min=0;
    }
    
    Orologio(int h)
    {
        this.h=h;
        min=0;
    }
    
    Orologio(int h, int min)
    {
        this.h=h;
        this.min=min;
    }
    
    public void visualizza()
    {
        System.out.println("Sono le ore "+h+":"+min);
    }
    
    public void sveglia(int hs, int mins)
    {
        if (h==hs && min==mins)
        {
            System.out.println("FEIN FEIN FEIN");
        }
    }
}