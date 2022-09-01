class Solution:
    def convert(self, s: str, numRows: int) -> str:
        r = []
        index = 0
        
        while (index < len(s)):
            r.append(list(s[index:(index + numRows)]))
            index += numRows
            for i in range(numRows - 2):
                if index < len(s):
                    prefix = [" "] * (i + 1)
                    prefix.append(s[index])
                    prefix.extend([" "] * (numRows - (i + 2)))
                    r.append(list(reversed(prefix)))
                    index += 1 
        if len(r[-1]) < numRows:
            r[-1].extend([' '] * (numRows - len(r[-1])))
        
        s = ""
        for j in range(numRows):
            k = ""
            for i in range(len(r)):
                k += r[i][j]
                if r[i][j] != " ":
                    s += r[i][j]
            # print(k + '\n')
        return s
            
                
if __name__ == '__main__':
    print(Solution().convert("PAYPALISHIRING", 4))