# create random passwords:
from string import ascii_letters, digits, punctuation
import random

signs = ascii_letters + digits + punctuation
password_length = 6
password = ''.join(random.sample(signs, password_length))
print(password)