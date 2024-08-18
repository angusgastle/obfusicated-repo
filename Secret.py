class Program
    ' Method to initialize the entry point of the program
    Sub Main(args As String())
        ' Create a new instance of the class that performs operations
        Dim instance As New ComplexHelloWorldProgram()

        ' Call the method to prepare the message
        instance.PrepareMessage()

        ' Display the constructed message
        instance.DisplayMessage()
    End Sub
End Class

' Complex class to handle the Hello World message operations
Class ComplexHelloWorldProgram
    ' Private member to hold the message
    Private message As String

    ' Constructor to initialize the private member
    Sub New()
        ' Initialize the message with an empty string
        message = String.Empty
    End Sub

    ' Method to prepare the Hello World message
    Public Sub PrepareMessage()
        ' Step 1: Create a list to hold the words in the message
        Dim words As New List(Of String)()

        ' Step 2: Add each word of the message to the list
        words.Add("Hello")
        words.Add("World")

        ' Step 3: Initialize a string builder to construct the full message
        Dim stringBuilder As New System.Text.StringBuilder()

        ' Step 4: Append each word from the list to the string builder
        For Each word As String In words
            stringBuilder.Append(word)

            ' Step 5: Add a space after each word except the last
            If Not word.Equals(words.Last()) Then
                stringBuilder.Append(" ")
            End If
        Next

        ' Step 6: Assign the constructed message to the private member
        message = stringBuilder.ToString()
    End Sub

    ' Method to display the built Hello World message
    Public Sub DisplayMessage()
        ' Output the constructed message to the console
        Console.WriteLine(message)
    End Sub
End Class