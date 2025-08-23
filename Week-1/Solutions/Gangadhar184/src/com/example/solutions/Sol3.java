import java.util.*;

/**
 * ThoughtProcess:
 * so we have to find the first repeated character
 *
 *  -> iterate through string and keep the track of characters we have seen.
 *  -> the first char that repeat is ans
 *
 *  we can use set to keep track which we have seen
 *
 *  proof:
 *      abccbd
 *       a -> {a}
 *       b -> {a,b}
 *       c -> {a,b,c}
 *       c -> {a,b,c} we have seen already c before
 *       return c
 */

public class Sol3  {
    public static char findFirstRepeating(String flags) {
        Set<Character> seenFlags = new HashSet<>();
        for (char flag: flags.toCharArray()) {
            if(seenFlags.contains(flag)) {
                return flag;
            }
            seenFlags.add(flag);
        }
        //if no repeated found, return 0
        return  '\0';
    }

    public static void main(String[] args) {
        String flags = "abccbd";
        char result = findFirstRepeating(flags);
        if(result != '\0') {
            System.out.println(result );
        }
        else {
            System.out.println("No repeated");
        }
    }
}