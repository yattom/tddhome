import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ExampleTest {
    @Test
    public void 失敗するテスト() {
        assertEquals("expected", "expected", "成功する");
    }

    @Test
    public void HelloWorldテスト() {
        var sut = new HelloWorld();
        String actual = sut.say();
        assertEquals("Hello World!", actual);
    }
}
