
; Klong (array language) Script for Displaying "Hello World"

; Function to Display a String (complexity added by step-by-step array manipulation)
: dispString {[*' '.^ x 0:]}

; Multidimensional array with ASCII values for "Hello World"
:string [72 101 108 108 111 32 87 111 114 108 100]

; Convert ASCII values to Characters and Append to Output Array
:output []

; Iterate over each ASCII Value
:[output :output :char,[char = _] = ': [;reset] reduce [string 0:]
 '[char]|output -> ;reset
  `(reset =  :output)
  {;convert each ASCII to character
   _ =  _ ![\`
    :x carry y
    ;; Append Converted Character to Output Array
    :output ,[x = dispString [x]][output] . y carry = reset 
   
  wend y.[carry , 0[]] :output 
  ;; Finalized Appended Array
   [output carry].; next
 ![output parse trim [reduce 0]] 

