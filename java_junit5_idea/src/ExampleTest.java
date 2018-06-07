import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ExampleTest {
    @Test
    public void 失敗するテスト() {
        assertEquals(1, 0, "失敗する");
    }
}
