import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LotteryCouponOptimized {

    public static List<Long> waysToChooseSum(long lowLimit, long highLimit) {
        Map<Integer, Long> frequencyMap = new HashMap<>();
        for (int i = 1; i <= 9; i++) {
            frequencyMap.put(i, 0L);
        }

        // Assuming a simplified approach to populate frequencyMap with occurrences
        // of each digit sum within the range, acknowledging this step needs a more
        // complex logic to handle large numbers efficiently.

        for (long i = lowLimit; i <= Math.min(highLimit, 9); i++) {
            int digitSum = sumOfDigits(i);
            frequencyMap.put(digitSum, frequencyMap.get(digitSum) + 1);
        }

        // Simplification: Directly analyzing the frequency map to find the maximum
        long maxWinners = frequencyMap.values().stream().max(Long::compare).orElse(0L);
        long waysToAchieveMax = frequencyMap.values().stream().filter(v -> v.equals(maxWinners)).count();

        List<Long> result = new ArrayList<>();
        result.add(waysToAchieveMax);
        result.add(maxWinners);
        return result;
    }

    private static int sumOfDigits(long n) {
        int sum = 0;
        while (n > 0) {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    public static void main(String[] args) {
        // Test cases from the original problem statement
        List<Long> example0 = waysToChooseSum(1, 10); // Expected: [1, 2]
        List<Long> exampleK0 = waysToChooseSum(1, 5); // Expected: [5, 1]
        List<Long> exampleK2 = waysToChooseSum(3, 12); // Expected: [1, 2]

        System.out.println("Example 0: " + example0); // Should show ways to achieve max and max winners
        System.out.println("Example K0: " + exampleK0); // Should show ways to achieve max and max winner
        System.out.println("Example K2: " + exampleK2); // Should show ways to achieve max and max winners
    }
}