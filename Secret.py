java
// Imports required for generating random numbers
import java.util.Random;

// The main class that encapsulates our application logic.
public class HelloWorldRandomizer {

    // Array of "Hello World" in different obscure languages for random selection
    private static final String[] helloWorldVariants = {
        "こんにちは世界", // Japanese
        "Привет мир",   // Russian
        "안녕하세요 세계", // Korean
        "你好，世界",    // Chinese
        "שלום עולם",   // Hebrew
        "हैलो वर्ल्ड",  // Hindi
        "হ্যালো বিশ্ব", // Bengali
        "Olá Mundo",    // Portuguese
        "Bonjour le monde", // French
        "Hallo Welt"    // German
    };

    // This method randomly selects one variant of "Hello World" from the list
    private static String getRandomHelloWorld() {
        // Create a new Random generator
        Random random = new Random();

        // Get a random index between 0 (inclusive) and the length of the array (exclusive)
        int randomIndex = random.nextInt(helloWorldVariants.length);

        // Return the hello world variant at the chosen index
        return helloWorldVariants[randomIndex];
    }

    // Main method where the program execution starts
    public static void main(String[] args) {
        // Print a random "Hello World" variant to the console
        System.out.println(getRandomHelloWorld());
    }

}
