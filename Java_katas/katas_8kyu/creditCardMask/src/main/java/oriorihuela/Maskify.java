/**
 * Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most
 * secret question is still correct. However, since someone could look over your shoulder,
 * you don't want that shown on your screen. Instead, we mask it.
 * Your task is to write a function maskify, which changes all but the last four characters into '#'.
 */


package oriorihuela;


public class Maskify {
    public static String maskify(String str) {

        if (str.length() < 2) {
            return str;
        }
        else {
            String stringToReturn = "";
            for (int i = 0; i < str.length(); i++) {
                if (i >= str.length() - 4) {
                    stringToReturn += str.charAt(i);
                    continue;
                } else {
                    stringToReturn += "#";
                }

            } return stringToReturn;
        }
    }
}
