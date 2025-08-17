def first_duplicate_char(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None

print(first_duplicate_char("abccbd"))