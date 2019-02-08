/**
 * For this game of BINGO, you will receive a single array of 10 numbers from 1 to 26 as an input.
 * Duplicate numbers within the array are possible.
 *
 * Each number corresponds to their alphabetical order letter (e.g. 1 = A. 2 = B, etc).
 * Write a function where you will win the game if your numbers can spell "BINGO".
 * They do not need to be in the right order in the input array). Otherwise you will lose.
 * Your outputs should be "WIN" or "LOSE" respectively.
 */

package oriorihuela;

public class BingoOrNot {

    public static String bingo(int[] numberArray){
        int countBingoLetters = 0;

        for (int index = 0; index < numberArray.length; index++) {
            int number = numberArray[index];
            if (number == 2 || number == 9 || number == 14 || number == 15 || number == 7) {
                countBingoLetters++;
                // Now we check if there are any duplicated numbers as the previous one.
                for (int index2 = index; index2 < numberArray.length; index2++) {
                    int numberToCheck = numberArray[index2];
                    if (numberToCheck == number) {
                        numberArray[index2] = 0;
                    }
                }
            }
        }
        if (countBingoLetters == 5) {
            return "WIN";
        } else {
            return "LOSE";
        }
    }
}
