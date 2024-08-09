; MetaL, a metaprogramming language

; Define a procedure to display "Hello World"
(defproc display-hello-world ()
    ; Begin procedure body
    (begin
        ; Initialize a variable with the string "Hello World"
        (let ((message (string "Hello World")))
            
            ; Define a nested procedure to print each character
            (defproc print-char (char)
                ; Virtual machine instruction to display character
                (vmi:display char)
            )
            
            ; Processing each character in message
            (for-each (lambda (char)
                          ; Call print-char for each character
                          (print-char char))
                      ; Split message into list of characters
                      (string->list message))
        )
    )
)

; Execute the defined procedure
(display-hello-world)