import java.util.Scanner;
import java.text.NumberFormat;
import java.util.Locale;

public class currency {

    public static void main(String[] args) {
        /* Read input */
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();
        Locale in=new Locale("en","IN");
        //System.out.println(in);

        NumberFormat us = NumberFormat.getCurrencyInstance(Locale.US);
        NumberFormat india = NumberFormat.getCurrencyInstance(in);
        NumberFormat china = NumberFormat.getCurrencyInstance(Locale.CHINA);
        NumberFormat france = NumberFormat.getCurrencyInstance(Locale.FRANCE);

        /* Print output */
        System.out.println("US: " + us.format(payment));
         System.out.println("India: " + india.format(payment));
        System.out.println("China: " + china.format(payment));
        System.out.println("France: " + france.format(payment));
    }
}