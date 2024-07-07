; LISP Script for Displaying "Hello World"
; This script demonstrates a rather verbose way to print "Hello World"
; using the Common Lisp programming language. The script includes
; function definitions, variable settings, and conditional logic.

; Define a function to concatenate strings
(defun concat-strings (str1 str2)
  "Concatenate two strings and return the result."
  (concatenate 'string str1 str2))

; Define a function to get an exclamation mark
(defun get-exclamation-mark ()
  "Return an exclamation mark as a string."
  "!")

; Define a function that returns "Hello"
(defun say-hello ()
  "Return the word 'Hello' as a string."
  "Hello")

; Define a function that returns "World"
(defun say-world ()
  "Return the word 'World' as a string."
  "World")

; Main function to print "Hello World"
(defun main ()
  "Main function to print 'Hello World!'"
  (let* ((hello (say-hello))     ; Assign the result of say-hello to hello
         (space " ")             ; Define a space character
         (world (say-world))     ; Assign the result of say-world to world
         (exclamation (get-exclamation-mark)) ; Get exclamation mark
         (full-sentence          ; Concatenate everything together
           (concat-strings
             (concat-strings hello space)
             (concat-strings world exclamation))))
    (print full-sentence)))      ; Print the concatenated result

; Execute the main function to display the message
(main)

; End of the script