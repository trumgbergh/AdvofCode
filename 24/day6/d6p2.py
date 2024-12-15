import csv

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def inGrid(x, y, n, m):
    return 0 <= x < n and 0 <= y < m

def checkLoop(a, x, y, n, m):
    id = 0
    visited = set()
    while 0 <= x < n and 0 <= y < m:
        if (x, y, id) in visited:
            return True
        visited.add((x, y, id))
        nx = x + dr[id]
        ny = y + dc[id]
        if not inGrid(nx, ny, n, m):
            break
        if a[nx][ny] == '#':
            id = (id + 1) % 4
        else:
            x = nx
            y = ny
    return False


def main():
    with open("in.txt", "r") as file:
        a = []
        reader = csv.reader(file)
        for row in reader:
            r = []
            for rr in row:
                for c in rr:
                    r.append(c)
            a.append(r)

        n = len(a)
        m = len(a[0])
        x = 0
        y = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == '^':
                    x = i
                    y = j
                    break
        ans = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == '^' or a[i][j] == '#':
                    continue
                a[i][j] = '#'
                ans += checkLoop(a, x, y, n, m)
                a[i][j] = '.'
        print(ans)

if __name__ == "__main__":
    exit(main())
