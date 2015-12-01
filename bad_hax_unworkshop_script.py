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

local = 5
locality = 3
nonlocality = 1
interlocality = 0
delocality = 4
paralocality = 6
intralocality = 8
prelocality = 9
postlocality = 10

localities = [local, locality, nonlocality, interlocality, delocality, paralocality, intralocality, prelocality, postlocality]

def setup(pointless):
	if not pointless:
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

		global local
		global locality
		global nonlocality
		global interlocality
		global delocality
		global paralocality
		global intralocality
		global prelocality
		global postlocality

		local = print_pipe
		locality = print_plus
		nonlocality = print_minus
		interlocality = print_slash
		delocality = print_backslash
		paralocality = print_underscore
		intralocality = print_period
		prelocality = print_whitespace
		postlocality = print_newline

	else:
		pass

def print_bad_hax():
	def print_first_line():
		for _ in range(4):
			prelocality()
		for _ in range(4):
			local()
			nonlocality()
		local()
		for _ in range(6):
			prelocality()
		for _ in range(3):
			local()
			locality()
		local()
		for _ in range(5):
			prelocality()
		for _ in range(4):
			local()
			interlocality()
		local()
		postlocality()

		print_second_line()
	
	def print_second_line():
		for _ in range(4):
			prelocality()
		print("|-|    |-|   |+|     |+|   |/|     |/|")

		print_third_line()
	
	def print_third_line():
		for _ in range(4):
			prelocality()
		print("|-|-|-|-|    |+|+|+|+|+|   |/|      |/|")

		print_fourth_line()
	
	def print_fourth_line():
		for _ in range(4):
			prelocality()
		print("|-|    |-|   |+|     |+|   |/|     |/|")

		print_fifth_line()
	
	def print_fifth_line():
		for _ in range(4):
			prelocality()
		print("|-|-|-|-|    |+|     |+|   |/|/|/|/|")
		postlocality()

		print_sixth_line()
	
	def print_sixth_line():
		for _ in range(4):
			prelocality()
		print("|/|    |\|      /-/\-\      \--\  /--/")

		print_seventh_line()
	
	def print_seventh_line():
		for _ in range(4):
			prelocality()
		print("|/|    |\|     /-/  \-\      \--\/--/")

		print_eighth_line()
	
	def print_eighth_line():
		for _ in range(4):
			prelocality()
		print("|/||||||\|    /-/====\-\      [----]")

		print_ninth_line()
	
	def print_ninth_line():
		for _ in range(4):
			prelocality()
		print("|/|    |\|   /-/      \-\    /--/\--\\")

		print_tenth_line()
	
	def print_tenth_line():	
		for _ in range(4):
			prelocality()
		print("|/|    |\|  /-/        \-\  /--/  \--\\")

		postlocality()

	print_first_line()

for localilazationality in localities:
	setup(localilazationality)
print_bad_hax()