import java.io.*;
import java.text.DecimalFormat;

public class april29 {
    public static DecimalFormat df=new DecimalFormat("#.##");
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int n=Integer.parseInt(br.readLine());
        double longitude=Double.parseDouble(br.readLine());
        double timeindecimal=(n*1.0*longitude)/360;
        int hours=(int)timeindecimal;

        int minutes=(int)((Double.parseDouble(df.format(timeindecimal))-hours)*100);

        double timeinminutes=minutes*60/100;
        // System.out.println(timeinminutes);


        // Calculate angle of hours and minutes hands

        hours=2;
        timeinminutes=10;
        
        double angle_hours=30*hours;
        double angle_minutes=timeinminutes*6;


        // System.out.println(angle_hours);
        // System.out.println(angle_minutes);

        if(angle_minutes!=0)
        angle_hours=angle_hours+timeinminutes*30/60;

        if(angle_hours==360 )
        angle_hours=0;

        if(angle_minutes==360)
        angle_minutes=0;
        System.out.println(""+Math.abs(angle_hours-angle_minutes)+"  Degrees");
        
    }
}