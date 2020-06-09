
class A {
    static int inc = 0;

   synchronized static void man() {
        inc++;
    }

}

public class thread {
    public static void main(String[] args) throws Exception {
        Thread t1 = new Thread(() -> {
            {
                for (int i = 0; i < 10000000; i++) {
                    A.man();
                }
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i = 0; i < 10000000; i++)
                A.man();
        });
        t1.start();
        t2.start();

        t1.join();
        t2.join();

        System.out.println("in main " + A.inc);
    }
}