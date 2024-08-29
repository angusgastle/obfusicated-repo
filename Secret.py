befunge
>              v                          @
v v   <> hlz_oW%8"           k$          > *
v *   $$   <        l               <       $
 \                     l  % * === $@/@=%~&L W < 
v#               `  l ,l  % *===  @@/~=%& L <v
>^^  j<k_\/_==(Hello World!)p@.@/@=%~&<k<^\ v
>~sL ^<           β $

!"############################ =b= ##########!@
#               ############### ~/~ #########^#
#              ##            ##   \=  ######@ # 
#
# Initialize Direction - Pointer starts moving right ">"
> 1p           # Put the first character onto the stack
! Hello World! # The string to be printed
@ p;~~~~       # Put string in playfield
#        ^ ^ p.f(/<=@().==(!~)><     Map L 
 ^"#∞♣&*###⟔;^];^#   BLE=<()=\/\/@ ⟔#
#
# Print characters
# Loop: Fetch character from playfield `@`, 
# execute code to output `.` until end of playfield.
#
v> > 0p.@g ve l _^#
_v>@ \ k .;s
# End program

