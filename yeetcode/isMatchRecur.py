def isMatch(s: str, p: str) -> bool:
    sl = list(s)
    sp = list(p)
    index = 0
    result = False
    while index < len(sp):
        if index < len(sp) - 1:
            if sp[index+1] == '*':
                isMatch(s, p[2:])
                ns = sl.copy()
                if sp[0] != sl[0]:
                    return False
                while len(ns) != 0 and ns[0] == sp[index]:
                    ns = ns[1:]
                    isMatch(ns, p[2:])
                index += 1
            # elif sp[index] != sl
    if len(sl) == 0:
        return True
    else:    
        return False

print(isMatch("hhhhddd", "h*d*")) ## T
# print(isMatch("hhhhddd", ".*")) ## T
# print(isMatch("ddd", "h*d*")) ## T
# print(isMatch("hit", "h*t")) ## False
# print(isMatch("hit", "h.t")) ## T
# print(isMatch("ddd", "d*t")) ## F
# print(isMatch("tddd", "d*")) ## F
# print(isMatch("aab", "c*a*b")) ## T
# print('break')
# print(isMatch("aaa", "a*a")) ## T
# print(isMatch("aaa", "a*aa")) ## T
# print(isMatch("aaca", "ab*a*c*a")) ## T
# print(isMatch("aaa", "ab*a*c*a")) ## T
# print(isMatch("bbbba", ".*a*a")) ## T
# print(isMatch("ab", ".*..")) ## T
# print(isMatch("mississippi", "mis*is*ip*."))## T
# print(isMatch("abbbcd", "ab*bbbcd"))##T
print(isMatch("abcdede", "ab.*de"))##T
print(isMatch("aaa", "aaaa"))##F
print(isMatch("aabcbcbcaccbcaabc", ".*a*aa*.*b*.c*.*a*"))##T
