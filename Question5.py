# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# ------Solution----

class Solution:
  
  def longestCommonPrefix(self, list):
    if not list:
     return "empty"
    list.sort()

    first=list[0]
    last=list[-1]

    i=0
    while i<len(first) and i<len(last):
      if first[i]==last[i]:
        i+=1
      else:
        break
    return first[:i]
    

string=["flower","flow","flight"]
a=Solution()
print(a.longestCommonPrefix(string))

     