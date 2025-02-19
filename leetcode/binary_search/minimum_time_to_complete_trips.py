from typing import List


class Solution:
    # Brute force don't work
    # def minimumTime(self, time: List[int], totalTrips: int) -> int:
    #     filtered_times_count = {}
    #     for t in time:
    #         filtered_times_count[t] = filtered_times_count.get(t, 0) + 1
    #     completed_trips = 0
    #     time_step = 0
    #     sorted_times = sorted(filtered_times_count.keys())
    #     # print(sorted_times)
    #     while completed_trips < totalTrips:
    #         time_step += 1
    #         for t in sorted_times:
    #             if time_step % t == 0:
    #                 # print(time_step, t)
    #                 completed_trips = completed_trips + filtered_times_count[t]
    #                 if completed_trips >= totalTrips:
    #                     break
    #     return time_step

    # binary search
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        max_time = max(time)
        #times = list(range(1, (max_time * totalTrips) + 1))
        low = 0
        high = (max_time * totalTrips)
        mid = 0
        last_known = mid
        num_trips = lambda x: sum([x // t for t in time])
        while low <= high:
            mid = (high + low) // 2
            curr_trip = num_trips(mid)
            if curr_trip < totalTrips:
                low = mid + 1
            elif curr_trip >= totalTrips:
                last_known = mid
                high = mid - 1
        return last_known


if __name__ == '__main__':
    print(Solution().minimumTime([5, 10, 10], 9))
"""
Accepted
Next question
2188. Minimum Time to Finish the Race
More challenges
2226. Maximum Candies Allocated to K Children
1870. Minimum Speed to Arrive on Time
2064. Minimized Maximum of Products Distributed to Any Store
"""