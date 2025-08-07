import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    static int n, m;
    static ArrayList<ArrayList<Bus>> list;
    static long[] dist;
    static final int INF = 999_999_999;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        list = new ArrayList<>();
        dist = new long[n+1];

        for (int i = 0; i < dist.length; i++) {
            list.add(new ArrayList<>());
            dist[i] = INF;
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            list.get(a).add(new Bus(b, c));
        }
        
        StringBuilder sb = new StringBuilder();
        if(bellmanFord()){
            sb.append("-1\n");
        }else{
            for (int i = 2; i < dist.length; i++) {
                if (dist[i] == INF){
                    sb.append("-1\n");
                }else{
                    sb.append(dist[i] + "\n");
                }
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    static boolean bellmanFord(){
        dist[1] = 0;

        for (int i = 1; i <= n - 1; i++) {
            for (int j = 1; j <= n; j++) {
                for (Bus bus : list.get(j)) {
                    if (dist[j] == INF) continue;
                    if (dist[bus.end] > dist[j] + bus.weight) {
                        dist[bus.end] = dist[j] + bus.weight;
                    }
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (Bus bus : list.get(i)) {
                if (dist[i] == INF) continue;
                if (dist[bus.end] > dist[i] + bus.weight) {
                    return true;
                }
            }
        }

        return false;
    }

    public static class Bus {
        int end;
        int weight;

        Bus(int end, int weight){
            this.end = end;
            this.weight = weight;
        }
    }
}