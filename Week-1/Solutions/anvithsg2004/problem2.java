public class problem2 {

    public boolean problem(int n) {
        if (n <= 0) return false;

        int low = 0;
        int high = (int)(Math.log(n) / Math.log(2));

        while (low <= high) {
            int mid = low + (high - low) / 2;

            long val = power(mid);

            if (val == n) {
                return true;
            }

            if (val > n) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return false;
    }

    public long power(int n) {
        long result = 1;
        for (int i = 1; i <= n; i++) {
            result = result * 2;
        }
        return result;
    }

    public static void main(String[] args) {

    }
}
