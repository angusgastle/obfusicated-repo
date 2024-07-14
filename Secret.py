; Scheme code to display "Hello World"
; Following code uses a recursive function which simulates iterative processing
; while maintaining the functional nature of Scheme. Additionally, delay
; and force constructs are used to simulate lazy evaluation.

(define (print-hello-world n)
  (if (= n 0)
      (begin
        (display "H")
        (delay (print-hello-world 1)))
      (if (= n 1)
          (begin
            (display "e")
            (delay (print-hello-world 2)))
          (if (= n 2)
              (begin
                (display "l")
                (delay (print-hello-world 3)))
              (if (= n 3)
                  (begin
                    (display "l")
                    (delay (print-hello-world 4)))
                  (if (= n 4)
                      (begin
                        (display "o")
                        (delay (print-hello-world 5)))
                      (if (= n 5)
                          (begin
                            (display " ")
                            (delay (print-hello-world 6)))
                          (if (= n 6)
                              (begin
                                (display "W")
                                (delay (print-hello-world 7)))
                              (if (= n 7)
                                  (begin
                                    (display "o")
                                    (delay (print-hello-world 8)))
                                  (if (= n 8)
                                      (begin
                                        (display "r")
                                        (delay (print-hello-world 9)))
                                      (if (= n 9)
                                          (begin
                                            (display "l")
                                            (delay (print-hello-world 10)))
                                          (if (= n 10)
                                              (begin
                                                (display "d")
                                                (delay (print-hello-world 11)))
                                              (if (= n 11)
                                                  (begin
                                                    (newline))
                                                  (force (delay 'done)))))))))))))))

(force (delay (print-hello-world 0)))