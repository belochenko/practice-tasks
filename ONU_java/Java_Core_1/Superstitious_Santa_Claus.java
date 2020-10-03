import java.util.*;
import java.lang.*;
import java.io.*;

class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		int k, a, b, counter = 0;
		Scanner scan = new Scanner(System.in);
		k = scan.nextInt();
		
		while (k > 0) {
			k--;
			a = scan.nextInt();
			b = scan.nextInt();
			for (int i = a; i <= b; i++) {
				if (i%28 == 1 || i%28 == 2 || i%28 == 3 || i%28 == 4 || i%28 == 7 || i%28 == 8 ||
			    i%28 == 13 || i%28 == 14 || i%28 == 16 || i%28 == 18 || i%28 == 19 || i%28 == 25) counter +=2;
			    else if (i%28 == 10 || i%28 == 21 || i%28 == 24 || i%28 == 27) counter += 3;
		        else counter++;
			}
		}
		System.out.println(counter);
	}
}