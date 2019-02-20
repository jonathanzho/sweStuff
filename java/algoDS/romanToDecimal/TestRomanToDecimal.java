public class TestRomanToDecimal {
    public static void main(String[] args) {
        String romalNumeral = "XXIV"; 	
	System.out.println("[V] TestRomanToDecimal: romalNumeral=[" + romalNumeral + "]");
	int num = romanToDecimal_v1(romalNumeral);
        System.out.println("[V] TestRomanToDecimal: num=[" + num + "]");

    }

    public static int romanToDecimal_v1(String romanNumeral) {
	System.out.println("[D] romanToDecimal_v1: romanNumeral=[" + romanNumeral + "]");

        if (romanNumeral.isEmpty()) return 0;

        int[] decimals = new int[] {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        String[] romans = new String[] {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};

        for (int i = decimals.length-1; i >= 0; i--) {
            if (romanNumeral.startsWith(romans[i])) {
                return decimals[i] + romanToDecimal_v1(romanNumeral.substring(romans[i].length()));
            }
        }

        return 0;
    }
}

