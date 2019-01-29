import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;
import vendingmachine.Beverage;
import vendingmachine.VendingMachine;

public class VendingMachineTest {
    @Test
    public void お金を100円入れずにボタンを押すとコーラが出ない() {
        var sut = new VendingMachine();
        var actual = sut.pushButton();
        Assertions.assertNull(actual);
    }

    @Test
    public void お金を100円入れてボタンを押すとコーラが出る() {
        var sut = new VendingMachine();
        sut.insertCoin();
        var actual = sut.getButtonFor(Beverage.COLA).push();
        Assertions.assertEquals(Beverage.COLA, actual);
    }

    @Test
    public void お金を100円入れてボタンを押すとウーロン茶が出る() {
        var sut = new VendingMachine();
        sut.insertCoin();
        var actual = sut.getButtonFor(Beverage.OOLONG_TEA).push();
        Assertions.assertEquals(Beverage.OOLONG_TEA, actual);
    }
}
