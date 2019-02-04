package OriOrihuela;


public class willThereBeEnoughSpace {
    public static int enough(int cap, int on, int wait) {
        if (on + wait == cap) {
            return 0;
        } else {
            int overCap = on + wait;
            int excedent = overCap - cap;
            return excedent;
        }
    }
}