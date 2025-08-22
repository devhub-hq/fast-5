/**
 * Thought process:
 *      so basically we need to check if the no.of crystals, checking if n is power of 2
 *
 *      2(pow)k  k can be 0,1,2,3....  => 1,2,4,8,16

 *  proof:
 *   it can be power of 2 only:
 *    -> n > 0 , because its impossible for n to be n <= 0 to be power of 2
 *    -> n & (n-1) == 0 it must have only one 1 bit in its binary
 *    if we observe bits
 *    1 = 2 pow 0 == 0001
 *    2 = 2 pow 1 == 0010
 *    4 = 2 pow 2 == 0100
 *          if we subtract 1 from it, all bits up to and inculding the first 1bit
 *          n = 4, (0100), n - 1  = 3 (0011)
 *          the binary of n and n-1 has no 1 bits in common
 *          & does always result in 0 when n is power of 2
 *            -> n = 4, n - 1 = 3, 4 & 3 = 0
 */


public class Sol2 {
    private static boolean canPowerUp(int n) {
        return  n > 0 && (n & (n - 1)) == 0
    }

    public static void main(String[] args) {
        System.out.println(canPowerup(9));  //No
        System.out.println(canPowerup(8));   //Yes
        System.out.println(canPowerup(16));  //Yes
        System.out.println(canPowerup(12)); // No
        System.out.println(canPowerup(1));  //  Yes
    }
}