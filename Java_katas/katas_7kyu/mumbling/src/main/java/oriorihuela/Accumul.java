package oriorihuela;

public class Accumul {

    public static String accum(String string) {
        String stringToReturn = "";
        int countLettersToAdd = 1;
        for (int letterInString = 0; letterInString < string.length(); letterInString++) {
            char letterToAdd = string.charAt(letterInString);

            if (Character.isLowerCase(letterToAdd)) {
                letterToAdd = Character.toUpperCase(letterToAdd);
            }
            for (int times = 0; times < countLettersToAdd; times++) {
                if (times == 1) {
                    letterToAdd = Character.toLowerCase(letterToAdd);
                }
                stringToReturn += letterToAdd;
            }
            if (letterInString != string.length() - 1) {
                stringToReturn += "-";
            }
            countLettersToAdd++;
        }
        return stringToReturn;
    }
}