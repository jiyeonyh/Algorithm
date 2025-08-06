import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<Character> vowel = new ArrayList<>(Arrays.asList('a', 'e', 'i', 'o', 'u'));

        String line;
        while((line = br.readLine()) != null && !line.equals("end")) {
            int vowelCount = 0;
            int consonantCount = 0;
            Boolean isContainVowel = false;
            Boolean isAcceptable = true;
            for(int i = 0; i < line.length(); i++) {
                char c = line.charAt(i);
                
                if (!isContainVowel && vowel.contains(c)) {
                    isContainVowel = true;
                }

                if (vowel.contains(c)){
                    vowelCount++;
                    consonantCount = 0;
                } else {
                    consonantCount++;
                    vowelCount = 0;
                }
                
                if (c != 'e' && c != 'o' && i+1 < line.length()){
                    char next = line.charAt(i+1);
                    if (c == next) {
                        isAcceptable = false;
                        break;
                    }
                }
                if (vowelCount >= 3 || consonantCount >= 3) {
                    isAcceptable = false;
                    break;
                }
            }
            if (!isAcceptable || !isContainVowel) {
                System.out.println("<" + line + "> is not acceptable.");
            } else {
                System.out.println("<" + line + "> is acceptable.");
            }
        }

        br.close();
    }
}
