class Solution:
    # 实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，x^n）
    def myPow(self, x: float, n: int) -> float:
        def pow_with_unsign(x, m):

            if m == 1:
                return x
            ans = pow_with_unsign(x, m >> 1)
            ans *= ans
            if m & 1 == 1:
                ans *= x
            return ans

        if n > 0:
            return pow_with_unsign(x, n)
        elif n == 0:
            return 1
        else:
            return 1 / pow_with_unsign(x, -n)

    # 打印从1到最大的n位数
    def print_n(self, n: int):
        n = 10 ** n
        for i in range(1, n):
            print(i)

    # 正则表达式，pattern为某种规则的正则表达式，s为某字符串，判断pattern是否与s相同
    # 首先判断模板pattern是否为空；判断首字母是否相同或为'.'，且s不为空；判断pattern长度，大于1且有*则开始递归；
    #
    def match(self, s, pattern):
        if not pattern: return not s
        f_match = bool(s) and pattern[0] in {s[0], '.'}
        if len(pattern) > 1 and pattern[1] == '*':
            return (self.match(s, pattern[2:])) or (f_match and self.match(s[1:], pattern))
        else:
            return f_match and self.match(s[1:], pattern[1:])


class SolutionStrmatch:
    mem = dict()

    def isMatch(self, s: str, p: str) -> bool:
        self.mem = dict()
        return self.dp(0, 0, s, p)

    def dp(self, i, j, s, p):   # 判断第i,j位

        S, P = len(s), len(p)       # 取两个字符串的长度
        if j == P: return i == S    # 如果p索引结束，返回s是否索引结束
        if i == S:
            if (P - j) % 2 == 1: return False   # 如果s索引结束，p剩余字符为奇数，则不可能匹配
            while j < P:                        # 为偶数，判断其后所有偶数位字符是否为*，使重复次数为0
                if p[j + 1] != "*": return False
                j += 2
            return True
        if (i, j) in self.mem:
            return self.mem[(i, j)]     # 返回第i,j位的判断情况
        res = False
        if s[i] == p[j] or p[j] == ".":     # 当前位判断是否相同
            if j < P - 1 and p[j + 1] == "*":   # 如p索引位未结束且下一位为*，则判断后续字符串
                # 有两种情况，s下一位重复或不重复
                res = self.dp(i + 1, j, s, p) or self.dp(i, j + 2, s, p)
            else:
                res = self.dp(i + 1, j + 1, s, p)   # 没有*，各进一位
        else:
            if j < P - 1 and p[j + 1] == "*":   # 不相同，有*则相同，没有*则不同
                res = self.dp(i, j + 2, s, p)   # p进2位，继续判断
            else:
                res = False
        self.mem[(i, j)] = res  # 利用memory记录点值，共len(s)*len(p)
        return res

    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去掉首尾空格
        s = s.lower()  # 小写字母

        # 正负(+-) 整数 [.] 整数 [E/e] 正负(+-) 整数

        sign, numbers, dot, expon = [False] * 4

        for i, ch in enumerate(s):
            if ch.isdigit():
                numbers = True

            elif ch in ('+', '-'):
                if i > 0 and s[i - 1] != 'e':  # 符号位出现,如果不在字符串第一位，只能在 E/e之后
                    return False
                if sign:
                    return False  # 如果符号位出现过(遇到 e会将符号位、数字 重置为0)
                sign = True

            elif ch == '.':
                if dot or expon:
                    return False
                dot = True

            elif ch == 'e':
                if not numbers or expon:
                    return False

                sign = False
                numbers = False
                expon = True
            else:
                return False

        return numbers

    def reOrderArray(self, array):
        from collections import deque
        q = deque()
        n = len(array)
        for i in range(n):
            if array[i] & 1 == 0:
                q.append(array[i])
            if array[-i-1] & 1 == 1:
                q.appendleft(array[-i-1])
        return q



if __name__ == '__main__':
    solution = SolutionStrmatch()
    print(solution.reOrderArray([1,2,3,4,5,6,7]))