
import java.util.Scanner;
class find_position{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
int i=1;
        while(n-i>0){
            n=n-i;
            i++;
        }
        System.out.println(n);

    }
}