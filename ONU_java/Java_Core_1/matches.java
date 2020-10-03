import java.util.*;
import java.lang.*;


class Main {
    public static void main (String[] args){
        Scanner in = new Scanner(System.in);
        double n = in.nextDouble();
        double l = Math.floor(Math.sqrt(n));
        double w = Math.ceil(n / l);
        double k = 2 * n + l + w;
        System.out.print((int)(k));
    }
}