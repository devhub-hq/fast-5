# Problem 3: Late Night Code Review

## Problem Statement
Find the first character that appears twice in a string.

## Approach
**Hash Set Tracking**
- Use a set to track seen characters
- Return first character found in the set

## Logic
```
String: "abccbd"
Process:
- 'a': not seen → add to set
- 'b': not seen → add to set  
- 'c': not seen → add to set
- 'c': already in set → return 'c'
```

## Time Complexity: O(n)
## Space Complexity: O(k) where k is unique characters

## Alternative Approaches
- Nested loops: O(n²) time, O(1) space
- Character counting: O(n) time, O(k) space