import java.util.*;
import java.lang.*;
import java.io.*;
 
class Ideone
{
	public static int gcd(int a, int b) {
		if (b == 0) {
			return a;
		}
		return gcd(b, a % b);
	}
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner i = new Scanner(System.in);
		int m = i.nextInt();
		int n = i.nextInt();
		int gcd_ = gcd(m, n);
		int res1, res2 = 0;
		m /= gcd_;
		n /= gcd_;
		res1 = n + m - 2;
		if (n%2 == 0 & m%2 != 0) {
			res2 = 4;
		}
		if (n%2 != 0 & m%2 != 0) {
			res2 = 3;
		}
		if (n%2 != 0 & m%2 == 0) {
			res2 = 2;
		}
 
		System.out.printf("%d %d", res1, res2);
	}
}