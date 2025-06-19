import sys
import re

def process_args(arguments):
    if not arguments:
        print("none")
    else:
        for arg in arguments:
            if not re.search(r'ism$', arg):
                print(arg + "ism")

def main():
    if len(sys.argv) > 1:
        process_args(sys.argv[1:])
    else:
        user_input = input("Enter parameters separated by spaces: ").strip()
        if user_input:
            arguments = user_input.split()
            process_args(arguments)
        else:
            print("none")

if __name__ == "__main__":
    main()