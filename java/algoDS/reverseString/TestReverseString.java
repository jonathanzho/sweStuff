public class TestReverseString {
    public static void main(String[] args) {
        String inWord = "abc";
        String outWord = reverseString(inWord);
    }

    public static String reverseString(String inWord) {
        String outWord = null;
        if (inWord != null) {
            System.out.println("[D] reverseString: inword=[" + inWord + "]");
        } else {
            System.out.println("[E] reverseString: inWord == null !!!");
            return outWord;
        }
        int len = inWord.length(); 
        if (len <= 1) {
            System.out.println("[I] reverseString: len <= 1. No need to reverse.");
            outWord = inWord;
            return outWord;
        }
        for (int i = 0; i < len/2; i++) {
            char temp = inWord.charAt(i);
	    inWord[i] = inWord[len-1-i];
	    inWord[len-1-i] = temp;
	    i++;
        }
        System.out.println("[V] reverseString: outWord=[" + outWord + "]");
        return outWord;
    }
}

