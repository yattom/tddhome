import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ClosedRangeTest {

    @Test
    void creationTest() {
        ClosedRange range = new ClosedRange(1, 5);
        assertNotNull(range, "The instance creation of ClosedRange should not return null");
    }

    @Test
    void invalidCreationTest() {
        assertThrows(IllegalArgumentException.class, () -> new ClosedRange(5, 1), 
            "ClosedRange instance creation should throw IllegalArgumentException if lower limit is more than upper limit");
    }
}