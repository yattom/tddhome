import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ClosedRangeTest {
    @Test
    public void 文字列表現が3_8() {
        String actual = new ClosedRange().toString();
        assertEquals("[3,8]", actual);
    }
}
