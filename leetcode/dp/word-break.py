# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         # wordDict = sorted(wordDict, key = lambda x: len(x))
#         # for w in wordDict:
#         #     s = s.replace(w, '')
#         # return s == ''
#         compleIdx = 0
#         for i in range(len(s)):
#             if s[compleIdx:i+1] in wordDict:
#                 compleIdx = i + 1
#         return compleIdx == len(s)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        queue = deque([0])
        seen = set()

        while queue:
            start = queue.popleft()
            if start == len(s):
                return True

            for end in range(start + 1, len(s) + 1):
                if end in seen:
                    continue

                if s[start:end] in words:
                    queue.append(end)
                    seen.add(end)

        return False