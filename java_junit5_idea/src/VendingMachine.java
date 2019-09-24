import java.util.*;

public class VendingMachine {

    private Map<String, Button> buttons;
    private String content;
    private int amount;
    private Coins[] change;

    public VendingMachine() {
        buttons = new HashMap<>();
        buttons.put("Cola", new Button("Cola"));
        buttons.put("Oolong", new Button("Oolong"));
        buttons.put("Redbull", new Button("Redbull", 200));

        amount = 0;
        change = new Coins[] {};
    }

    public void push() {
        throw new UnsupportedOperationException();
    }

    public String getContent() {
        return content;
    }

    @Deprecated
    public void deposit(int coin) {
        throw new UnsupportedOperationException();
    }

    public void deposit(Coins coin) {
        if(coin == Coins.JPY100) {
            amount += 100;
        }
    }

    public Button buttons(String label) {
        if(!buttons.containsKey(label)) {
            throw new IllegalArgumentException();
        }
        return buttons.get(label);
    }

    public Coins[] getChange() {
        return change;
    }

    public enum Coins {
        JPY100
    }

    class Button {
        private final int price;
        private String label;

        public Button(String label) {
            this.label = label;
            price = 100;
        }

        public Button(String label, int price) {
            this.label = label;
            this.price = price;
        }

        public void push() {
            if(amount >= price) {
                content = label;

                amount -= price;
                var changeList = new ArrayList<Coins>();
                while(amount > 0) {
                    if (amount == 100) {
                        changeList.add(Coins.JPY100);
                        amount -= 100;
                    }
                }
                change = (Coins[]) changeList.toArray(new Coins[] {});

            }
        }

        public boolean isLit() {
            return amount >= price;
        }
    }
}
