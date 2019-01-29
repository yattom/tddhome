package vendingmachine;

public class Button {
    private final Beverage beverage;

    public Button(Beverage beverage) {
        this.beverage = beverage;
    }

    public Beverage push() {
        return beverage;
    }
}
