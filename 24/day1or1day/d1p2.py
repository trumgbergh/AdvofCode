import csv
from collections import Counter

a = []
b = []

def main():
    with open("in.txt", "r") as file:
        reader = csv.reader(file, delimiter = ' ')
        for row in reader:
            a.append(row[0])
            b.append(row[3])
    bcounter = Counter(b)
    sum = 0
    for val in a:
        sum += int(val) * bcounter[val]
    print(sum)

if __name__ == "__main__":
    exit(main())
