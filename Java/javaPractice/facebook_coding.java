import java.util.Arrays;

public class facebook_coding {

    public static void main(String[] args) {
        
        int[] a={-1,1,3,4};
        Arrays.sort(a);
        for(int i=1;i<=a.length;i++){
            int k=Arrays.binarySearch(a, i);
            if(k<=-1){
                System.out.println(i);
                break;
            }
            //System.out.println(k+" "+i);
            
        }
    }
}