import csv

a = []
b = []


def main():
    with open("in.txt", "r") as file:
        reader = csv.reader(file, delimiter = ' ')
        for row in reader:
            a.append(int(row[0]))
            b.append(int(row[3]))
    a.sort()
    b.sort()
    sum = 0
    for i in range(len(a)):
        print(a[i], b[i])
        sum += abs(a[i] - b[i])
    print(sum)

if __name__ == "__main__":
    exit(main())
