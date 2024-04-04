def isMatch(s: str, p: str) -> bool:
    # dp[i][j] will be True if first i characters in s match the first j characters in p
    dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

    # Empty string and empty pattern are a match
    dp[0][0] = True

    # Handles patterns like a* or a*b* or a*b*c* etc.
    for j in range(2, len(p) + 1):
        dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'

    # Fill dp table
    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                # Match 0 or more of the previous element
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            else:
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

    return dp[-1][-1]

# Testing the provided examples
test_cases = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True)
]

results = [(s, p, isMatch(s, p) == expected) for s, p, expected in test_cases]
print(results)
print(isMatch("hhhhddd", "h*d*")) ## T
print(isMatch("hit", "h*t")) ## False
print(isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))##T