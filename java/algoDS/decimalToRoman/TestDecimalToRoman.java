public class TestDecimalToRoman {
    public static void main(String[] args) {
	int n = 24;
	System.out.println("[V] TestDecimalToRoman: n=[" + n + "]");
	String romanNumeral = decimalToRoman_v1(n);
        System.out.println("[V] TestDecimalToRoman: romanNumeral=[" + romanNumeral + "]");

    }

    public static String decimalToRoman_v1(int num) {
	System.out.println("[D] decimalToRoman_v1: num=[" + num + "]");

        int[] decimals = new int[] {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        String[] romans = new String[] {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};

        StringBuilder sb = new StringBuilder();
        int quotient = 0;

        for (int i = decimals.length-1; i >= 0; i--) {
            quotient = num / decimals[i];
            num %= decimals[i];

            while (quotient > 0) {
                sb.append(romans[i]);
                quotient--;
            }
        }

        String romanNumeral = sb.toString();

	System.out.println("[V] decimalToRoman_v1: romanNumeral=[" + romanNumeral + "]");
    
	return romanNumeral;
    }
}

