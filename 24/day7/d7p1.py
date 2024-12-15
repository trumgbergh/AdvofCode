import csv
import re

def main():
    with open("in.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            s = row[0]
            print(s)
            a = re.finditer(r"(\d+): (\d+)(?:\s(\d+))*", s)
            for t in a:
                print(t.span())

if __name__ == "__main__":
    exit(main())
