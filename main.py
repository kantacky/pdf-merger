import sys
from reverse import reverse

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "reverse":
        input_pdf = sys.argv[2]
        output_pdf = sys.argv[3]
        reverse(input_pdf, output_pdf)
    elif command == "merge":
        pass
