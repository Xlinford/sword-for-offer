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

