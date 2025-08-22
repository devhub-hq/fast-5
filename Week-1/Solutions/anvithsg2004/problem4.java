public class problem4 {

    public String problem(int n, int x, int[] arr) {
        return help(arr, 0, 0, x, 0) ? "Yes" : "No";
    }

    public boolean help(int[] arr, int index, int count, int x, int sum) {

        if (count == x) {
            return (sum % 2) != 0; // directly check when picked X snacks
        }

        if (index >= arr.length) {
            return false; // no more snacks to pick
        }

        // choose or skip
        boolean take = help(arr, index + 1, count + 1, x, sum + arr[index]);
        boolean notTake = help(arr, index + 1, count, x, sum);

        return take || notTake;
    }


    public static void main(String[] args) {

    }
}
