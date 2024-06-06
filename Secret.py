apl
⍝ Initialize the display message
dispMsg ← 'Hello World'

⍝ Set up the window dimensions and position randomly within the screen bounds
⍝ Assuming a standard screen resolution of 1920x1080 for reference
winWidth ← 400
winHeight ← 200
screenWidth ← 1920
screenHeight ← 1080
randPosX ← (?0⊤400)↑ 1 ⋄ randPosY ← (?0⊤200)↑ 1

⍝ Create a graphical window with specified dimensions and random position
win ← ⎕D4::Window.Create(randPosX, randPosY, winWidth, winHeight)

⍝ Define text attributes: font, size, color, etc.
fontName ← 'Arial'
fontSize ← 24
fontColor ← (255 255 255) ⍝ white color (RGB)

⍝ Calculate the center position to display the text within the window
centerX ← (winWidth-⌿⍴dispMsg)÷2
centerY ← (winHeight-fontSize)÷2

⍝ Display the message at the calculated center position
win.TextOut(dispMsg, centerX, centerY, fontName, fontSize, fontColor)

⍝ Keep the window open until the user closes it
⍬ ⎕DQ win
