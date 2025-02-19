class Solution:
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        idx = len(list(s))
        result = 0
        for i in range(idx - 1, -1, -1):
            current_val = s[i]
            if result != 0 and self.roman_values.get(current_val, 0) < self.roman_values.get(s[i + 1], 0):
                result -= self.roman_values.get(current_val, 0)
            else:
                result += self.roman_values.get(current_val, 0)
        return result


if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt("III"))
    print(a.romanToInt("XIV"))
