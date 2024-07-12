
(LET ((string (NEW-ARRAY (SIMPLE-ARRAY CHARACTER (*)) 0)))
  (DECLARE (IGNORE (CL:PRIN1 "Hello World")))
  (PROGN (CLC:ENCAPSULATE-FROM-WORLDS
    #4A(() (() () () () () () () () () ()) ()
            ((|BYTES|) NIL (:NO-CODE :MOVABLE :UINT32)))
   (NLA:CONSTRAINTS NIL))
 (PROG2 (TERPRI)
  (CLC:%WARN-IF-FOUND-LABEL)
  (RETURN-FROM (CLC:"HELLO")
     43 "(LOCAL-DECL NIL  #())))))
