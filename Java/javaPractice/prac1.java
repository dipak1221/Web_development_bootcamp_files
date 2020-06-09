
class P{
   void hello(){
        System.out.println("in P hello");
    }
    Object hello(int k) throws Exception{
        System.out.println("in p hello int value "+k);
        return null;
    }
}

public class prac1 extends P{

    @Override
   String hello(int k)  throws Exception{
       super.hello(k);
      System.out.println("in prac1 hello");
      return null;
   }
    public static void main(String[] args) throws Exception {
        P k=new prac1();
        k.hello(23);
            
    }
}