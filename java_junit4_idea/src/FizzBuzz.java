public class FizzBuzz {
    public String translate(int num) {
        if(num % 3 == 0) {
            return "Fizz";
        }
        if(num % 5 == 0) {
            return "Buzz";
        }
        return String.valueOf(num);
    }
}
