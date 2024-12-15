import csv

def main():
    with open("in.txt", "r") as file:
        reader = csv.reader(file, delimiter = ' ')
        sum = 0
        for row in reader:
            tmp = []
            for val in row:
                tmp.append(int(val))
            for id in range(len(tmp)):
                b = 1
                a = tmp.copy()
                for i in range(len(a)):
                    if i > 0:
                        if not 1 <= abs(a[i] - a[i - 1]) <= 3:
                            b = 0
                        if i < len(a) - 1 and a[i] > a[i - 1] and a[i] > a[i + 1]:
                            b = 0
                        if i < len(a) - 1 and a[i] < a[i - 1] and a[i] < a[i + 1]:
                            b = 0
                if b != 0:
                    sum += 1
                    break
                del a[id]
                b = 1
                for i in range(len(a)):
                    if i > 0:
                        if not 1 <= abs(a[i] - a[i - 1]) <= 3:
                            b = 0
                        if i < len(a) - 1 and a[i] > a[i - 1] and a[i] > a[i + 1]:
                            b = 0
                        if i < len(a) - 1 and a[i] < a[i - 1] and a[i] < a[i + 1]:
                            b = 0
                if b != 0:
                    sum += 1
                    break
        print(sum)

if __name__ == "__main__":
    exit(main())
