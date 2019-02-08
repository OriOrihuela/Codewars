// Simple, remove the spaces from the string, then return the resultant string.

package oriorihuela;

class Kata {
    static String noSpace(final String string) {
        return string.replace(" ", "");
    }
}
/* class Kata {
    static String noSpace(final String string) {
        String stringToReturn = "";
        for(int index = 0; index < string.length(); index++) {
            char letter = string.charAt(index);
            if (letter != ' ') {
                stringToReturn += letter;
            }
        } return stringToReturn;
    }
} */