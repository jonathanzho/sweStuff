public class TestIsPrimeNumber {
    public static void main(String[] args) {
	int n = 1234567;
	System.out.println("[V] TestIsPrimeNumber: n=[" + n + "]");
	boolean prime = isPrimeNumber(n);
        System.out.println("[V] TestIsPrimeNumber: prime=[" + prime + "]");

    }

    public static boolean isPrimeNumber(int n) {
	System.out.println("[D] isPrimeNumber: n=[" + n + "]");

        if (n <= 1) return false;

	for (int i = 2; i < n; i++) {
	    if (n % i == 0) {
		System.out.println("[V] isPrimeNumer: found divisor i=[" + i + "]. The quotient=[" + n/i + "]");
		return false;
	    }
	}

	return true;
    }
}

