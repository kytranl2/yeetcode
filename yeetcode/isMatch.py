def isMatch(s: str, p: str) -> bool:
    ptotal = 0
    sl = list(s)
    sp = list(p)
    stotal = 0
    pdict = {}
    sdict = {}

    for c in s:
        if c not in sdict:
            sdict[c] = 1
        else:
            sdict[c] += 1 
        stotal += 1
    
    for index in range(len(sp)):
        if sp[index] == '*':
            continue
        # or (index < len(sp) - 1 and sp[index+1] == '*')
        else:
            c = sp[index]
            if c not in pdict:
                pdict[c] = 1
            else:
                pdict[c] += 1
            ptotal +=1

    hasP = False
    def starRun(sl, c):
        nonlocal stotal
        nonlocal ptotal
        if c == '.' and len(sl) > 0:
            while len(sl) > 0 and sl[0].isalpha():
                if stotal > ptotal:
                    sl.pop(0)
                    stotal -= 1
                else:
                    break
        elif len(sl) > 0:
            while len(sl) > 0 and sl[0] == c:
                if stotal > ptotal:
                    sl.pop(0)
                    stotal -= 1
                else:
                    break
    index = 0
    while index < len(sp):
        if index < len(sp) - 1 and sp[index+1] == '*':
            starRun(sl, sp[index])
            index += 1
        else:
            if len(sl) > 0:
                if sp[index] != "." and sl[0] != sp[index]:
                    break
                else:
                    sl.pop(0)
                    stotal -= 1
                    ptotal -= 1
            else: 
                hasP = True   
        index += 1

    if len(sl) == len(s):
        return False
    elif len(sl) > 0:
        return False
    elif hasP:
        return False
    else:
        return True

# print(isMatch("hhhhddd", "h*d*")) ## T
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
