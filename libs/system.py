import string
import random

def random_string(number_of_strings = 5 , length_of_string = 8):
    for x in range(number_of_strings):
      ret = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))

    return ret