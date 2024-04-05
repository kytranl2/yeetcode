package yeetcode.validParentheses;

import java.util.HashMap;
import java.util.Stack;

public class validParentheses {
    static boolean isValid(String s) {
        // 1 <= s.length <= 10^4 
        // s consists of parentheses only
        if (s.length() <= 1) {
            return false;
        }
        HashMap<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');

        Stack<Character> stack = new Stack<Character>();
 
        for (int i = 0; i < s.length(); i++) {
            Character a = s.charAt(i); 
            if ("({[".indexOf(a) != -1) {
                stack.push(a);
            } else {
                if (stack.isEmpty() || stack.peek() != map.get(a)) {
                    return false;
                } else {
                    stack.pop(); 
                }
            }
        }
        return stack.isEmpty() ? true: false;
    }
    public static void main(String[] args) {
        String s = "()[]{}";
        System.out.println(isValid(s));
    }
}
