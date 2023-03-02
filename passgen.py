from os import urandom 
from argparse import ArgumentParser

Parser = ArgumentParser(description="Simple password generator")
Parser.add_argument("-1","--length", help="Length of password", type=int, default=8)
args, unknown = Parser.parse_known_args() 

pass_l = 0

while True:
    if pass_l == args.length:
        break
    try:
        char = urandom(1).decode("UTF-7")
        if ord(char) > 32 and ord(char) < 127:
            pass_l+= 1
            print(char, end="")
    except (UnicodeDecodeError, TypeError):
        pass

print()
