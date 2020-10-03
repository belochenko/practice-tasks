import java.util.Scanner;
 
public class Main {
    final static double E = 10e-8;
 
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
 
        double x1 = input.nextDouble();
 
        double y1 = input.nextDouble();
 
        double x2 = input.nextDouble();
 
        double y2 = input.nextDouble();
 
        double d = Math.abs((y2 * x1 - x2 * y1) / Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)));
        double a = Math.sqrt(x1 * x1 + y1 * y1);
        double b = Math.sqrt(x2 * x2 + y2 * y2);
 
        int count = 0;
 
        if ((2 * x1 * x1 - 2 * x1 * x2 + 2 * y1 * y1 - 2 * y1 * y2 < 0)
                || (2 * x2 * x2 - 2 * x1 * x2 + 2 * y2 * y2 - 2 * y1 * y2 < 0)) {
            count = (int) (Math.max(a, b) + E) - (int) (Math.min(a, b) - E);
        } else {
            count = (int)(a + E) - (int)(d - E);
            count = count + (int)(b + E) - (int)(d - E);
            if ((Math.abs(Math.round(d) - d) < E) && (Math.abs(d) > E)) {
                count--;
            }
        }
        System.out.println(String.format("%d", count));
    }
}