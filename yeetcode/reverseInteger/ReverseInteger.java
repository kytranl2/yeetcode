package yeetcode.reverseInteger;

public class ReverseInteger {
    public static void main(String[] args) {
        // 2147483647
        int number = 1463847413;
        int reversed = reverse(number);
        System.out.println("Original: " + number);
        System.out.println("Reversed: " + reversed);
    }

    public static int reverse(int x) {
        int reversed = 0;
        while (x != 0) {
            int digit = x % 10;
            x /= 10;
            
            // Check for overflow before actually performing the multiplication and addition
            if (reversed > Integer.MAX_VALUE/10 || (reversed == Integer.MAX_VALUE / 10 && digit > 7)) return 0; // Overflow condition for positive values
            if (reversed < Integer.MIN_VALUE/10 || (reversed == Integer.MIN_VALUE / 10 && digit < -8)) return 0; // Underflow condition for negative values
            
            reversed = reversed * 10 + digit;
        }
        return reversed;
    }
}
