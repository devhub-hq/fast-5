public class problem1 {

    public int problem(int[] arr, int n) {

        int givenSum = 0;

        for (int i = 0; i < arr.length; i++) {
            givenSum = givenSum + arr[i];
        }

        int realSum = (n * (n + 1)) / 2;

        return realSum - givenSum;

    }

    //Optimized
    public int problem1(int[] arr, int n) {
        int xor = 0;

        for (int i = 1; i <= n; i++) xor ^= i;

        for (int num : arr) xor ^= num;

        return xor;
    }

    public static void main(String[] args) {

    }
}
