import csv
import re

def main():
    with open("in.txt", "r") as file:
        lines = file.readlines()
        sum = 0
        e = 1
        for s in lines:
            a = re.findall(r'mul\((\d+),(\d+)\)', s)
            id = re.finditer(r'mul\((\d+),(\d+)\)', s)
            b = re.finditer(r'do\(\)', s)
            c = re.finditer(r'don\'t\(\)', s)

            aid = []
            do = [-1]
            dont = [-1]
            for match in b:
                f, s = match.span()
                do.append(f)
            for match in c:
                f, s = match.span()
                dont.append(f)

            for match in id:
                f, s = match.span()
                aid.append(f)

            cnt = 0
            j = 0
            k = 0
            for f, s in a:
                i = aid[cnt]
                while j < len(do) - 1:
                    if do[j + 1] > i:
                        break
                    j += 1
                while k < len(dont) - 1:
                    if dont[k + 1] > i:
                        break
                    k += 1
                if dont[k] > do[j]:
                    e = 0
                elif do[j] > dont[k]:
                    e = 1
                sum += int(f) * int(s) * e
                cnt += 1
            if dont[len(dont) - 1] > do[len(do) - 1]:
                e = 0
            elif dont[len(dont) - 1] < do[len(do) - 1]:
                e = 1
        print(sum)

if __name__ == "__main__":
    exit(main())
