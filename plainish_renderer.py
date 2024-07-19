import sys
def main():
    args = sys.argv
    path = ""
    if len(args) != 2:
        print("Expect one argument: Path to file to convert")
        return 0
    else:
        path = args[1]
        getFile(path)

def getFile(path):
    file = ""

    try:
        file = open(path, "r")
        if not file.name.endswith(".ptxt"):
            print("File does not end with .ptxt. Require a .ptxt file")
            return 0
    except FileNotFoundError:
        print("File not found")
        return 0
    file = file.read()
    parse(file)

def parse(raw):
    sections = ""


main()