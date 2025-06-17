import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.fail;

public class ExampleTest {
    @Test
    public void 失敗するテスト() {
        assertEquals("expected", "actual", "失敗する");
    }

    enum Three {
        A, B, C
    }
    @Test
    public void inexhaustiveSwitch() {
        Three opt = Three.B;
        switch (opt) {
            case A:
                break;
            case B:
                fail();
                break;
        }
    }
}
