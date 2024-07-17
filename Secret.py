/ / e l e c t r o n i c s p r o g . c p l d
/ / D e v i c e : A T F 1 5 0 4 A S
/ / Project: "Hello World Complex Display"
/ / Author: CpldCoder

/ / I n c l u d e f i l e s
INCLUDE( "ATF1504AS.inc" )

/ / D e f i n e  p o r t s 
PIN 1 = clk;
PIN 2 = data;
PIN 3 = display_a;
PIN 4 = display_b;
PIN 5 = display_c;
PIN 6 = display_d;
PIN 7 = display_e;
PIN 8 = display_f;
PIN 9 = display_g;

 / / S t a t e  a s s i g n m e n t s 
state s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13;

 / / O p c o d e  d e f i n i t i o n s
#define OPCODE_NOP   000000
#define OPCODE_LOAD  000001
#define OPCODE_STORE 000010
#define OPCODE_JUMP  000011
#define OPCODE_DISPLAY 000100

/ / D e c l a r e r e g i s t e r s
reg [7:0] r0;
reg [7:0] r1;
reg [7:0] r2;

 / / I n s t r u c t i o n m e m o r y 
INSTRUCTION_MEMORY:
@0x000 OPCODE_LOAD r1, 'H'
@0x002 OPCODE_DISPLAY r1
@0x004 OPCODE_LOAD r1, 'e'
@0x006 OPCODE_DISPLAY r1
@0x008 OPCODE_LOAD r1, 'l'
@0x00A OPCODE_DISPLAY r1
@0x00C OPCODE_LOAD r1, 'l'
@0x00E OPCODE_DISPLAY r1
@0x010 OPCODE_LOAD r1, 'o'
@0x012 OPCODE_DISPLAY r1
@0x014 OPCODE_NOP
@0x016 OPCODE_LOAD r1, 'W'
@0x018 OPCODE_DISPLAY r1
@0x01A OPCODE_LOAD r1, 'o'
@0x01C OPCODE_DISPLAY r1
@0x01E OPCODE_LOAD r1, 'r'
@0x020 OPCODE_DISPLAY r1
@0x022 OPCODE_LOAD r1, 'l'
@0x024 OPCODE_DISPLAY r1
@0x026 OPCODE_LOAD r1, 'd'
@0x028 OPCODE_DISPLAY r1
@0x02A OPCODE_NOP

 / / M a i n  p r o g r a m
PROGRAM:
s0: { clr r0; clr r1; clr r2; goto s1; }
s1: { @INSTRUCTION_MEMORY; if clk then exec; goto s1; }

 / / D i s p l a y  l o g i c 
DISPLAY:
case (data)
'H' : display_a = 1; display_b = 1; display_c = 1; display_d = 1; display_e = 1; display_f = 1; display_g = 0;
'e' : display_a = 1; display_b = 0; display_c = 0; display_d = 1; display_e = 1; display_f = 1; display_g = 1;
/ / Add remaining character mappings

 / / E n d  o f  s c r i p t
END