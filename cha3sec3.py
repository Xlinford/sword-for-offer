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

    # 正则表达式
    def match(self, s, pattern):
        if not pattern: return not s

