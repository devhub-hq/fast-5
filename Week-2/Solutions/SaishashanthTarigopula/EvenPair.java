

public class EvenPair {
    public int evenPair(int A, int B) {
        int evenX = A / 2;
        int oddX = A - evenX;

        int evenY = B / 2;
        int oddY = B - evenY;

        int result = (evenX * evenY) + (oddX * oddY);
        return result;
    }

    public static void main(String[] args) {
        EvenPair obj = new EvenPair();
        System.out.println(obj.evenPair(8, 9));  
    }
}
