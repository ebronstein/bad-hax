"""
                     +_+
                  +_+_+_+_+
               +_+_+_+_+_+_+_+
            +_+_+_+_+_+_+_+_+_+_+
           +_ \ _+_+_+_+_+_+ / +_+
         +_(  @\ )_+_+_+_+( /@  )+_+
        +_+_+   \_+_+_+_+_+/   _+_+_+
      +_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
    +_+_+_+_+_+_\ VVVVVVVV /+_+_+_+_+_+_+
  +_+_+_+_+_+_+_+\________/_+_+_+_+_+_+_+_+
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
 . . . . . . . . . . . . . . . . . . . . .

    |-|-|-|-|      |+|+|+|     |/|/|/|/|
    |-|    |-|   |+|     |+|   |/|     |/|
    |-|-|-|-|    |+|+|+|+|+|   |/|      |/|
    |-|    |-|   |+|     |+|   |/|     |/|
    |-|-|-|-|    |+|     |+|   |/|/|/|/|

    |/|    |\|      /-/\-\      \--\  /--/
    |/|    |\|     /-/  \-\      \--\/--/
    |/||||||\|    /-/====\-\      [----]
    |/|    |\|   /-/      \-\    /--/\--\
    |/|    |\|  /-/        \-\  /--/  \--\

 . . . . . . . . . . . . . . . . . . . . .
+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
"""

def print_pipe():
	print("|", end="")

def print_plus():
	print("+", end="")

def print_minus():
	print("-", end="")

def print_slash():
	print("/", end="")

def print_backslash():
	print("\\", end="")

def print_underscore():
	print("_", end="")

def print_period():
	print(".", end="")

def print_whitespace():
	print(" ", end="")

def print_newline():
	print("\n", end="")

def print_bad():
	for _ in range(4):
		print_whitespace()
	for _ in range(4):
		print_pipe()
		print_minus()
	print_pipe()
	for _ in range(6):
		print_whitespace()
	for _ in range(3):
		print_pipe()
		print_plus()
	print_pipe()
	for _ in range(5):
		print_whitespace()
	for _ in range(4):
		print_pipe()
		print_slash()
	print_pipe()
	print_newline()

	for _ in range(4):
		print_whitespace()
	print("|-|    |-|   |+|     |+|   |/|     |/|")

	for _ in range(4):
		print_whitespace()
	print("|-|-|-|-|    |+|+|+|+|+|   |/|      |/|")

	for _ in range(4):
		print_whitespace()
	print("|-|    |-|   |+|     |+|   |/|     |/|")

	for _ in range(4):
		print_whitespace()
	print("|-|-|-|-|    |+|     |+|   |/|/|/|/|")

	print_newline()

	for _ in range(4):
		print_whitespace()
	print("|/|    |\|      /-/\-\      \--\  /--/")

	for _ in range(4):
		print_whitespace()
	print("|/|    |\|     /-/  \-\      \--\/--/")

	for _ in range(4):
		print_whitespace()
	print("|/||||||\|    /-/====\-\      [----]")

	for _ in range(4):
		print_whitespace()
	print("|/|    |\|   /-/      \-\    /--/\--\\")

	for _ in range(4):
		print_whitespace()
	print("|/|    |\|  /-/        \-\  /--/  \--\\")

	print_newline()

print_bad()