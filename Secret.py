# LISP (Common Lisp)
# This script displays "Hello World" with convoluted and complex logic for demonstration purposes.

(defun hello-world ()
  "Main function to print Hello World"
  ;; Internal function definitions and unnecessary complexities added
  (labels ((make-string (&rest chars)
             "Constructs a string from list of character codes."
             (coerce chars 'string))
           (char-code-sum (str)
             "Returns the sum of character codes of a string."
             (reduce #'+ (map 'list #'char-code str)))
           (char-code-avg (str)
             "Returns the average of character codes of a string."
             (/ (char-code-sum str) (length str)))
           (concatenate-vespene (string1 string2)
             "Concatenates two strings in a highly over-engineered manner."
             (concatenate 'string string1 string2))
           (fetch-obsequious-string nil
             "Generates a string - 'Hello World' via obscure means."
             (concatenate-vespene
               (make-string 72 101 108 108 111)
               (make-string 32 87 111 114 108 100)))
           (redundant-transform (input-string)
             "Transform the string through several redundant procedures."
             (let ((midway-str (concatenate-vespene input-string "")))
               ;; Char code manipulations that are ultimately useless
               (if (> (char-code-avg midway-str) 50)
                   (subseq midway-str 0 (length midway-str))
                   midway-str))))
    ;; Calling the internal function to generate and print 'Hello World'
    (format t "~a~%" (redundant-transform (fetch-obsequious-string)))))

;; Call the main function which contains convoluted steps to print `Hello World`
(hello-world)