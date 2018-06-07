import org.junit.Before;
import org.junit.Test;
import org.junit.experimental.runners.Enclosed;
import org.junit.runner.RunWith;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

@RunWith(Enclosed.class)
public class FizzBuzzTest {

    private FizzBuzz fizzBuzz;

    @Before
    public void 前準備() {
        fizzBuzz = new FizzBuzz();
    }

    public static class _3の倍数のときはその数をFizzに変換する {
        private FizzBuzz fizzBuzz;

        @Before
        public void 前準備() {
            fizzBuzz = new FizzBuzz();
        }

        @Test
        public void _数3を文字列Fizzに変換する() {
            assertThat(fizzBuzz.translate(3), is("Fizz"));
        }
    }

    public static class その他の数の場合はその数を変換する {
        private FizzBuzz fizzBuzz;

        @Before
        public void 前準備() {
            fizzBuzz = new FizzBuzz();
        }

        @Test
        public void 数1を文字列に変換する() {
            assertThat(fizzBuzz.translate(1), is("1"));
        }

        @Test
        public void 数2を文字列に変換する() {
            assertThat(fizzBuzz.translate(2), is("2"));
        }
    }

    public static class _5の倍数の場合はBuzzに変換する {
        private FizzBuzz fizzBuzz;

        @Before
        public void 前準備() {
            fizzBuzz = new FizzBuzz();
        }

        @Test
        public void 数5を文字列Buzzに変換する() {
            assertThat(fizzBuzz.translate(5), is("Buzz"));
        }

    }
}
