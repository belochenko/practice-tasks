import java.util.;
import java.lang.;
import java.io.*;
import java.util.Scanner;
import java.lang.Math;

class Main
{
    public static void main (String[] args) throws java.lang.Exception
    {
        Scanner i = new Scanner(System.in);
        long a = i.nextInt();
        long b = i.nextInt();
        long c = i.nextInt();
        System.out.println(Math.max(Math.max(a, b), c) + Math.min(Math.min(a,b), c));
    }
}