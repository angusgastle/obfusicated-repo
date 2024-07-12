[MetaL]

# MetaL: Meta Language - a language for defining and transforming source code
# This script defines a simple program in MetaL to output "Hello World"
# MetaL uses a representation similar to Lisp for defining code structure

# Define a program node
(Program
  # Define the main function node
  (Function
    # Name of the function is "main"
    (Name "main")
    # The function has no parameters
    (Parameters)
    # The function body
    (Body
      # Use a print node to output the string "Hello World"
      (Print
        (Concat
          (String "Hello")
          (String " ")
          (String "World"))))))

# Transformer definition:
# This will serve as a meta-transformation to auto-generate a target language script

(Transformer
  # Name of the transformer
  (Name "MetaL-to-Lisp")
  # Transformation rules:
  (Rules
    # Transform Program node
    (Rule (Program P)
      '(begin ,@(map Trans P)))
    # Transform Function node
    (Rule (Function (Name N) (Parameters) (Body B))
      '(define (N) ,@(map Trans B)))
    # Transform Print node
    (Rule (Print S)
      '(display (Trans S)))
    # Transform Concat node
    (Rule (Concat S ...)
      '(string-append . ,(map Trans S)))
    # Transform String node
    (Rule (String L)
      ''L)))

# Example transformation usage:
# (Transform (MetaL-to-Lisp) <program node>)
# This will convert the MetaL structure to Lisp code

# Generate Lisp code from MetaL representation
(Program
  (Function
    (Name "main")
    (Parameters)
    (Body
      (Print
        (Concat
          (String "Hello")
          (String " ")
          (String "World"))))))


# After transformation, a Lisp equivalent code would look like this:
# 
# (begin
#   (define (main)
#     (display (string-append "Hello" " " "World"))))