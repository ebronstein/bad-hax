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


# def print_newline():
#     print()
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
def print_plus():
    print("+", end="")
def print_underscore_plus():
    print("_+", end = "")
def print_plus_underscore():
    print("_+", end = "")
def print_plus_underscore():
    print("+_", end = "")
def print_at():
    print("@", end = "")
def print_tab():
    for _ in range(4):
        print_whitespace()
def print_three_plus():
    print_plus_underscore()
    print_plus()
def print_three_underscore():
    print_underscore()
    print_plus_underscore()
def print_parentheses_one():
    print("(", end = "")
def print_parentheses_two():
    print(")", end = "")
def print_underscore_plus():
    print("_+", end = "")
def print_plus_underscore():
    print("_+", end = "")
def print_plus_underscore():
    print("+_", end = "")
def print_at():
    print("@", end = "")
def print_tab():
    for _ in range(4):
        print_whitespace()
def print_three_plus():
    print_plus_underscore()
    print_plus()
def print_three_underscore():
    print_underscore()
    print_plus_underscore()
def print_parentheses_one():
    print("(", end = "")
def print_parentheses_two():
    print(")", end = "")
def print_whitespace():
    print(" ", end="")
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
    print()
    print_first_line()

for localilazationality in localities:
    setup(localilazationality)

# use poop() to print the top, use end() to print the bottom.

def poop():
    # line i
    for _ in range(5):
        print_tab()
    print_whitespace()
    print_three_plus()
    print_newline()

    # line ii
    for _ in range(4):
        print_tab()
    for _ in range(2):
        print_whitespace()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    print_newline()

    # line iii
    for _ in range(3):
        print_tab()
    for _ in range(3):
        print_whitespace()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    print_newline()

    # line iv
    for _ in range(3):
        print_tab()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    print_newline()

    # line v
    for _ in range(2):
        print_tab()
    for _ in range(3):
        print_whitespace()
    print_plus_underscore()
    # eye
    print_whitespace()
    print_backslash()
    print_whitespace()
    # forehead
    print_underscore_plus()
    print_underscore()
    print_three_plus()
    print_three_underscore()
    print_three_plus()
    # eye
    print_whitespace()
    print_slash()
    print_whitespace()
    print_three_plus()
    print_newline()

    # line vi
    for _ in range(2):
        print_tab()
    print_whitespace()
    print_plus_underscore()
    print_parentheses_one()
    for _ in range(2):
        print_whitespace()
    print_at()
    print_backslash()
    print_whitespace()
    print_parentheses_two()
    # forehead
    print_underscore()
    print_three_plus()
    print_three_underscore()
    print_plus()
    # eye
    print_parentheses_one()
    print_whitespace()
    print_slash()
    print_at()
    for _ in range(2):
        print_whitespace()
    print_parentheses_two()
    # temples
    print_three_plus()
    print_newline()

    # line vii
    for _ in range(2):
        print_tab()
    print_three_plus()
    print_underscore_plus()
    for _ in range(3):
        print_whitespace()
    print_backslash()
    print_three_underscore()
    print_three_plus()
    print_three_underscore()
    print_plus()
    print_slash()
    for _ in range(3):
        print_whitespace()
    print_three_underscore()
    print_three_plus()
    print_newline()

    # line viii
    print_tab()
    for _ in range(2):
        print_whitespace()
    for _ in range(5):
        print_three_plus()
        print_three_underscore()
    print_three_plus()
    print_newline()

    # line ix
    print_tab()
    for _ in range(2):
        print_three_plus()
        print_three_underscore()
    print_backslash()
    print_whitespace()
    print("VVVVVVVV", end = "")
    print_whitespace()
    print_slash()
    for _ in range(2):
        print_three_plus()
        print_three_underscore()
    print_plus()
    print_newline()

    # line x
    for _ in range(2):
        print_whitespace()
    for _ in range(2):
        print_three_plus()
        print_three_underscore()
    print_three_plus()
    print_backslash()
    for _ in range(8):
        print_underscore()
    print_slash()
    print_underscore
    for _ in range(2):
        print_three_plus()
        print_three_underscore()
    print_three_plus()
    print_newline()


    # line xi
    print_underscore()
    for _ in range(7):
        print_three_plus()
        print_three_underscore()
    print_plus_underscore()
    print_newline()

    # line xii
    for _ in range(7):
        print_three_plus()
        print_three_underscore()
    print_three_plus()
    print_newline()

    # line xiii
    for _ in range(21):
        print_whitespace()
        print_period()
    print_newline()



def end():
    # dots
    for _ in range(21):
        print_whitespace()
        print_period()
    print_newline()
    # one
    for _ in range(7):
        print_three_plus()
        print_three_underscore()
    print_three_plus()
    print_newline()
    # two
    print_underscore()
    for _ in range(7):
        print_three_plus()
        print_three_underscore()
    print_plus_underscore()
    print_newline()


def walk_the_walk():
    poop()
    print_bad_hax()
    end()
