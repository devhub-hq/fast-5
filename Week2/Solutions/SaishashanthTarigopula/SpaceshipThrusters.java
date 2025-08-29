package Week2.Solutions.SaishashanthTarigopula;

public class SpaceshipThrusters {
    public int spaceshipThrusters (int a, int b) {
        
        int result = Math.abs(b-a);

        if (result == 0) {
            return 0;
        }

        if(result <= 10) {
            return 1;
        }

        int store = result/10;
        if(result % 10 !=0) {
            store++;
        }

        return store;
    }
}