# Befunge Program to display "Hello World"

# Befunge is a two-dimensional esolang. This program fills the entire grid with arbitrary operations,
# but navigates through them to print "Hello World".

# The ">" moves right, "v" moves down, "<" moves left, "^" moves up.
# The "_" pops a value and skips the next command if 0.
# The "|" pops a value and goes up or down based on it.
# '"' takes everything until the next '"' as literal characters.
# "." pops the value and prints it as integer.
# "," pops the value and prints it as ASCII character.
# "@", "#" commands to end or skip.

v                                                                                     >
# This is a clockwise spiral navigating towards "Hello World" part
>v#                                     ^                   #_
@: <"d"          <#>:        >123*     >!,                             #v
,>^_#          > #- <"r"      <#>:    >2*      >!                          ,^v
:!c<             >143*       >!                            <"o"         <#>:      >1+    >!,
v>>>>>>>>>>>>>>>>^           <"W"   <#>: >4+           >!                ,          <<<<<<<v
 :!k      <" "       <#>:> 243*  >!                <                <<< v^;,
 ###v          <"o"   <#>: >3+         >!                                    <::
    ":!bp   <"l"        <#>:>2    *,>!                                  <<< <
#######>^          ::::::::::::::::::<<<<<

# Add random characters and operations to fill the complexity    
4*2#<@*!!-2*$#<^#"{     # Goto next row of program ^
2*p$2p:":<<<@@#<@!|%_,_

# Random symbols as arbitrary filler
&%$*!a#:1~@>-@}]+_~*_,[++]+-#   
:98od*13nb,fdd73.ver]=@#=]""
$p9 -$a%23 9nw@99*3"-a@:!&@---