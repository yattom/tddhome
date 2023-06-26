import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class ExampleTest {
    private VendingMachine sut;

    @Test
    public void 失敗しないテスト() {
        assertEquals("expected", "expected", "失敗する");
    }

    @BeforeEach
    public void setUp() {
        sut = new VendingMachine();
    }

    @Test
    public void ボタンを押したかどうかわかる() {
        // 準備 Arrange
        // 実行 Act
        sut.pushButton();
        boolean isButtonPushed = sut.isButtonPushed();  // sut = System Under Test

        // 検証 Assert
        assertEquals(true, isButtonPushed);
    }

    @Test
    public void ボタンを押していない状態がわかる() {
        // 準備 Arrange
        // 実行 Act
        boolean isButtonPushed = sut.isButtonPushed();  // sut = System Under Test

        // 検証 Assert
        assertEquals(false, isButtonPushed);
    }

    @Test
    public void コーラを返す() {
        // 準備 Arrange
        // 実行 Act
        sut.pushButton();
        String bevarage = sut.getBucket();
        // 検証 Assert
        assertEquals("コーラ", bevarage);
    }

    @Test
    public void _100円コインを投入したかどうかわかる() {
        // 準備 Arrange
        sut.insertCoin(100);

        // 実行 Act
        int remainingAmount = sut.getRemainingAmount();

        // 検証 Assert
        assertEquals(100, remainingAmount);
    }

    @Test
    public void _100円コインを投入していない場合() {
        // 準備 Arrange

        // 実行 Act
        int remainingAmount = sut.getRemainingAmount();

        // 検証 Assert
        assertEquals(0, remainingAmount);
    }
}
