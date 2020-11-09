# Problem 2: Valid Anagram
# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:	Input: s = "anagram", t = "nagaram"		Output: true
# Example 2:	Input: s = "rat", t = "car"			Output: false
# Note: You may assume the string contains only lowercase alphabets.

# create two variables to hold the strings to compare
s = "aNagram"
t = "nagaram"

# convert both strings to all lower czse, in case mixed case values are input
s = s.lower()
t = t.lower()

# sort each variable so that all letters are arranged alphabetically
sort_s = sorted(s)
sort_t = sorted(t)

# compare the two sorted strings. If they are the same, then they are an anagram.
if sort_s == sort_t:
    print(f"The strings {s} and {t} are anagrams!")
else:
    print(f"The strings {s} and {t} are NOT anagrams!")



# Follow up: What if the inputs contain unicode characters? How would you adapt your solution to such case?

