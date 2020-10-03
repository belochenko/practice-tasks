import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in = new Scanner (System.in);
		int h1, m1, s1, h2, m2, s2;
		int time, res_time, h3, m3, s3, sum1, sum2, mid_res;
 
		h1 = in.nextInt();
		m1 = in.nextInt();
		s1 = in.nextInt();
		h2 = in.nextInt();
		m2 = in.nextInt();
		s2 = in.nextInt();
 
		sum1 = h1 + 24 * m1 + 24 * 60 * s1;
		sum2 = h2 + 24 * m2 + 24 * 60 * s2;
		mid_res = (sum2 - sum1 + 86400)%86400;
		time = h1 * 3600 + m1 * 60 + s1;
		res_time = (time + mid_res)%86400; //right time in sec
 
		s3 = res_time%60;
		m3 = ((res_time - s3) / 60)%60;
		h3 = (res_time - m3 * 60 - s3) / 3600;
 
		System.out.printf("%d %d %d", h3, m3, s3);
	}
}