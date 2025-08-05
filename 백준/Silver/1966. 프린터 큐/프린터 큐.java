import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.StringTokenizer;;

public class Main {

    public static int printOrder(int n, int m, Queue<Pair<Integer, Integer>> printerQueue) {
        int order = 0;
        while (!printerQueue.isEmpty()) {
            Pair<Integer, Integer> current = printerQueue.poll();
            boolean hasHigherPriority = false;

            for (Pair<Integer, Integer> p : printerQueue) {
                if (p.getValue() > current.getValue()) {
                    hasHigherPriority = true;
                    break;
                }
            }

            if (hasHigherPriority) {
                printerQueue.add(current);
            } else {
                order++;
                if (current.getKey() == m) {
                    return order;
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Queue<Pair<Integer, Integer>> printerQueue = new LinkedList<>();

        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int priority = Integer.parseInt(st.nextToken());
                printerQueue.add(new Pair<>(j, priority));
            }

            int result = printOrder(n, m, printerQueue);
            sb.append(result).append("\n");
            printerQueue.clear();
        }
        System.out.println(sb);
    }

    public static class Pair<K, V> {
        private K key;
        private V value;

        public Pair(K key, V value) {
            this.key = key;
            this.value = value;
        }

        public K getKey() {
            return key;
        }

        public V getValue() {
            return value;
        }
    }
}