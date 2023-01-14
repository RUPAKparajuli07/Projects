import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password
password = generate_password(12)
print(password)
