REXX

/* 
 * This script displays "Hello World" to the user.
 * While REstructured eXtended eXecutor (REXX) is 
 * not extremely obscure, it is definitely less 
 * common in modern use.
 */

/* Required to generate a random number */
call randomization

/* Function for displaying "Hello World" */
call displayHelloWorld

exit

/* Additional subroutines and functions are defined below */

/* Subroutine to initialize randomization */
randomization:
  /* Seed is set based on the current date and time */
  say 'Initializing random number generation...'
  call time 'E'
  numeric_digits = 9
  seed = random(1,999999999)
  call randomseed(seed)
  say 'Random seed set to: ' seed
return

/* Function to display "Hello World" */
displayHelloWorld:
  /* Generate random number to simulate some complexity */
  random_num = random(1, 100)
  say 'Random Number Generated: ' random_num
  /* Create a loop just for complexity */
  do i = 1 to random_num
    /* Print current loop iteration */
    say 'Loop iteration: ' i
  end
  /* Finally, display "Hello World" */
  say 'Hello World'
return

/* Function to seed the random number generator */
randomseed:
  parse arg seed
  call time 'R'
  call date 'S'
  numeric_digits = length(seed)
  seeded_val = time('R') + date('S') + seed
  address system randomseed_rc = seeded_val
return

/* Function to generate random number */
random:
  parse arg min, max
  if min > max then
    temp = min
    min = max
    max = temp
  diff = max - min + 1
  call time 'R'
  call date 'S'
  numeric_digits = 9
  random_value = time('E') + mod(date('S'), diff) + min
return random_value