# Rule: #DON'T RUN THIS
>lmao you can't run it now...

Press "f"+"ctrl" to find topic

---
# Types...
> You can check the typing by using:
```python
x=98
print(type(x))
```
### ***int()*** AKA ***integers***
Are  you can internally do math with
> Written as: ```25``` or ```8``` or ```42```

### ***str()*** AKA ***strings*** 
It is a line of letters and numbers. str can only be converted into a "int" if it is all numbers (currently(you will find out how in the far future)) They shared some functions with array/List
> Written as: ```"_"``` or ```"2four"``` or ```"24"``` or ```"twofour"```

### ***list[]*** AKA ***array*** 
They are a list of things that you can .append / .pop .remove and replace things like str,int and even other lst.
> Written as:  ```[12,32,"sad",["yes","no"]]```

Some key definitions that you may need to know before you get to functions. Here is the example array that you will be using to learn the following defintions:     ```lst = [1,4,3,2]```
  - Index is where in the lst the thing is (alway start at zero)
  >Example: index of 4 in the lst is ```1```
  >
  >Example: index of 2 in the lst is ```3```
  - Value is the value at the index
  >Example: value at index 0 is ```1```
  >
  >Example: value at index -1 is ```2```


### ***Floats*** 
They are just variables that point at another variable
>Example: ```fly=None  sky=1  fly=sky``` and when you ```return fly```, you will get ```1``` AKA what ```sky``` variable is.

### ***Bools*** AKA ***True/False***
Every statement returns this in some way or another. It tells the code to run the stuff in/below it or not.

### ***Nodes*** AKA No Other Defintion, Eventually Study.
An advanced topic that deals with trees and is one way.
Written as: LinkedList[] or ListNode()
Nodes are a singluar entity that can only look forward. Here is an example of a single linked list:

```a -> b -> c -> d -> e ```

Node **a** only know what Node **b** is but Node **b** dont know what Node **a** is and only knows about what is in front of it which is Node **c**.


**Trees** actually look like roots but it is better to think of them as an upside down tree so the definitions are easier. They are the next level of nodes.

          Example of a Tree:
                          <a>
                  <b>             <c>
              <d>      e       f       g
             h   i
>Node ```a``` is a **root** node because it is the top/start of the tree (for now)
>
>Node ```b``` and ```c``` are both child nodes of Node ```a``` and parent nodes of ```d,e``` and ```f,g``` respectively
>
>Node ```h, i, e, f, g``` are all leaf nodes because they don't have child nodes and is the end of ListNode()
>
Levels of the Tree: The concept of this is basically the same as arrays. They start a level 0 and move down/up to level x.
>Level 0: ```a```
>
>Level 1: ```b, c```
>
>Level 2: ```d, e, f, g```
>
>Level 3: ```h, i```

---
# Functions/Statements
## Converisons:
- ```int()``` ONLY takes all number str() or list()
- ```str()``` Anything (you can also type "" but it turn every inbetween them into a str not the actual function)
- ```list()``` str or you can append/pop int and even other lists

## Math:
- ```+, -, /, *``` works are normal math
- ```**``` and ```pow(int,int)``` are the same thing
- ```=```make the thing on the left equal to the thing on the right
- ```x-=y``` is the same as ```x=x-y```
- ```x+=y``` is the same as ```x=x+y```
- ```x*=y``` is the same as ```x=x*y```
- Bascially you can put math stuff in front of ```=```

## Comparasions:
- ```==``` checks if it is equal (return True/False)
- ```!=``` check if it is not equal (return True/False)
- not is the same as ```!```

## str and list functions: 
(lst is example list, x and y are integers)
- ```lst[index]``` will return the value at that index of lst
- ```lst[:x]``` will return everything in front of index x
- ```lst[x:]``` will return everything after index x
- ```lst[x:y]``` will return everything from x to y
- ```lst[::-1]``` will reversed the lst just like lst.reversed() but isnt a builtin (^o^)
- ```lst.index(32)``` will return the index of 32 if there are not 33 things in the ```lst``` else it will break.

