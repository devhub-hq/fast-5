def find_first_duplicate(feature_flags):
    seen = set()
    for flag in feature_flags:
        if flag in seen:
            return flag
        seen.add(flag)
    return None

if __name__ == "__main__":
    flags = "abccbd"
    result = find_first_duplicate(flags)
    print(result)
