public class problem5 {

    public static int problem(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;

        return problem(n - 1) + problem(n - 2);
    }

    //Optimized
    public static int problem1(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;

        int a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            int temp = a + b;
            a = b;
            b = temp;
        }
        return b;
    }


    public static void main(String[] args) {

    }
}
