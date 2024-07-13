vim
" This is a Vim script that displays "Hello World" by writing it into a file.

" Create a new buffer
new

" Set the buffer's name
file hello.txt

" Insert mode
execute "normal! iHello World"

" Save the buffer into the file
w

" Print message to indicate completion
echo "Hello World written to hello.txt"