# Rule: #DON'T RUN THIS
lmao you can't run it now.
I hope this is better. If you hate it, revert it.
- means defintions/Information of ___ below
   - means entry
```py
means input/internal things/variable
```
Press "f"+"ctrl" to find topic

### Types...
  -int AKA integers that you can internally do math with
Written as: _
Example:231

  - str AKA strings which is a line of letters and numbers. str can only be converted into a "int" if it is all numbers (currently(you will find out how in the far future)) They shared some functions with array(lst)
Written as: "_"
Example: "2four" or "24" or "twofour"
  - char '_'
    Example str:"213a" (use to learn defintions)
    - Index is where in the str the thing is(alway start at zero)
    Example: index of 2 in the lst is 0
    -Value is the value at the index
    Example: value at index 3 is a

  - lst AKA array/list which you can .append / .pop .remove and replace things like str,int and even other lst.
Written as: [_]
Example: [12,32,"sad",["yes","no"]]
    Example lst:[1,4,3,2] (use to learn defintions)
    -Index is where in the lst the thing is(alway start at zero)
    Example: index of 4 in the lst is 1
    - Value is the value at the index
    Example: value at index 3 is 2

  - floats are just pointers
  Example: fly=None  sky=1  fly=sky and when you return fly, you will get 1 AKA what sky variable is.

  -Bools AKA True/False, every statement returns this in some way or another. It tells the code to run the stuff in it or not.

  - Nodes AKA No Other Defintion, Eventually Study. An advanced topic that deals with trees and is one way.
Written as: LinkedList[] or ListNode()

### Functions/Statements
  >Converisons:
    - int() ONLY takes all number str() or list()
    - str() Anything (you can also type "" but it turn every inbetween them into a str not the actual function)
    - list() str or you can append/pop int and even other lists

- Math:
    - +,-,/,* works are normal math
    - ** and pow(_,_) are the same thing
    - = make the thing on the left equal to the thing on the right
      * x-=y is the same as x=x-y
      * x+=y is the same as x=x+y
      * x*=y is the same as x=x*y
      *Bascially you can put math stuff in front of =

  - Comparasions:
    - == checks if it is equal (return True/False)
    - != check if it is not equal (return True/False)
    - not is the same as !

  - str and lst functions:
    - lst[index] will return the value at that index of lst
      - lst[:x] will return everything in front of index x
      - lst[x:] will return everything after index x
      - lst[x:y] will return everything from x to y
      - lst[::-1] will reversed the lst just like lst.reversed() but isnt a builtin \(^o^)/
    -lst.index(32) will return the index of 32 if 32 is in the lst else it will break

  - lst functions: #https://www.programiz.com/python-programming/methods/list/index
    #x is a integer
    -lst.append(x) with add x to the end of the lst
    -lst.pop(x) will remove what is at index x
    -len(lst) returns the length of lst as an int

### if, elif and else statement
    ONlY WORKS WITH SAME TYPING
    if _ <comparasion> _: return if the statement is True/False and runs the code after/in the if statement
    else: runs the code in the "else" statement if the "if" statement fails
    elif _ <comparasion> _: return something if the "if" statement fails (else if)

### Print stuff on the Console
    Written as: print()
    Put stuff in str so it is printable=""

 - Ask for inputs (returns things as str())
    Written as: _=input("")

- class and def functions
  - Writing class
      -class run the same as def function but is in a higher level
- Writing def function
      ```py
      def x(y:z) -> z:
      ```
        - x represent the name of the function
        - y represent the variable you are going to work with
        - z represents the typing of the variable and also regulate what typing you have to return or it will just crash so you can fix it before it becames a big problem. It are optional but I reccomend writing them like that so it is easier to read.

### Definitions:
  - Nodes are a singluar entity that can only look forward:
    a -> b -> c -> d -> e 
    Node <a> only know what Node <b> is but Node<b> dont know what Node <a> is and only knows about what is in front of it which is Node <c>