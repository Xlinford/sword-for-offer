def fibonacci(n):
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def find_min(nums):
    h, t = 0, len(nums) - 1
    if nums[h] < nums[t]:
        return nums[h]
    while h <= t:
        m = (h + t) // 2
        if nums[h] > nums[m]:
            t = m
        elif nums[m] < nums[t]:
            h = m
        else:
            return nums[h]


def exits(self, g, word: str) -> bool:
    R, C = len(g), len(g[0])

    def speard(i, j, w):
        if not w:
            return True
        original, g[i][j] = g[i][j], '-'
        spreaded = False
        for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if 0 <= x < R and 0 <= y < C and g[x][y] == w[0] and speard(x, y, w[1:]):
                spreaded = True
                break
        g[i][j] = original
        return spreaded

    for i in range(R):
        for j in range(C):
            if g[i][j] == word[0] and speard(i, j, word[1:]):
                return True

    return False


# 机器人的运动范围
class SyboMoveSolution:
    def movingCount(self, threshold, rows, cols):
        visited = [[False] * cols for _ in range(rows)]

        def get_sum(x, y):
            return sum(map(int, str(x) + str(y)))

        def movingCore(threshold, rows, cols, i, j):
            if get_sum(i, j) <= threshold:
                visited[i][j] = True
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < rows and 0 <= y < cols and not visited[x][y]:
                        movingCore(threshold, rows, cols, x, y)

        movingCore(threshold, rows, cols, 0, 0)
        return sum(sum(visited, []))

# 剪绳子
def cut_rope(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2
    else:
        three_muti_times = length // 3
        left = length % 3
        if left == 1:
            three_muti_times -= 1
        two_muti_times = (length - 3*three_muti_times)//2
        return (3**three_muti_times)*(2**two_muti_times)


# 二进制中1的个数
def hamming_weight(n):
    count = 0
    for _ in range(32):
        count += (n & 1 == 1)
        n >>= 1
    return count
def hamming_weigth1(n):
    bits = 0
    while n:
        bits += 1
        n = (n-1) & n
    return bits

