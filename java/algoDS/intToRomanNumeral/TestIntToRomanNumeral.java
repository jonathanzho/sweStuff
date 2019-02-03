public class TestIntToRomanNumeral {
    public static void main(String[] args) {
	int n = 24;
	System.out.println("[V] TestIntToRomanNumeral: n=[" + n + "]");
	String romanNumeral = intToRomanNumeral(n);
        System.out.println("[V] TestIntToRomanNumeral: romanNumeral=[" + romanNumeral + "]");

    }

    public static String intToRomanNumeral(int n) {
	System.out.println("[D] intToRomanNumeral: n=[" + n + "]");

        if (n <= 0) return null;

        int num10s = n / 10;
        n = n % 10;

        int num5s = n / 5;    // 0 or 1
        n = n % 5;

        String romanNumeral = new String();

        for (int i = 0; i < num10s; i++) {
	    romanNumeral += "X";
        }

        if (num5s == 1) {
	    romanNumeral += "V";
        }

        switch (n) {
        case 0:
	    break;
        case 1:
	    romanNumeral += "I";
	    break;
        case 2:
	    romanNumeral += "I";
	    romanNumeral += "I";
	    break;
        case 3:
	    romanNumeral += "I";
	    romanNumeral += "I";
	    romanNumeral += "I";
	    break;
        case 4:
	    romanNumeral += "I";
	    romanNumeral += "V";
	    break;
        default:
	    break;
        }

	System.out.println("[V] intToRomanNumeral: romanNumeral=[" + romanNumeral + "]");
    
	return romanNumeral;
    }
}

