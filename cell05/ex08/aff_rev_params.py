import sys

params = [arg for arg in sys.argv[1:] if arg.strip() != ""]

if len(params) < 2:
    print("none")
else:
    for arg in reversed(params):
        print(arg)