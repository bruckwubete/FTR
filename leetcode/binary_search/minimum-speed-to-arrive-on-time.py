import math
from typing import List


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        num_trains = len(dist)
        num_hours = lambda x: sum([math.ceil(i / x) for i in dist[:-1]]) + dist[-1] / x
        if hour < num_hours(max(dist) * 100):
            return -1
        max_speed = max(dist) * 100
        min_speed = 1
        last_answer = min_speed
        while min_speed <= max_speed:
            k = (max_speed + min_speed) // 2
            if num_hours(k) <= hour:
                max_speed = k - 1
                last_answer = k
            else:
                min_speed = k + 1
        return last_answer


if __name__ == '__main__':
    print(Solution().minSpeedOnTime([1, 3, 2], 6))

"""
1871. Jump Game VII
More challenges
1883. Minimum Skips to Arrive at Meeting On Time
2332. The Latest Time to Catch a Bus
2439. Minimize Maximum of Array
"""
