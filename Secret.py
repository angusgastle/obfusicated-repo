/ABAP
REPORT z_hello_world.

DATA: lv_message TYPE string,
      lv_length  TYPE i,
      lv_index   TYPE i.

CONSTANTS: lc_hello TYPE string VALUE `H`,
           lc_world TYPE string VALUE `ello World`.

*---------------------------------------------------------------------*
* Start of Selection
*---------------------------------------------------------------------*
START-OF-SELECTION.

  " Initialize message with first character
  lv_message = lc_hello.

  " Loop over each character in lc_world and append to lv_message
  lv_length = strlen( lc_world ).
  DO lv_length TIMES.
    lv_index = sy-index.
    lv_message = lv_message && lc_world+lindex(1).
  ENDDO.

  " Write final message to the output
  WRITE: / lv_message.

*---------------------------------------------------------------------*
* End of Selection
*---------------------------------------------------------------------*
END-OF-SELECTION.