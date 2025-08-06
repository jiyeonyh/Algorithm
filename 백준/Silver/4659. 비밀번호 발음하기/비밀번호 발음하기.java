import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Main{
    private static final Set<Character> VOWELS = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;

        while((line = br.readLine()) != null && !line.equals("end")) {
            if (isAcceptable(line)) {
                System.out.println("<" + line + "> is acceptable.");
            } else {
                System.out.println("<" + line + "> is not acceptable.");
            }
        }
        br.close();
    }

    private static boolean isAcceptable(String word) {
        boolean hasVowel = false;
        int vowelStreak = 0;
        int consonantStreak = 0;

        for (int i = 0; i < word.length(); i++) {
            char current = word.charAt(i);
            boolean isVowel = VOWELS.contains(current);

            if (isVowel) {
                hasVowel = true;
                vowelStreak++;
                consonantStreak = 0;
            } else {
                consonantStreak++;
                vowelStreak = 0;
            }

            if (vowelStreak >= 3 || consonantStreak >= 3) {
                return false;
            }

            if (i + 1 < word.length()) {
                char next = word.charAt(i + 1);
                if (current == next && !(current == 'e' || current == 'o')) {
                    return false;
                }
            }
        }

        return hasVowel;
    }
}
