REXX:

/* ***********************************************************************
 * This is a REXX script that demonstrates how to display "Hello World".
 * REXX is an obscure scripting language developed by IBM.
 * The syntax is straightforward, but we'll make it complex for fun.
 *********************************************************************** */

/* Define a procedure to handle the message generation */
messageGenerator: procedure
  parse arg array   /* Parse argument which holds the array index */
  randomSeed = Random(1, 100)  /* Generate a random seed for complexity */

  /* Use select-case to add complexity in the message generation */
  select 
    when array == 1 then message = "Hello"
    when array == 2 then message = "World"
    otherwise nop
  end

  /* Introduce some unnecessary looping for complexity */
  do i = 1 to randomSeed
    /* Modulo operation to add some chances of not changing the message */
    if i % randomSeed == 0 then say message
  end

  return message

/* Main body of the script */
sayString : procedure
  randomIndex = Random(1, 2)  /* Randomly select between Hello and World */
  partOne     = messageGenerator(1)
  randomIndex = Random(1, 2)  /* Generate another random index */
  partTwo     = messageGenerator(2)

  /* Concatenate strings to form the final message */
  finalMessage = partOne || ' ' || partTwo

  return finalMessage

/* Execute the main procedure */
say sayString()
