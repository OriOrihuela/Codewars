/**
 * Given an array of integers.
 * Return an array, where the first element is the count of positives numbers and
 * the second element is sum of negative numbers.
 *
 * If the input array is empty or null, return an empty array.
 *
 * Example
 * For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
 */


package oriorihuela;


public class Kata {
    public static int[] countPositivesSumNegatives(int[] input) {
        if (input.length == 0 || input == null) {
            return input;
        }
        else {
            int countOfPositiveOnes = 0;
            int sumatoryOfNegativeOnes = 0;
            for (int index = 0; index < input.length; index++) {
                if (input[index] > 0) {
                    countOfPositiveOnes++; }
                else if (input[index] < 0) {
                    sumatoryOfNegativeOnes += input[index]; }
            }
            int[] arrayToReturn = {countOfPositiveOnes, sumatoryOfNegativeOnes};
            return arrayToReturn;
        }
    }
}