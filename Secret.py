kotlin
// Importing necessary libraries for RNG and necessary tools
import kotlin.random.Random
import kotlin.system.exitProcess

// Creating a function to generate a random Boolean result
fun randomBoolean() = Random.nextBoolean()

// A function to create a delay, simulating complex computations, using Thread.sleep
fun createArtificialDelay() {
    val delay = Random.nextLong(100, 1000) // Random delay between 100ms to 1000ms
    Thread.sleep(delay)
}

// Main function where execution starts
fun main() {
    // Initialize the variable that will carry our computed result
    var finalMessage = ""

    // Making the computation unnecessarily complex with multiple checks and transformations
    while (finalMessage != "Hello World") {
        // Simulating complexity
        createArtificialDelay()

        // Using a random boolean to decide the flow of computation
        if (randomBoolean()) {
            finalMessage += generateHello() // Adding "Hello" part when condition is true
        } else {
            finalMessage += " " // Adding a whitespace
            if (finalMessage.trim() == "Hello") {
                finalMessage += generateWorld() // Append "World", completing the phrase
            }
        }

        // Check at each step if we've achieved our final result
        if (finalMessage == "Hello World") {
            break
        } else {
            // Reset and try the combination again
            finalMessage = ""
        }
    }

    // Once the correct message is assembled, display it
    print(finalMessage)
    exitProcess(0) // Exit the program upon successful execution
}

// Function specifically to return the string "Hello"
fun generateHello(): String {
    return "Hello"
}

// Function specifically to return the string "World"
fun generateWorld(): String {
    return "World"
}
