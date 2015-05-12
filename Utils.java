package chessfinalproject;

public class Utils
	{
	public static int[] algebraic_to_cartesian(String algebraic)
		{
		int[] cartesian = {0,0};
		
		String x_string = algebraic.substring(0,1);
		String y_string = algebraic.substring(1,2);
		
		cartesian[0] = ((int) x_string.charAt(0)) - 97;
		cartesian[1] = Integer.parseInt(y_string) - 1;
		
		return cartesian;
		}
	
	public static String cartesian_to_algebraic(int[] cartesian)
		{
		String algebraic = "";
		
		algebraic += ((char) (cartesian[0] + 97));
		algebraic += String.valueOf(cartesian[1] + 1);
		
		return algebraic;
		}
	}
