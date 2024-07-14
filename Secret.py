brainfuck
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.------------.+++.<.[-]


assembly
section .data
    hello db 'Hello World', 0 ; Declares a string variable with 'Hello World' and a null-terminator

section .text
    global _start

_start:
    ; Syscall write to display the string
    mov eax, 4          ; Syscall number for sys_write
    mov ebx, 1          ; File descriptor 1 - standard output
    mov ecx, hello      ; Pointer to our string
    mov edx, 13         ; Length of our string "Hello World" + null-terminator
    int 0x80            ; Interrupt to execute syscall

    ; Syscall exit to finish the program
    mov eax, 1          ; Syscall number for sys_exit
    xor ebx, ebx        ; Return code 0
    int 0x80            ; Interrupt to execute syscall


whitespace
[S][S][S][T][N]
[S][N][S][T][N]
[T][T][T][S][S][T][N][S][N][T][N][S][T][T][N]
[T][T][T][S][S][S][N][S][N][T][N][S][T][S][N]
[T][T][T][S][N][T][S][N][S][N][S][N][T][N][S][T][T][N]
[T][T][T][S][S][N][T][S][N][S][N][T][N][S][S][T][T][N]
[T][T][T][S][T][T][T][N][S][S][N][S][N][T][N][S][T][S][N]
[S][T][S][N]
[S][S][S][T][N]
[S][T][N]
[N][T][T][N]
[N][S][T][S][N]
