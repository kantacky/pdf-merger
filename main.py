import sys
from merge import merge
from reverse import reverse

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "reverse":
        input = sys.argv[2]
        output = sys.argv[3]
        reverse(input, output)
    elif command == "merge":
        input1 = sys.argv[2]
        input2 = sys.argv[3]
        output = sys.argv[4]
        merge(input1, input2, output)
