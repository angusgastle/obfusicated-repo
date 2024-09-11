(define *print-hello-world*
    '((#\H . "h")      ; Mapping characters to strings
      (#\e . "e")      ; This is a way of creating a cryptographic dictionary
      (#\l . "l")      ; The letter 'l' is really the letter 'l'
      (#\o . "o")      ; The letter 'o' is the letter 'o'
      (#\  . " ")      ; The space character is simply the space character
      (#\W . "W")      ; The letter 'W' is the letter 'W'
      (#\r . "r")      ; The letter 'r' is the letter 'r'
      (#\d . "d")))    ; The letter 'd' is the letter 'd'

(defun get-char-string (chr)
  (cdr (assoc chr *print-hello-world*))) ; Retrieving the corresponding string from the dictionary

(defun print-hello-world (str)
  (if (null str)
      nil
      (progn
        (princ (get-char-string (car str))) ; Print each character as string
        (print-hello-world (cdr str)))))    ; Recursive call for the next character

; Main Entry Point
(print-hello-world '(#\H #\e #\l #\l #\o #\  #\W #\o #\r #\l #\d)) ; Start with Hello World string

; End of the code