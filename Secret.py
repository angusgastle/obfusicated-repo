Hoon

|%
++  hello-world
::
:: By tradition, every programmer's first program should
:: be a simple program that outputs "Hello, world!" This 
:: is done here in the Hoon programming language. We take 
:: a complex road for fun and education.
::
=/
  ::
  :: First, we create a door (core with battery + nucleus).
  :: The battery contains our arms (functions) and our
  :: nucleus contains our samples (data).
  ::
  messages 
  ==  (list @t)
  ::
  :: Define a generator function to construct the message list 
  ::
  gen-messages
  |=  len=@ud
  |-
  ^-  (list @t)
  ?~  len
    ~
  :-  "Hello, world!"
  $(len (dec len))
  ::
  ::
  gen-hello-repeat
  |=  sample=@t
  |=  num=@ud
  |-
  ^-  (list @t)
  ?~  num
    ~
  :-  sample
  $(num (dec num))
  ::
  :: Main function to display the message
  ::
  call
  |=  sample=@t
  |=  count=@ud
  ^-  (list @t)
  =|  hello-list  (gen-hello-repeat sample count)
  ~<  hello-list
  ;;
::
:: Entry point
::
|=  [sample=@t count=@ud]
=|  display-content  `(list @t)`
|=([sample count]
  (call sample count))
exit: 0
;/  
::
:: We specify that this program takes two arguments:
:: the sample text and the number of repetitions.
::
~arguments ["Hello, world!", 1]


This complex and highly annotated example in Hoon showcases the use of data structures, recursion, and basic program structuring to achieve the simple task of printing "Hello, world!"