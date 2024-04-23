class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        if not s: return 0
        if len(s) == 1: return 1
        max_len = 0
        start = 0
        end = 0
        while end < len(s):
            if s[end] in s[start:end]:
                start += 1
            else:
                end += 1
                max_len = max(max_len, end - start)
        return max_len


def main():
    s = "abcabcbb"
    print(s)
    result = Solution.lengthOfLongestSubstring(s)
    print(result)

    s = "bbbbb"
    print(s)
    result = Solution.lengthOfLongestSubstring(s)
    print(result)

    s = "pwwkew"
    print(s)
    result = Solution.lengthOfLongestSubstring(s)
    print(result)

    s = ""
    print(s)
    result = Solution.lengthOfLongestSubstring(s)
    print(result)

    s = " "
    print(s)
    result = Solution.lengthOfLongestSubstring(s)
    print(result)

    s = "au"
    print(s)
    result = Solution.lengthOfLongestSubstring(s)
    print(result)


if __name__ == '__main__':
    main()
