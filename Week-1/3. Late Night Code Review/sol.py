def sol(branch: str) -> str:
    seen = set()
    for c in branch:
        if c in seen:
            return c
        seen.add(c)
    return ""

assert sol("abccbd") == "c"
assert sol("abcabc") == "a"
assert sol("aabbcc") == "a"
assert sol("abcdef") == ""
assert sol("xxyz") == "x"
assert sol("z") == ""
assert sol("") == ""
assert sol("112233") == "1"
assert sol("!@#!!") == "!"
assert sol("aa") == "a"
