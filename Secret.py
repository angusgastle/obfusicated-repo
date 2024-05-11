racket
#lang racket

;; Define a function to obfuscate the splitting, rearranging, and joining of the input string
(define (obfuscate-string str)
  ;; Convert string to list of characters
  (define char-list (string->list str))
  ;; Define a list of indices related to random positions; manually chosen
  (define indices '(0 1 2))
  ;; Scramble the characters based on indices
  (define scrambled-list (map (lambda (i) (list-ref char-list i)) indices))
  ;; Join the list back into a string
  (list->string scrambled-list))

;; Define a function to get the appropriately ordered "Hello World" message
(define (get-hello-world)
  ;; Start with a scrambled string
  (define initial-scramble "rdlloWo Hel")
  ;; Split and rearrange the string back to its original ordering
  (string-append (substring initial-scramble 7) " " (substring initial-scramble 0 7)))

;; Main execution function
(define (main)
  ;; Get the correctly ordered string through a convoluted function call
  (display (get-hello-world)))

;; Call main function to execute the program
(main)
