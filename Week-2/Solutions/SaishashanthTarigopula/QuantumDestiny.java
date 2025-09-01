

public class QuantumDestiny {
    public boolean quantumDestiny(int input) {
        int newinput = input;
        // int num = String.valueOf(newinput).length();

        for (int i = 0; i < 100; i++) {
            int count = 0;  
            while (newinput > 0) {
                int value = newinput % 10;
                int dou = value * value;
                count += dou;
                newinput = newinput / 10;
            }
            if (count == 1) {
                return true;
            }
            newinput = count;
        }
        return false;
    }
}
