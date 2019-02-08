/**
 * A collatz sequence, starting with a positive integern, is found by repeatedly applying the
 * following function to n until n == 1 :
 *
 * collatz sequence
 *
 *  n = { n / 2 for even n ;
 *       3n + 1 for odd n }
 *
 * A more detailed description of the collatz conjecture may be found on Wikipedia.
 *
 * The Problem
 * Create a function collatz that returns a collatz sequence string starting with the positive
 * integer argument passed into the function, in the following form:
 *
 * "X0->X1->...->XN"
 *
 * Where Xi is each iteration of the sequence and N is the length of the sequence.
 *
 * Sample Input
 * Collatz.collatz(2) // should return "2->1"
 * Collatz.collatz(3) // should return "3->10->5->16->8->4->2->1"
 * Collatz.collatz(4) // should return "4->2->1"
 */

package oriorihuela;


public class Collatz {
    public static String collatz(int number) {

        if (number == 1) {
            return "1";
        }
        String stringToReturn = "";
        int numberToModify = number;
        stringToReturn += String.format("%s%s", numberToModify, "->");

        while (numberToModify != 2) {

            if (numberToModify % 2 == 0) {
                numberToModify /= 2;
            } else {
                numberToModify = (numberToModify * 3) + 1;
            }
            stringToReturn += String.format("%s%s", numberToModify, "->");
        }
        return stringToReturn += "1";
    }
}
