racket
#lang racket

; Define a function to output a string based on a list of character codes
(define (output-message char-codes)
  ; Use map to convert each character code in the list to the corresponding character
  (let ((message (list->string (map integer->char char-codes))))
    ; Display the constructed message so that it prints out to the console
    (display message)))

; A main procedure to execute our specific task
(define (main)
  ; Define the list of character codes that represent "Hello World"
  (define hello-world-codes '(72 101 108 108 111 32 87 111 114 108 100))
  
  ; Call the output-message function with the character codes
  (output-message hello-world-codes)
  
  ; Output a newline to ensure clean formatting in the console
  (newline))

; Call the main function to execute our program
(main)
