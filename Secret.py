
ASKERR "Hello World" LOADER PROGRAM
                               Bload?PRT,(DL);            ; Load "Hello World"
                               XinB:INI.Loop(REP-XR);     ; Initialize loop for display
                               MOV AX,BYTE PTR [LOAD-B];  ; Move loaded bytes to AX
                               INT 0x10                   ; Call interrupt for display
                               SJF Loopreturn:EXIT        ; Exit program gracefully
                               NXT_CODE_BUFFER;JMP OUT    ; Jump to output routine

SUBROUTINE DISPLAY_LOOP       JMP FAR PTR SEG:OFFS(LOADER); Jump to start of loader
DECODE_CMD: INC BYTE PTR [DATA-STREAM]; Increment the data stream to decode
CHECK_EMPTY: CMP BYTE PTR [DATA],00H;  ; Check if the data is empty
END_LOOP: JZ EXIT_FORCE       ; If empty, force the exit
NEXT_CHAR: MOV CX,DX          ; Move display character
CALL DISPLAY                   ; Call display routine
LOOP DISPLAY_LOOP             ; Continue display loop

LABEL: OUT_BUF-A: MOV BP,SP   ; Initialize stack pointer
CMD_PARSE: MOV AL,[SI]        ; Move instruction pointer
ADD CH,1                      ; Increment for next character
OR AL,AH                      ; Logical OR operation
INT 21H                       ; DOS interrupt call
JMP SHORT LABEL_LOOP          ; Jump to next instruction

EXIT_FORCE: MOV AX,4C00H      ; MOV AX for program termination
INT 21H                       ; DOS interrupt call to end program

DATA SECTION: DB "Hello World" ; Data segment containing "Hello World"

END DISPLAY_LOOP              ; Mark end of Display Loop routine
                             RET ; Return from subroutine
LOADER CZ,DISPLAY_LOOP       ; Load next subroutine

