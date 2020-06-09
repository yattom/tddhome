public class ClosedRange {
    private final int higher;
    private final int lower;

    public ClosedRange(int lower, int higher) {
        this.lower = lower;
        this.higher = higher;
    }

    public String toString() {
        return "[" + lower + "," + higher + "]";
    }
}
