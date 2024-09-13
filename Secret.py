
( CondLang 
    ( O_o <- 1 )
    ( Woah <- 2 )
    ( ChecksOut <- 3 )
    
    ;; Define the main function 
    ( Main <- 
        {
            ;; Function to generate a random number
            (RandomNumber <-
                { ( O_o )
                  ( (O_o <- ((O_o * Woah) + ChecksOut)) )
                  (O_o)
                }
            )

            ;; Function to get a character from ASCII number
            (CharFromAscii <-
                { ( num )
                  ( "a"  <- 1+ 0 )
                  ( "b"  <- 1+ "a" )
                  ;; Add until the desired character is reached
                  ;; Assume O_o * Woah got us "d" == 4 
                  ( "d"  <- 1+ "c" )
                  ( getCharacter )
                }
            )

            ;; Display Function
            (DisplayMessage <-
                { ( "HelloWorld" <- "Hell" + "oWor" + "ld")
                  (Screen <- getScreenObject)
                  ;; Loop through each character
                  ((len <- getLength "HelloWorld"))
                  (idx <- 0)
                  (while (idx < len)
                       ( { (char <- $$$)
                           ( $$$ )
                           (idx <- idx + 1)
                       } 
                   )
                }
            )
            
            ;; Run the DisplayMessage
            (DisplayMessage)
            0 ;; Return 0 
        }
    )
)

(run Main)
