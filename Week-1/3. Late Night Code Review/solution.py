def first_repeat(s):
    seen = set()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return None  # In case no repeat is found

if __name__ == "__main__":
    s = input().strip()
    result = first_repeat(s)
    if result:
        print(result)
    else:
        print("No repetition")
