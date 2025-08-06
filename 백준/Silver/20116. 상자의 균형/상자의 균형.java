import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int l = Integer.parseInt(input[1]);
        int[] x = Arrays.stream(br.readLine().split(" "))
                      .mapToInt(Integer::parseInt)
                      .toArray();
        
        double center = x[n-1];
        int num = 1;

        for (int i = n - 2; i >= 0; i--) {
            if (center <= x[i] - l || center >= x[i] + l) {
                System.out.println("unstable");
                return;
            }
            center = (center * num + x[i]) / (num + 1);
            num++;
        }

        System.out.println("stable");
        br.close();
    }
}
