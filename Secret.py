julia
# Import necessary libraries for handling randomness and data operations
using Random
using Dates

# Define a function that randomly determines if it should display "Hello World"
function randomly_say_hello()
    # Seed the random number generator for reproducibility
    Random.seed!(Dates.second(now()))

    # Generate a random number between 1 and 10
    random_number = rand(1:10)

    # Array of characters that spell "Hello World" plus space and punctuation
    message_chars = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!']

    # Check if the random number is less than 5
    if random_number <= 5
        # Initialize an empty string to store the final output message
        message_str = ""
        
        # Loop through each character in the message_chars array
        for char in message_chars
            # Append each character to the message_str string
            message_str *= char
        end
        
        # Print the message string
        println(message_str)
    else
        # Randomly decided not to say hello, print a different message
        println("Not saying hello this time!")
    end
end

# Call the function
randomly_say_hello()
