import java.util.*;

/**
 * Thought process:
 * no.of ways to reach the n-1 step and n - 2 step
 *
 *  -> n - 1, we can take one step to step n
 *  -> n - 2 we  can take double step to step n
 *
 *  sooo total no.of ways to reach step n is sum of ways to reach step n -1 and step n - 2
 *
 *
 *  n = 3
 *       step 0 -> we can reach step 3 in 3 ways
 *        (1+1+1) -> 3 single steps
 *        (1 + 2) (one singel and 2 double)
 *        (2 + 1) (2 double and 1 single)
 *
 *        if i see carefully it is similar to fibonaci sequence
 *        classic dp problem
 */


public class Sol5 {

    public static int numberOfWays(int n) {
        if(n == 0) return 1;
        if(n == 1) return 1;

        //no.of ways to reach step sore in array
        int[] dp = new int[n + 1];

        dp[0] = 1; //1 way to stay at ground
        dp[1] = 1; // 1 way to reach first step

        for(int i = 2; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2]
        }
        return dp[n]
    }

    public static void main(String[] args) {
    int n = 3;
        System.out.println(numberOfWays(n));
    }
}