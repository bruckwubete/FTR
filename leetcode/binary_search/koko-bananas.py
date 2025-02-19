import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)
        min_speed = 1
        k = max_speed
        last_known = k
        while min_speed <= max_speed:
            # print(min_speed, k, max_speed)
            k = (max_speed + min_speed) // 2

            hours = sum([math.ceil(i / k) for i in piles])
            # print(hours)
            if hours <= h:
                max_speed = k - 1
                last_known = k
            else:
                min_speed = k + 1
            # print('end', min_speed, k, max_speed)
        return last_known


if __name__ == '__main__':
    print(Solution().minEatingSpeed([30, 11, 23, 4, 20], 5))
"""
876. Middle of the Linked List
More challenges
774. Minimize Max Distance to Gas Station
2064. Minimized Maximum of Products Distributed to Any Store
2498. Frog Jump II
"""