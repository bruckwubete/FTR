# class Solution:
#     def max_unique_split(self, s: str) -> int:
#         sub_strings = {}
#         current_char = ''
#         length = 0
#         for c in s:
#             c = current_char + c
#             if sub_strings.get(c):
#                 current_char = c
#                 continue
#             else:
#                 length += 1
#                 current_char = ''
#                 sub_strings[c] = 1
#         return length
class Solution:
    sub_strings = {}

    def max_unique_split(self, s: str) -> int:
        maxm = 0

        # Iterate over the characters of the string
        for i in range(1, len(s) + 1):

            # Stores prefix substring
            tmp = s[0:i]

            # Check if the current substring
            # already exists
            if (tmp not in self.sub_strings):
                # Insert tmp into set
                self.sub_strings[tmp] = 1

                # Recursively call for remaining
                # characters of string
                maxm = max(maxm, self.max_unique_split(s[i:]) + 1)
                print(self.sub_strings)
                # Remove from the set
                del self.sub_strings[tmp]
        return maxm


if __name__ == '__main__':
    s = Solution()
    #s.max_unique_split("wwwzfvedwfvhsww")
    print(s.max_unique_split("www"))
    #print(s.sub_strings)
