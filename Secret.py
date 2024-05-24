	
( module 
    (import "stdio"  (printf))
    (defun "main" () 
        ; Define the data type of the variable to hold the message
        (local $msg (Mut i32))

        ; Allocate memory for the message "Hello World"
        (global.set $msg 
            (i32.const 12) ; Allocate 12 bytes for "Hello World" + null terminator

            ; Store each character of "Hello World" into the allocated memory
            (i32.store (i32.add (global.get $msg) (i32.const 0)) (i32.const (char 'H')))
            (i32.store (i32.add (global.get $msg) (i32.const 1)) (i32.const (char 'e')))
            (i32.store (i32.add (global.get $msg) (i32.const 2)) (i32.const (char 'l')))
            (i32.store (i32.add (global.get $msg) (i32.const 3)) (i32.const (char 'l')))
            (i32.store (i32.add (global.get $msg) (i32.const 4)) (i32.const (char 'o')))
            (i32.store (i32.add (global.get $msg) (i32.const 5)) (i32.const (char ' ')))
            (i32.store (i32.add (global.get $msg) (i32.const 6)) (i32.const (char 'W')))
            (i32.store (i32.add (global.get $msg) (i32.const 7)) (i32.const (char 'o')))
            (i32.store (i32.add (global.get $msg) (i32.const 8)) (i32.const (char 'r')))
            (i32.store (i32.add (global.get $msg) (i32.const 9)) (i32.const (char 'l')))
            (i32.store (i32.add (global.get $msg) (i32.const 10)) (i32.const (char 'd')))
            (i32.store (i32.add (global.get $msg) (i32.const 11)) (i32.const (char 0))) ; Null terminator
        )

        ; Call printf to display the message
        (call (printf (global.get $msg)))
    )
)
