# 20. Valid Parentheses
# Given a string 's' containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'

            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


def test_solution(is_valid):
    # Dicionário expandido de casos de teste com os resultados esperados
    test_cases = {
        "()": True,
        "()[]{}": True,
        "(]": False,
        "([)]": False,
        "{[]}": True,
        "{{{}}}}": False,
        "((()))": True,
        "[([])]": True,
        "[({})]": True,
        "": True,
        "([": False,
        "([]{})": True,
        "([{}])": True,
        "({[})": False,
        "(([]){})": True,
        "([)][]{}": False,
        "([]{})()[]{}": True,
        "([{}])([{}])": True,
        "([{}])[]{}": True,
        "()]": False,
        "([]{[()]})": True
    }

    # Testando cada caso
    for input_string, expected_result in test_cases.items():
        result = is_valid(input_string)
        print(
            f"Input: {input_string} | Expected: {expected_result} | Result: {result} | Test Passed: {result == expected_result}")


def main(is_valid):
    test_solution(is_valid)


if __name__ == "__main__":
    main(isValid)
