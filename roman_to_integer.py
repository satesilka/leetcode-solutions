acceptable_chars = ["I", "V", "X", "L", "C", "D", "M"]
roman_map= { "I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL":40,  "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500, "CM":900, "M": 1000}

class Solution:
    def validation(self, s:str) -> int:
        if not (1 <= len(s) <= 15 and all(ch in acceptable_chars for ch in s)):
            print("Error")
            return False
        return True


    def romanToInt(self, s: str) -> int:
        count = 0 
        i = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] in roman_map:
                count += roman_map[s[i:i+2]]
                i += 2
            else:
                count += roman_map[s[i]]
                i += 1
        return count
    

if __name__ == "__main__":
    sol = Solution()

    test_cases = {
        "III": 3,        
        "IV": 4,         
        "IX": 9,         
        "LVIII": 58,     
        "MCMXCIV": 1994, 
        "XLII": 42,      
        "XC": 90,        
        "CDXLIV": 444,   
        "MMXXV": 2025,   
    }

    for roman, expected in test_cases.items():
        result = sol.romanToInt(roman)
        print(f"{roman:10} -> {result:5} ")
