# 30 Common String Tools and Functions

# 1. Concatenation
string1 = "Hello, "
string2 = "World!"
result = string1 + string2
print("1. Concatenation:", result)

# 2. Length of a string
string = "Python is great!"
length = len(string)
print("2. Length of the string:", length)

# 3. String slicing
substring = string[7:10]
print("3. Sliced substring:", substring)

# 4. String formatting
name = "Alice"
age = 30
formatted_string = f"4. My name is {name} and I am {age} years old."
print("Formatted string:", formatted_string)

# 5. String methods
text = "   This is some text with spaces.   "
stripped_text = text.strip()
print("5. Stripped text:", stripped_text)

uppercase_text = text.upper()
print("6. Uppercase text:", uppercase_text)

lowercase_text = text.lower()
print("7. Lowercase text:", lowercase_text)

# 8. Searching in a string
sentence = "Python is a powerful programming language."
keyword = "Python"
if keyword in sentence:
    print(f"8. '{keyword}' found in the sentence.")
else:
    print(f"8. '{keyword}' not found in the sentence.")

# 9. Replacing in a string
original_text = "I like apples, but I also like bananas."
replaced_text = original_text.replace("apples", "oranges")
print("9. Replaced text:", replaced_text)

# 10. Counting occurrences
count = original_text.count("like")
print("10. Count of 'like':", count)

# 11. Splitting a string
words = original_text.split()
print("11. Split words:", words)

# 12. Joining a list of strings
words = ["I", "like", "coding"]
joined_text = " ".join(words)
print("12. Joined text:", joined_text)

# 13. Checking if a string starts with a prefix
if original_text.startswith("I like"):
    print("13. The string starts with 'I like'.")

# 14. Checking if a string ends with a suffix
if original_text.endswith("bananas."):
    print("14. The string ends with 'bananas.'")

# 15. Finding the index of a substring
index = original_text.find("also")
print("15. Index of 'also':", index)

# 16. Checking if a string contains only digits
numeric_string = "12345"
is_numeric = numeric_string.isdigit()
print(f"16. Is '{numeric_string}' numeric?: {is_numeric}")

# 17. Checking if a string contains only alphabetic characters
alphabetic_string = "Python"
is_alphabetic = alphabetic_string.isalpha()
print(f"17. Is '{alphabetic_string}' alphabetic?: {is_alphabetic}")

# 18. Checking if a string is in title case
title_case_string = "Title Case Example"
is_title_case = title_case_string.istitle()
print(f"18. Is '{title_case_string}' in title case?: {is_title_case}")

# 19. Converting a string to a list of characters
char_list = list(original_text)
print("19. List of characters:", char_list)

# 20. Reversing a string
reversed_text = original_text[::-1]
print("20. Reversed text:", reversed_text)

# 21. Checking if a string is empty
empty_string = ""
is_empty = len(empty_string) == 0
print("21. Is the string empty?:", is_empty)

# 22. Removing leading and trailing whitespace
whitespace_text = "   Some spaces around   "
stripped_whitespace = whitespace_text.strip()
print("22. Stripped whitespace:", stripped_whitespace)

# 23. Checking if a string contains a substring
substring_to_check = "coding"
contains_substring = substring_to_check in original_text
print(f"23. Does the string contain '{substring_to_check}'?: {contains_substring}")

# 24. Checking if a string is a valid identifier
identifier = "my_variable_123"
is_valid_identifier = identifier.isidentifier()
print(f"24. Is '{identifier}' a valid identifier?: {is_valid_identifier}")

# 25. Capitalizing the first letter of a string
name = "john doe"
capitalized_name = name.capitalize()
print("25. Capitalized name:", capitalized_name)

# 26. Checking if a string is in lowercase
is_lowercase = name.islower()
print(f"26. Is '{name}' in lowercase?: {is_lowercase}")

# 27. Checking if a string is in uppercase
is_uppercase = name.isupper()
print(f"27. Is '{name}' in uppercase?: {is_uppercase}")

# 28. Checking if a string contains only whitespace characters
whitespace_only = "   \t  \n"
is_whitespace_only = whitespace_only.isspace()
print(f"28. Is '{whitespace_only}' whitespace only?: {is_whitespace_only}")

# 29. Repeating a string
repeated_string = "abc" * 3
print("29. Repeated string:", repeated_string)

# 30. Checking if a string ends with any of a list of suffixes
suffixes = [".jpg", ".png", ".gif"]
filename = "image.jpg"
ends_with_any = filename.endswith(tuple(suffixes))
print(f"30. Does '{filename}' end with any of {suffixes}?: {ends_with_any}")