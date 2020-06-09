class Parent{

}
class C extends Parent{
    void man(int i,float f){
        System.out.println("man in p");
    }
    void man(float f,int i){
        System.out.println("man1 in C");
    }
    void man(StringBuffer k){
        System.out.println("in buffewr==");
    }
}
public class prac2{
    public static void main(String[] args) {
       C i = new C();
       i.man(12,34);

    }
}