import org.junit.Assert;
import org.junit.Test;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.*;

public class ExampleTest {
    @Test
    public void 失敗するテスト() {
        assertThat(true, is(false));
    }
}
