class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # one string Python solution
        #return haystack.find(needle) if needle in haystack else -1

        n = len(haystack)
        m = len(needle) 

        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()

    tests = [
        ("sadbutsad", "sad"),
        ("leetcode", "leeto"),
        ("hello", "ll"),
        ("aaaaa", "bba"),
        ("mississippi", "issi"),
        ("abc", ""),
    ]

    for haystack, needle in tests:
        result = s.strStr(haystack, needle)
        print(f"haystack='{haystack}', needle='{needle}' → {result}")