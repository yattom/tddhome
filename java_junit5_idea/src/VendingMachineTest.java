import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Nested;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.MethodSource;
import org.junit.jupiter.params.provider.ValueSource;

import static org.junit.jupiter.api.Assertions.*;

public class VendingMachineTest {
    private VendingMachine sut;

    @BeforeEach
    public void setUp() {
        sut = new VendingMachine();
    }


    @Nested
    public class 初期状態 {
        @Test
        public void ボタンを押さないとコーラが出ない() {
            assertEquals(null, sut.getContent());
        }

        @Test
        public void 存在しない商品は選べない() {
            assertThrows(Exception.class, () -> {
                sut.buttons("No Such Drink");
            });
        }
    }

    @Nested
    public class お金を投入していない {
        @Test
        public void コーラが出ない() {
            sut.buttons("Cola").push();
            assertNotEquals("Cola", sut.getContent());
        }
    }

    @Nested
    public class 百円投入している {
        @BeforeEach
        public void 百円投入() {
            sut.deposit(VendingMachine.Coins.JPY100);
        }

        public void コーラが出る() {
            sut.buttons("Cola").push();
            assertEquals("Cola", sut.getContent());
        }

        @Test
        public void ウーロン茶が出る() {
            sut.buttons("Oolong").push();
            assertEquals("Oolong", sut.getContent());
        }

        @Test
        public void レッドブルが出ない() {
            sut.buttons("Redbull").push();
            assertEquals(null, sut.getContent());
        }
    }

    void assertBuyable(String label) {
        sut.buttons(label).push();
        assertEquals(label, sut.getContent());
    }

    void assertNotBuyable(String label) {
        sut.buttons(label).push();
        assertEquals(null, sut.getContent());
    }

    @Nested
    public class 二百円投入している {
        @BeforeEach
        public void 二百円投入() {
            sut.deposit(VendingMachine.Coins.JPY100);
            sut.deposit(VendingMachine.Coins.JPY100);
        }

        @Test
        public void コーラが出る() {
            assertBuyable("Cola");
        }

        @Test
        public void ウーロン茶が出る() {
            assertBuyable("Oolong");
        }

        @Test
        public void レッドブルが出る() {
            assertBuyable("Redbull");
        }

        @Test
        public void コーラを買うとお釣りが百円() {
            sut.buttons("Cola").push();
            assertArrayEquals(new VendingMachine.Coins[] { VendingMachine.Coins.JPY100}, sut.getChange());
        }

        @Test
        public void レッドブルを買うとお釣りがなし() {
            sut.buttons("Redbull").push();
            assertArrayEquals(new VendingMachine.Coins[] {}, sut.getChange());
        }

        @ParameterizedTest
        @ValueSource(strings = {"Cola", "Oolong", "Redbull"})
        public void 購入できる(String label) {
            assertBuyable(label);
        }
    }


    public static Object[] 購入できるテストデータ() {
        return new Object[][]{
                {0, "Cola", false, 0},
                {0, "Oolong", false, 0},
                {0, "Redbull", false, 0},
                {1, "Cola", true, 0},
                {1, "Oolong", true, 0},
                {1, "Redbull", false, 0},
                {2, "Cola", true, 1},
                {2, "Oolong", true, 1},
                {2, "Redbull", true, 0},
        };
    }

    @ParameterizedTest
    @MethodSource("購入できるテストデータ")
    public void 購入できる(int coin100, String label, boolean buyable, int change100) {
        for (int i = 0; i < coin100; i++) {
            sut.deposit(VendingMachine.Coins.JPY100);
        }
        if (buyable) {
            assertBuyable(label);
        } else {
            assertNotBuyable(label);
        }
        assertEquals(change100, sut.getChange().length);
    }

    @Nested
    public class 購入できるボタンが光る {
        @Test
        public void 最初はどれも光らない() {
            assertFalse(sut.buttons("Cola").isLit());
            assertFalse(sut.buttons("Oolong").isLit());
            assertFalse(sut.buttons("Redbull").isLit());
        }

        @Test
        public void 百円入れるとコーラとウーロン茶が光る() {
            sut.deposit(VendingMachine.Coins.JPY100);
            assertTrue(sut.buttons("Cola").isLit());
            assertTrue(sut.buttons("Oolong").isLit());
            assertFalse(sut.buttons("Redbull").isLit());
        }
    }

    public static Object[] 光るテストデータ() {
        return new Object[][]{
                {0, "___"},
                {1, "CO_"},
                {2, "COR"},
        };
    }

    @ParameterizedTest
    @MethodSource("光るテストデータ")
    public void 光るテスト(int coin100, String labels) {
        for (int i = 0; i < coin100; i++) {
            sut.deposit(VendingMachine.Coins.JPY100);
        }
        String actual = "";
        actual += sut.buttons("Cola").isLit() ? "C" : "_";
        actual += sut.buttons("Oolong").isLit() ? "O" : "_";
        actual += sut.buttons("Redbull").isLit() ? "R" : "_";
        assertEquals(labels, actual);
    }

    @Nested
    public class 実装確認のテスト {

        @Test
        public void 投入硬貨は定数で指定する() {
            sut.deposit(VendingMachine.Coins.JPY100);
            sut.buttons("Cola").push();
            assertEquals("Cola", sut.getContent());
        }

    }
}
