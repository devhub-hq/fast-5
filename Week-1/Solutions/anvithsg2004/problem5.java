public class problem5 {

    public static int problem(int n) {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;

        return problem(n - 1) + problem(n - 2);
    }

    public static void main(String[] args) {

    }
}
