class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"(": ")", "[": "]", "{": "}"}
        close_to_open = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in open_to_close:
                stack.append(char)
            elif char in close_to_open:
                if not stack or stack[-1] != close_to_open[char]:
                    return False
                stack.pop()
        return not stack



if __name__ == "__main__":
    sol = Solution()

    examples = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("([{}])", True),
        ("{[()]}[]", True),
        ("{[(])}", False)
    ]

    for s, expected in examples:
        result = sol.isValid(s)
        print(f"Input: {s} -> Output: {result} (expected: {expected})")