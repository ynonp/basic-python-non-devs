"""
We use the keyword "def" to write a function

     function_name uses lowercase letters and underscores (do_stuff)
def <function_name>(p1, p2, p3):
    exp1
    exp2
    ...
    (Optional) return Stuff (by default functions return None)
"""

################
import utils
print(utils.square(2))


def hello_functions_world(name: str):
    print(f"Hello, {name}")
    return len(name)


def is_first_letter_equal_to_last_letter_of_other_word(word1, word2):
    return word1[0] == word2[-1]


hello_functions_world("ynon")

print(is_first_letter_equal_to_last_letter_of_other_word(word1="one", word2="two"))
print(is_first_letter_equal_to_last_letter_of_other_word(word2="two", word1="one"))

x = "one"
hello_functions_world(x)

#y = 5
#hello_functions_world(y)




