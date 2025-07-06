import re

def is_valid_email(email:str) -> bool:
    if not isinstance(email, str) or not email:
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None



# ^ — start of string

# [\w\.-]+ — one or more (+) of:

# \w → word characters (a-z, A-Z, 0-9, and _)

# . or - → period or hyphen

# @ — literal @ symbol

# [\w\.-]+ — same as above: domain name part

# \. — literal . before the top-level domain (like .com)

# \w+ — one or more word characters for the top-level domain

# $ — end of string