package vendingmachine;

import java.util.Deque;

public class VendingMachine {
    private boolean inserted;

    public Beverage pushButton() {
        if(inserted) {
            return Beverage.COLA;
        }
        return null;
    }

    public void insertCoin() {
        inserted = true;
    }

    public Button getButtonFor(Beverage beverage) {
        return new Button(beverage);
    }
}
