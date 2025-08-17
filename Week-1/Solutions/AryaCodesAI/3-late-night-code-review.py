# Late Night Code Review Solution
# Find the first duplicate feature flag that triggers a "wait..." moment

# Read the feature flag sequence
flags = input().strip()

# Track seen flags and find first duplicate
seen = set()
for flag in flags:
    if flag in seen:
        print(flag)
        break
    seen.add(flag)
