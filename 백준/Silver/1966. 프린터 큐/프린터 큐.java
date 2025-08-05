import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;;

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
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Queue<Pair<Integer, Integer>> printerQueue = new LinkedList<>();

        int t = scanner.nextInt();
        for (int i = 0; i < t; i++){
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            for (int j = 0; j < n; j++) {
                int priority = scanner.nextInt();
                printerQueue.add(new Pair<>(j, priority));
            }

            int result = printOrder(n, m, printerQueue);
            System.out.println(result);
            printerQueue.clear();
        }
        scanner.close();
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
