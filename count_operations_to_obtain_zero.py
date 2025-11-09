class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                count += num1 // num2
                num1 %= num2
            else:
                count += num2 // num1
                num2 %= num1
        return count

def run_tests():
    solution = Solution()
    tests = [
        (3, 3),
        (10, 2),
        (6, 4),
        (15, 1),
        (0, 5),
        (5, 0),
        (1_000_000, 999_999),
        (1_000_000, 500_000),
    ]

    for num1, num2 in tests:
        result = solution.countOperations(num1, num2)
        print(f"Count Operations({num1}, {num2}) = {result}")


if __name__ == "__main__":
    run_tests()