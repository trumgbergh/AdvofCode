import csv

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
a = []
def check(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

def BFS(i, j, n, m):
    vis = []
    q = []
    q.append((i, j))
    vis.append((i, j))
    cnt = 0
    while len(q) != 0:
        x, y = q[0]
        q.pop(0)
        

        for d in range(len(dr)):
            nx = x + dr[d]
            ny = y + dc[d]
            if (nx, ny) in vis:
                continue
            if not check(nx, ny, n, m):
                continue
            if int(a[nx][ny]) - int(a[x][y]) != 1:
                continue
            if a[nx][ny] == '9':
                cnt += 1
                continue
            q.append((nx, ny))
    return cnt



def main():
    with open("in.txt", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            a.append(row[0])
        n = len(a)
        m = len(a[0])

        ans = 0
        for i in range(n):
            for j in range(m):
                if a[i][j] == '0':
                    ans += BFS(i, j, n, m)
                    print(i, j, BFS(i, j, n, m))
        print(ans)


if __name__ == "__main__":
    exit(main())
