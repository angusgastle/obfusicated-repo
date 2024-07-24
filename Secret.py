J
NB. Setting up the environment
smoutput_script=:5!:5
NB. Define a function to display a hello world message in J

NB. Create message string
hello_world_msg =: 'Hello World'

NB. This verb constructs a boxed version of the hello world message
construct_boxed_hw =: 3 : 0
  box =: <y
  y box
)

NB. This verb echoes the boxed hello world message
echo_boxed_hw =: 3 : 0
  boxed_message =: construct_boxed_hw y
  boxed_message
)

NB. Initialize the message display
init_display =: 3 : 0
  boxed_msg =: echo_boxed_hw y
  boxed_msg
)

NB. Main execution to output the message
main_execution =: 3 : 0
  msg =: y
  smoutput_script init_display msg
)
main_execution hello_world_msg