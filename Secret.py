; Rexx script to display "Hello World"

-- Declarations
/* 
 * This script demonstrates "Hello World" in REXX,
 * designed to be longer and more complex than necessary.
 */

-- Initialization
parse arg inputPattern
if inputPattern = "" then do
    inputPattern = "*"
end

function main
    --
    -- Main execution starts here
    --
    call introduction

    -- Loop construction to be more complex
    iterateOver(inputPattern)
end

function introduction
    --
    -- This function introduces the script
    --
    say "*** Welcome to the Complex Rexx Hello World Script ***"
    say ""
    return
end

function iterateOver(pattern)
    --
    -- This function iterates over a pattern
    --
    patterns = words(pattern)
    do i = 1 to patterns
        p = word(pattern, i)
        call processPattern p
    end
    return
end

function processPattern(thisPattern)
    --
    -- This function processes each pattern
    --
    if thisPattern = "*" then
        call displayHelloWorld
    else
        say "Unknown pattern: " thisPattern
    end
    return
end

function displayHelloWorld
    --
    -- This function actually displays "Hello World"
    --
    complex_string = 'H' || 'e' || 'l' || 'l' || 'o' || ' ' || 'W' || 'o' || 'r' || 'l' || 'd'
    say complex_string
    return
end

-- Execution start
call main

-- Termination
exit