import java.util.*;
import java.lang.*;
import java.io.*;
 
class Main
{
	public static int log2(long N) 
    { 
        int result = (int)(Math.log(N) / Math.log(2)); 
 
        return result; 
    } 
 
	public static void main (String[] args) throws java.lang.Exception
	{
		Scanner in = new Scanner(System.in);
 
		long in_val = in.nextInt(), tmp_val = in_val, max_val, power;
		power = (long)Math.pow(2, Math.floor(log2(in_val)) + 1);
		tmp_val = in_val;
		max_val = in_val;
		do{
			in_val <<= 1;
			in_val = in_val % power + (in_val >= power ? 1 : 0);
			if (max_val < in_val) max_val = in_val;
		}while (tmp_val != in_val);
		System.out.println(max_val);
	}
}