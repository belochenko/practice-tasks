import java.util.*;
import java.lang.*;


class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner in = new Scanner (System.in);
        int l = in.nextInt();
        int n = in.nextInt();
        int k = in.nextInt();
        int h = 0;
        for(int i = 0; i < n; i++){
            int x1 = in.nextInt();
            int y1 = in.nextInt();
            int x2 = in.nextInt();
            int y2 = in.nextInt();
            if((x1 * x1 + y1 * y1 <= l * l) || (x2 * x2 + y2 * y2 <= l * l)){
                h++;
            }
            else{
                int a, b, c;
                int dX = x2 - x1;
                int dY = y2 - y1;
                a = dY;
                b = -dX;
                c = y1 * dX - x1 * dY;
                if((c * c <= l * l * (a * a + b * b))&&((-c * b <= (b * b + a * a) * Math.max(y2, y1)) && (-c * b >= (b * b + a * a) * Math.min(y2, y1))))
                    h++;
            }
        }
        System.out.println(h/k+1);
    }
}