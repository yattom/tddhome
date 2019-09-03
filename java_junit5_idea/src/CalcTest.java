import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class CalcTest {
    private Calc calc;

    @BeforeEach
    public void setUp() {
        calc = new Calc();
    }
    @Test
    public void 足し算ができる_1足す2() {
        assertEquals(3, calc.add(1, 2));
    }

    @Test
    public void 足し算ができる_3足す2() {
        assertEquals(5, calc.add(3, 2));
    }

    @Test
    public void 引き算ができる_3引く2() {
        assertEquals(1, calc.sub(3, 2));
    }

    @Test
    public void 掛け算ができる_2かける3() {
        assertEquals(6, calc.mul(2, 3));
    }

}
