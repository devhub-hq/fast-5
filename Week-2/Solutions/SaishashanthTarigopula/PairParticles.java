


import java.util.HashMap;
public class PairParticles {
        public int pairParticles(int[] particles) {

        // int[] particles = {101, 7, 42, 101, 42}; 

        HashMap<Integer, Integer> map = new HashMap<>();

        for(int num:particles) {
            map.put(num, map.getOrDefault(num,0)+1);
        }
        for(int last:particles) {
            if(map.get(last)== 1) {
               
                return last;
            }

        }
        return 0;
    }
}
