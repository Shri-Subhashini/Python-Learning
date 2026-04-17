import re

text = "User logged in with email support@example.com at 10AM"

match = re.search(r"\w+@\w+\.\w+", text)

if match:
    print("Found email:", match.group())


print(re.findall("[aeiou]", "education"))
print(re.findall("a+", "caaaab"))

text = "abc123y7ww23"
match = re.search("([a-z]+)(\d+)", text)
print(match.groups())


print(re.findall("(?:cat|dog)", "cat dog"))