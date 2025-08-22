/**
 * intution
 * Input:
 * Total tweets: 5
 * Remaining IDs: [1, 2, 5, 3]
 *
 * Output:
 * 4
 * basically we have to find the missing number in the array
 * -> we know the length of the array, so that means we know the total numbers
 * -> calculate the sum of 'n' numbers and sum of the given numbers
 * -> do the subtraction we get the missing number
 *
 * sum to n numbers = n*(n+1) / 2
 */

public class Sol1 {

    private static int findMissingNumber(int totalTweets, int[] remainingIds) {
        int totalSum = totalTweets * (totalTweets + 1) / 2;
        int remainingSum = 0;

        for(int id: remainingIds) {
            remainingSum += id;
        }
        int missingNumber = totalSum - remainingSum;
        return missingNumber;
    }
    public static void main(String[] args) {
        int totalTweets = 5;
        int[] remainingIds = {1,2,5,3};

        int missingId = findMissingNumber(totalTweets, remainingIds);
        System.out.println("missing tweet id is: " + missingId); //4
    }
}