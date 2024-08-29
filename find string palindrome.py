str1="hi everyone Welcome"
str2="hi everyone welcome"
str1=str1.replace(" ","").lower()
str2=str2.replace(" ","").lower()
a=str1[::-1]
b=str2[::-1]
if a==b:
    print(" palindrome")
else:
    print("not palindrome")




""""""""""""""





def is_palindrome(s):
    """
    Function to check whether a string is a palindrome or not.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    return s == s[::-1]


# Example usage:
string = "A man a plan a canal Panama"
if is_palindrome(string):
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')

