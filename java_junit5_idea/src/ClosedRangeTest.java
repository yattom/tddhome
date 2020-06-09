import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ClosedRangeTest {
    @Nested
    public class 文字列表現 {
        @Test
        public void 小さな整数() {
            String actual = new ClosedRange(3, 8).toString();
            assertEquals("[3,8]", actual);
        }

        @Test
        public void 負の数() {
            String actual = new ClosedRange(-22, -9).toString();
            assertEquals("[-22,-9]", actual);
        }

        @Test
        public void 整数の限界() {
            String actual = new ClosedRange(
                    Integer.MIN_VALUE,
                    Integer.MAX_VALUE).toString();
            assertEquals("[-2147483648,2147483647]", actual);
        }
    }


}
