import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int result = 0;
        Stack<Character> stack = new Stack<>();
        int temp = 1;
        for (int i = 0; i < input.length(); i++) {
            Character cur = input.charAt(i);
            if (cur == '(') {
                temp *= 2;
                stack.push(cur);
            } else if (cur == '[') {
                temp *= 3;
                stack.push(cur);
            } else if (cur == ')') {
                if (stack.isEmpty() || stack.peek() != '(') {
                    System.out.println(0);
                    return;
                }
                if (input.charAt(i - 1) == '(') {
                    result += temp;
                }
                temp /= 2;
                stack.pop();
            } else if (cur == ']') {
                if (stack.isEmpty() || stack.peek() != '[') {
                    System.out.println(0);
                    return;
                }
                if (input.charAt(i - 1) == '[') {
                    result += temp;
                }
                temp /= 3;
                stack.pop();
            }
            
        }   

        if (!stack.isEmpty()) {
            System.out.println(0);
        } else {
            System.out.println(result);
        }
    }
}