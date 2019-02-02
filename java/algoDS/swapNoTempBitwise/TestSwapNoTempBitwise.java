public class TestSwapNoTempBitwise {
    public static void main(String[] args) {
	int a = 2;
	int b = 3;
	System.out.println("[V] TestSwapNoTempBitwise: input  a=[" + a + "], b=[" + b + "]");
	swapNoTempBitwise(a, b);
        System.out.println("[V] TestSwapNoTempBitwise: output a=[" + a + "], b=[" + b + "]");

    }

    public static void swapNoTempBitwise(int a, int b) {
	System.out.println("[D] swapNoTempBitwise: input   a=[" + a + "], b=[" + b + "]");

	a = a ^ b;
        System.out.println("[V] swapNoTempBitwise: step 1  a=[" + a + "], b=[" + b + "]");

	b = a ^ b;
        System.out.println("[V] swapNoTempBitwise: step 2  a=[" + a + "], b=[" + b + "]");

	a = a ^ b;
	System.out.println("[V] swapNoTempBitwise: step 3  a=[" + a + "], b=[" + b + "]");

	// Note: For Java, int is primitive, so it is passed by value, and output will not change !!!
    }
}

