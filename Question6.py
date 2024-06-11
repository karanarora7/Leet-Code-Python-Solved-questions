# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false

# ------Solution-----------------

class Solution:
  def isValid(self, s):
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}
    # Stack to keep track of opening brackets
    stack = []
  
    # Iterate through each character in the string
    for char in s:
        # If it's an opening bracket, push it onto the stack
        if char in bracket_map.values():
            stack.append(char)
        # If it's a closing bracket
        elif char in bracket_map:
            # Check if the stack is not empty and if the top of the stack matches the corresponding opening bracket
            if not stack or bracket_map[char] != stack.pop():
                return False
  
    # If the stack is empty, all opening brackets were properly matched and closed
    return not stack
a=Solution()
# Examples
print(a.isValid("()"))      # Output: true
print(a.isValid("()[]{}"))  # Output: true
print(a.isValid("(]"))      # Output: false