>Other list functions: #https://www.programiz.com/python-programming/methods/list/index

- ```lst.append(x)``` with add ```x``` to the end of the lst
- ```lst.pop(x)``` will remove what is at index ```x```
- ```len(lst)``` returns the length of lst as an int

## if, elif and else statement
ONlY WORKS WITH SAME TYPING
- ```if _ <comparasion> _:``` return if the statement is True/False and runs the code after/in the if statement
- ```else:``` runs the code in the ```else``` statement if the ```if``` statement fails
- ```elif _ <comparasion> _:``` return something if the ```if``` statement fails (```else if```)

## Print stuff on the Console
>Written as: ```print()```
```python
class textmodifiers:
  ResetAll = "\033[0m"

	Bold       = "\033[1m"
	Dim        = "\033[2m"
	Underlined = "\033[4m"
	Blink      = "\033[5m"
	Reverse    = "\033[7m"
	Hidden     = "\033[8m"

	ResetBold       = "\033[21m"
	ResetDim        = "\033[22m"
	ResetUnderlined = "\033[24m"
	ResetBlink      = "\033[25m"
	ResetReverse    = "\033[27m"
	ResetHidden     = "\033[28m"

	Default      = "\033[39m"
	Black        = "\033[30m"
	Red          = "\033[31m"
	Green        = "\033[32m"
	Yellow       = "\033[33m"
	Blue         = "\033[34m"
	Magenta      = "\033[35m"
	Cyan         = "\033[36m"
	LightGray    = "\033[37m"
	DarkGray     = "\033[90m"
	LightRed     = "\033[91m"
	LightGreen   = "\033[92m"
	LightYellow  = "\033[93m"
	LightBlue    = "\033[94m"
	LightMagenta = "\033[95m"
	LightCyan    = "\033[96m"
	White        = "\033[97m"

	BackgroundDefault      = "\033[49m"
	BackgroundBlack        = "\033[40m"
	BackgroundRed          = "\033[41m"
	BackgroundGreen        = "\033[42m"
	BackgroundYellow       = "\033[43m"
	BackgroundBlue         = "\033[44m"
	BackgroundMagenta      = "\033[45m"
	BackgroundCyan         = "\033[46m"
	BackgroundLightGray    = "\033[47m"
	BackgroundDarkGray     = "\033[100m"
	BackgroundLightRed     = "\033[101m"
	BackgroundLightGreen   = "\033[102m"
	BackgroundLightYellow  = "\033[103m"
	BackgroundLightBlue    = "\033[104m"
	BackgroundLightMagenta = "\033[105m"
	BackgroundLightCyan    = "\033[106m"
	BackgroundWhite        = "\033[107m"

print(color.Bold + 'Hello World !' + color.END)
```
- Make sure put stuff in str so it is printable=""

- Ask for inputs (returns things as str())
>Written as: _=input("")

- class and def functions
  - Writing class
      -class run the same as def function but is in a higher level
    
## Writing def function
```def variable_a(input_a:typing, input_b:typing)-> typing(output):```

Key points of the def function:

- variable_a is the thing that you will call the function by and it looks something like this: ```variable_a(input_a, input_b)```
  - There are two inputs cuz the def function need to take in two input
  - writing self will mess with the function and mean it very confusing even thou it is literal the same as any other word. You can do ```self.number``` and ```sad.number``` and they do the **same thing**
- ```input_a``` is just the name of variable that is inputed
- ```typing``` is reccomend to write to make sure there is not collision problems with the code and makes it easier/faster to debug
- ```typing(output)``` is the typing of the output
  
  
  
  
Now here is a actual example that acts like a calculator:
  (int is the integer/numbers)
```python
def example_calculator(first:int, second:int)-> int:  
  sum=first+second
  
  #return the answer
  return sum
        
#now we run the function by calling it
print(example_calculator(21,23))
```
The above is basically a function that adds the first number and the second number into the sum of both numbers. It then return the called function as the sum. The calling function is in ```print()``` so you can see it. Since it is returned as a int, you can even do math with it. Something like ```213 + example_calculator(21,23)``` will give you ```257```.
    