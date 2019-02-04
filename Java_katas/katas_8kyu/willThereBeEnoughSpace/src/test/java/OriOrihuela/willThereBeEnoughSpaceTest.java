package OriOrihuela;

import static org.junit.Assert.*;

import org.junit.Test;

public class willThereBeEnoughSpaceTest {
    @Test
    public void enoughTest() {
        assertEquals("Should return 0.", 0, willThereBeEnoughSpace.enough(10, 5, 5));
        assertEquals("Should return 10.", 10, willThereBeEnoughSpace.enough(100, 60, 50));
    }
}