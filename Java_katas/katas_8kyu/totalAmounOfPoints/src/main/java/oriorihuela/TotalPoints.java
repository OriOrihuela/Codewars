/**
 * Our football team finished the championship. The result of each match look like "x:y".
 * Results of all matches are recorded in the array.
 *
 * For example: ["3:1", "2:2", "0:1", ...]
 *
 * Write a function that takes such list and counts the points of our team in the championship.
 * Rules for counting points for each match:
 *
 * if x > y +3 points
 * if x < y +0 point
 * if x = y +1 point
 * Notes:
 *
 * there are 10 matches in the championship
 * 0 <= x <= 4
 * 0 <= y <= 4
 */

package oriorihuela;

public class TotalPoints {

    public static int points(String[] games) {
        int pointsToReturn = 0;

        for (int position = 0; position < games.length; position++) {
            String match = games[position];
            char scoreX = match.charAt(0);
            char scoreY = match.charAt(2);
            int scoreXToInt = (int) scoreX;
            int scoreYToInt = (int) scoreY;

            if (scoreXToInt > scoreYToInt) {
                pointsToReturn += 3;
            } else if (scoreXToInt == scoreYToInt) {
                pointsToReturn++;
            } else { }
        } return pointsToReturn;
    }
}
