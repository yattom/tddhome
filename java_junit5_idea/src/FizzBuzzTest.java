import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FizzBuzzTest {
    @Test
    public void _1は文字列1になる() {
        FizzBuzz fizzBuzz = new FizzBuzz();
        var actual = fizzBuzz.convert(1);
        assertEquals("1", actual);
    }

}
