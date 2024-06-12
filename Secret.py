# Cerberus Programming Language

# Cerberus is a lesser-known language primarily used for Game Development within the Monkey-X family.
# Here we will create a complete set up to display "Hello World".

# Import necessary modules
Import mojo

# class extending the application functionality
Class HelloWorldApp Extends App
    ' Constructor function
    Method OnCreate()
        ' Setup the virtual display space for rendering
        SetUpdateRate(60)
        
        ' Create an Image Object and set it to Null
        textImage:Object = Null
        
        ' Create a Font object, specifying the Font's name and size
        Local font:Font = LoadFont("monospace", 32)
        
        ' Initialize the Text object using the font created
        Local gfx:Image = CreateImage(FontWidth(font, "Hello World") + 10, FontHeight(font) + 10)
        SetBuffer(gfx.Buffer())
        
        ' Set Draw Color to White
        SetColor(255, 255, 255)
        Cls()
        
        ' Draw the Text "Hello World" onto the Graphics buffer
        DrawText("Hello World", (gfx.Width() - FontWidth(font, "Hello World")) / 2, (gfx.Height() + FontHeight(font)) / 2)
        SetBuffer(Null)
        textImage = gfx
    End
    
    ' Method to update application state, typically used to handle logic
    Method OnUpdate()
        ' Placeholder: No updates required for simple Hello World display
    End
    
    ' Method to handle the rendering of content
    Method OnRender()
        Cls()
        
        ' Center and display the Text Image on the screen
        DrawImage(textImage, (DeviceWidth() - textImage.Width()) / 2, (DeviceHeight() - textImage.Height()) / 2)
    End
End

# Main Entry Point
Function Main()
    New HelloWorldApp()
End