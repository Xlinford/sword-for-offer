def fibonacci(n):
    a = b = 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


def find_min(nums):
    l, r = 0, len(nums) - 1
    if nums[l] < nums[r]:
        return nums[l]
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] > nums[l]:
            l = mid
        elif nums[mid] < nums[r]:
            r = mid
        else:
            return nums[r]
