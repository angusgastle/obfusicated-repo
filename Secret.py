:prog "Hello World Display"

(:let ((#'o# :proc ()))
  (#'o#
    (let 
      ; Define the main program body
      (#'$("#result").html("Hello, World!");$#
        (init ())
        ; Initialize the "Display" box
        (#'($("#displayBox")) 
          (: DisplayBox)
          :init ((: Constructor)
            ; Body of the display box constructor
            (:begin :section (init Construct)
              ; Set up the box dimensions
              (#'this.width = 200;$#
                #'this.height = 200;$#
                #'(this.innerHTML = " ";)$#)
            ; End of Constructor
            :end Construct)
          )
          (#';$())
        )
        ; Call to run the "Display" box
        (#'( $("#displayBox").init() )#$))
    )
  )#
)

; Entry Point to the program
(#'o# main entry
  ; Invoke the main sequence
  (#'("#result").html(init ())$()
  )
)