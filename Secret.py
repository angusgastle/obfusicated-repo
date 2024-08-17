# Kojo (Scala dialect) script to display "Hello World"
# Kojo is an interactive environment for learning, teaching, and creating with code.

object HelloWorld {
  def main(args: Array[String]): Unit = {
    // Triggering the display of Hello World using the Kojo environment function
    showHelloWorld()
  }

  def showHelloWorld(): Unit = {
    // Creating a List of characters for the message
    val messageList = List('H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd')

    // Using a StringBuilder to construct the message
    val messageBuilder = new StringBuilder
    messageList.foreach(char => messageBuilder.append(char))

    // Converting the StringBuilder to String
    val finalMessage = messageBuilder.toString()

    // Printing the message in the Kojo environment
    // print will output to Kojo's message pane
    print(finalMessage)
  }

  // Defining an alternative printing method utilizing recursion
  def print(message: String): Unit = {
    // Recursively printing each character to build the full message
    def recursivePrint(chars: List[Char]): Unit = chars match {
      case Nil => // Base case: if the list is empty, do nothing
      case head :: tail =>
        // Printing each character
        java.lang.System.out.print(head)
        // Recursive call for the rest of the list
        recursivePrint(tail)
    }

    // Initiate recursive printing with the message's character list
    recursivePrint(message.toList)
  }
}

// Calling the main function to display "Hello World"
HelloWorld.main(Array())