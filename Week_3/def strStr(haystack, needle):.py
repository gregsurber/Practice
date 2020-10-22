# Compare string values to determine if string2 exists within string1

def strStr(haystack, needle):
    haystack_length = len(haystack)
    needle_length = len(needle)
    if haystack_length < needle_length: 
        print("The first string you enter must be at least as long as the second.")
    else:
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
    return 0


# Get input for two strings from user
print("Let's see if a string of characters (the 'needle') exists inside another string of characters (the 'haystack')!")
haystack = input("What haystack would you like to look in? ")
needle = input("Now, what needle would you like to look for inside that haystack? ")

# Get the rsult of the function
result = strStr(haystack, needle)

# If the function is able to find the given needle inside the haystack, print its location.
# If it is not able to find it, tell the user the string could not be found.
if result == 0:
    print("That needle could not be found inside the haystack, sorry.")
else:
    print(f"That particular needle can be found starting at index {strStr(haystack, needle)} of the haystack.")


