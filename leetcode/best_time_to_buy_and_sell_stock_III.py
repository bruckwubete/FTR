from typing import List
import sys

def maxProfit(self, prices: List[int]) -> int:
    fs = ss = 0
    fb = sb = ~sys.maxsize
    for i in prices:
        fb = max(fb, -1 * i)
        fs = max(fs, fb + i)
        sb = max(sb, fs - i)
        ss = max(ss, sb + i)
    return ss
