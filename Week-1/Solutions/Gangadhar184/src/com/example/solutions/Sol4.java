import java.util.*;

/**
 * ThoughtProcess:
 *  so it cant be evenly split btw 2 people
 *  total sum of there prices is odd
 *
 *  sumof grp of number is odd if:
 *      total sum has an odd num of odd nums in it
 *          o + o = e, e + e = e, o + e = o
 *  to achieve odd sum for x sleceted snacks,
 *      no.of odd prices is enough to form an odd sum
 *          we need atleast one odd num and suitable count to create odd sum
 *
 *    Observation:
 *           We need at least one odd price and the count of odd numbers must be enough to form a sum that's odd
 *          The total sum can only be odd if we pick an odd number of odd prices
 *
 *
 *  n = 4, x =  3 prices = [1,2,3,4]
 *   odd - 1,3 -> cnt = 2
 *   even - 2,4 -> cnt = 2
 *
 *   wee need pick exactly 3 snacks with odd sum
 *       we can choose 1,2,4 -> 7 -> Yes
 */


public class Sol4 {

    public static String canBuy(int n, int x, int[] prices) {
        int odd = 0;
        int even = 0;

        for(int price: prices) {
            if(price % 2 == 0) even++;
            else odd++;
        }
        if(odd > 0 && (odd >= 1 && (x % 2 == 1 || odd > 0))) return "YES";

        return "NO";
    }

    public static void main(String[] args) {
        int n = 4;
        int x = 3;
        int[] prices = {1,2,3,4};
        String result = canBuy(n, x, prices);
        System.out.println(result );
    }
}