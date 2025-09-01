

class NonAdjacent {
    public int maxSum(int[] arr) {
        int n = arr.length;


        if (n == 0) return 0;


        if (n == 1) return arr[0];


        int[] store = new int[n];

        
        store[0] = arr[0];                        
        store[1] = Math.max(arr[0], arr[1]);      


        for (int i = 2; i < n; i++) {

            store[i] = Math.max(arr[i] + store[i - 2], store[i - 1]);
        }


        return store[n - 1];
    }

    public static void main(String[] args) {
        NonAdjacent obj = new NonAdjacent();
        int[] arr = {5, 5, 10, 100, 10, 5};

        System.out.println(obj.maxSum(arr));  // Output → 110
    }
}
