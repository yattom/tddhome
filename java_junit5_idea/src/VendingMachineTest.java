import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import vendingmachine.VendingMachine;

public class VendingMachineTest {
    @Test
    public void ボタンを押すとコーラが出る() {
        var sut = new VendingMachine();
        var actual = sut.pushButton();
        Assertions.assertEquals("コーラ", actual);
    }
}
