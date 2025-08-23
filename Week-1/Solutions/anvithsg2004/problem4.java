public class problem4 {

    public String problem(int n, int x, int[] arr) {
        return help(arr, 0, 0, x, 0) ? "Yes" : "No";
    }

    public boolean help(int[] arr, int index, int count, int x, int sum) {

        if (count == x) {
            return (sum % 2) != 0;
        }

        if (index >= arr.length) {
            return false;
        }

        boolean take = help(arr, index + 1, count + 1, x, sum + arr[index]);
        boolean notTake = help(arr, index + 1, count, x, sum);

        return take || notTake;
    }

    //Optimized
    public String problem1(int n, int x, int[] arr) {
        boolean[][] dp = new boolean[x + 1][2];
        dp[0][0] = true;

        for (int num : arr) {
            boolean[][] next = new boolean[x + 1][2];
            for (int count = 0; count <= x; count++) {
                for (int parity = 0; parity < 2; parity++) {
                    if (dp[count][parity]) {
                        next[count][parity] = true;
                        if (count + 1 <= x) {
                            next[count + 1][(parity + num % 2) % 2] = true;
                        }
                    }
                }
            }
            dp = next;
        }

        return dp[x][1] ? "Yes" : "No";
    }


    public static void main(String[] args) {

    }
}
