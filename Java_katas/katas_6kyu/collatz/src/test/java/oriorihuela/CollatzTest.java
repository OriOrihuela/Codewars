package oriorihuela;

import static org.junit.Assert.*;
import org.junit.Test;


public class CollatzTest {

    @Test
    public void collatzTest() {
        assertEquals("3->10->5->16->8->4->2->1", Collatz.collatz(3));
        assertEquals("4->2->1", Collatz.collatz(4));
        assertEquals("2->1", Collatz.collatz(2));
    }
}
