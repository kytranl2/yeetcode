package yeetcode.happyNumber;

import java.util.HashSet;
import java.util.Set;

public class happyNumber {
    static int square(int n) {
        int total = 0;
        String nString = Integer.toString(n);
        for (int i = 0; i < nString.length(); i++) {
            int cInt = Character.getNumericValue(nString.charAt(i));
            total += cInt * cInt;
        }
        return total;
    }
    static boolean isHappy(int n) {
        Set<Integer> s = new HashSet<Integer>();
        int cSquare = square(n);
        while (cSquare != 1) {
            if (!s.add(cSquare)) {
                return false;
            } 
            cSquare = square(cSquare);
        }
        return true;
    }
    public static void main(String[] args) {
        int a = 2;
        System.out.println(isHappy(19));
    }
}
