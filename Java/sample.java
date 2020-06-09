class hello{
int m;
int show(){
return m;
}
}
class sample{
public static void main(String s[]){

hello k=new hello();
//k.show();
hello k1=new hello();
System.out.println(k.show());
System.out.println(k1.show());
}
}

