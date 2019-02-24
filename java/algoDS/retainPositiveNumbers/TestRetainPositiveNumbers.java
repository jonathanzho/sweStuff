public class TestRetainPositiveNumbers {
    public static void main(String[] args) {
	int[] nums = {1, -2, 3, -4, 5};
	printInts(nums);
	int count = retainPositiveNumbers(nums);
        System.out.println("[V] TestRetainPositiveNumbers: count=[" + count + "]");
	printInts(nums);

    }

    public static int retainPositiveNumbers(int[] nums) {
	int len = nums.length;
	if (len == 0) return 0;
	int count = 0;
	for (int i = 0; i < len; i++) {
	    if (nums[i] > 0) {
		nums[count++] = nums[i];
	    }
	}
	return count;
    }

    public static void printInts(int[] nums) {
        System.out.println("nums=");
	for (int i = 0; i < nums.length; i++) {
	    System.out.println("i=[" + i + "], nums=[" + nums[i] + "]");
	}
    }
}
