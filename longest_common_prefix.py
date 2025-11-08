from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]

        for i in range(1, len(strs)):
                    word = strs[i]
                    for j in range(len(prefix)):
                        if j >= len(word) or prefix[j] != word[j]:
                            prefix = prefix[:j]
                            break
        return prefix
    
if __name__ == "__main__":
    sol = Solution()

    examples = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["throne", "throne"], "throne"),
        (["a"], "a"),
        (["", ""], ""),
        (["prefix", "pre"], "pre")
    ]

    for strs, expected in examples:
        result = sol.longestCommonPrefix(strs)
        print(f"Input: {strs}")
        print(f"Output: '{result}' (expected: '{expected}')")
