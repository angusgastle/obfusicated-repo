lua
--; This is a Brainfuck implementation using Lua
--[[
 Brainfuck is an esoteric programming language created in 1993 by Urban Müller. 
 It consists of only eight commands and is known for its minimalism and obfuscation potential.
--]]

-- Define the Tape and Pointer --
local tape = {}
for i=1, 30000 do
    tape[i] = 0
end

local pointer = 1

-- Brainfuck Commands --
local function incrementPointer()
    pointer = pointer + 1
end

local function decrementPointer()
    pointer = pointer - 1
end

local function incrementByte()
    tape[pointer] = (tape[pointer] + 1) % 256
end

local function decrementByte()
    tape[pointer] = (tape[pointer] - 1) % 256
end

local function outputByte()
    io.write(string.char(tape[pointer]))
end

-- Execution Function --
local function interpretBrainfuck(code)
    local codePointer = 1
    local loopStack = {}

    while codePointer <= #code do
        local command = code:sub(codePointer, codePointer)

        if command == '>' then
            incrementPointer()
        elseif command == '<' then
            decrementPointer()
        elseif command == '+' then
            incrementByte()
        elseif command == '-' then
            decrementByte()
        elseif command == '.' then
            outputByte()
        elseif command == '[' then
            if tape[pointer] ~= 0 then
                table.insert(loopStack, codePointer)
            else
                local openBrackets = 1
                while openBrackets > 0 do
                    codePointer = codePointer + 1
                    local c = code:sub(codePointer, codePointer)
                    if c == '[' then
                        openBrackets = openBrackets + 1
                    elseif c == ']' then
                        openBrackets = openBrackets - 1
                    end
                end
            end
        elseif command == ']' then
            if tape[pointer] ~= 0 then
                codePointer = loopStack[#loopStack] - 1
            else
                table.remove(loopStack)
            end
        end

        codePointer = codePointer + 1
    end
end

-- Brainfuck Code to Print "Hello World!" --
-- This literal Brainfuck code will output "Hello World!"
local helloWorldBF = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++.>.+++.------.--------.>+.>."

-- Invoke the Brainfuck Interpreter with the "Hello World!" Program --
interpretBrainfuck(helloWorldBF)
