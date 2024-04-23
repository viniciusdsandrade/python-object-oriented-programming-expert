# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:

    @staticmethod
    def addBinary2(a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]

    @staticmethod
    def addBinary(a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            res.append(str(carry % 2))
            carry //= 2
        return ''.join(res[::-1])


def test():
    a = "11"
    b = "1"
    s = Solution()
    print(f"{a} + {b} = {s.addBinary(a, b)}")
    print(f"{a} + {b} = {s.addBinary2(a, b)}")

    a = "1010"
    b = "1011"
    s = Solution()
    print(f"{a} + {b} = {s.addBinary(a, b)}")
    print(f"{a} + {b} = {s.addBinary2(a, b)}")


if __name__ == '__main__':
    test()
