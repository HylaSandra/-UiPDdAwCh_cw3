import logging
import base64
import random
import string

#zadanie1


def logs():
    logger = logging.getLogger('simple_example')
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.debug("debug message")


logs()

#zadanie2


def encoding():

    print("Type text to encode:")
    text = input()
    text = text.encode()
    text = base64.b64encode(text)
    print("Encoded text: " + str(text))


encoding()

print("***")

#zadanie3


def password_generator():
    password = ""
    length = random.randint(8, 15)
    for i in range(length):
        password += random.choice(string.ascii_letters + string.digits + string.punctuation)
    return password


def main():
    print("Generated password:")
    print(password_generator())


main()
