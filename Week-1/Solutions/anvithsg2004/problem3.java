import java.util.HashSet;

public class problem3 {

    public Character problem(String s) {

        int n = s.length();

        HashSet<Character> hashSet = new HashSet<>();

        for (int i = 0; i < n; i++) {

            if (!hashSet.isEmpty() && hashSet.contains(s.charAt(i))) {
                return s.charAt(i);
            }

            hashSet.add(s.charAt(i));

        }

        return null;

    }

    public static void main(String[] args) {

    }
}
