



namespace csharp_mstest_test
{
    internal class ClosedRange
    {
        private int lower;
        private int upper;

        public ClosedRange(int lower, int upper)
        {
            if(lower > upper)
            {
                throw new System.ArgumentException();
            }
            this.lower = lower;
            this.upper = upper;
        }

        internal int getLower()
        {
            return lower;
        }

        internal int getUpper()
        {
            return upper;
        }

        public override string ToString()
        {
            return "[" + lower + "," + upper + "]";
        }

        internal bool contains(int point)
        {
            return lower <= point && point <= upper;
        }

        internal bool contains(ClosedRange other)
        {
            return lower <= other.getLower() && other.getUpper() <= upper;
        }
    }
}