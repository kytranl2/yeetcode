def isMatch(s: str, p: str) -> bool:
        def starRun(sl, c):
            if c == '.' and len(sl) > 0:
                while len(sl) > 0 and sl[0].isalpha():
                    sl.pop(0)
            elif len(sl) > 0:
                while len(sl) > 0 and sl[0] == c:
                    sl.pop(0)
        sl = list(s)
        sp = list(p)
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
            index += 1

        slr = list(s)
        slr.reverse()
        spr = list(p)
        spr.reverse()
        index = 0
        while index < len(spr):
            if index < len(spr) - 1 and spr[index] == '*':
                starRun(slr, spr[index+1])
                index += 1
            else:
                if len(slr) > 0:
                    if spr[index] != "." and slr[0] != spr[index]:
                        break
                    else:
                        slr.pop(0)
            index+=1
        if len(sl) == len(s) or len(slr) == len(s):
            return False
        elif len(sl) > 0 and len(slr) > 0:
            return False
        else:
            return True

print(isMatch("hhhhddd", "h*d*")) ## T
print(isMatch("hhhhddd", ".*")) ## T
print(isMatch("ddd", "h*d*")) ## T
print(isMatch("hit", "h*t")) ## False
print(isMatch("hit", "h.t")) ## T
print(isMatch("ddd", "d*t")) ## F
print(isMatch("tddd", "d*")) ## F
print(isMatch("aab", "c*a*b")) ## T
print('break')
print(isMatch("aaa", "a*a")) ## T
print(isMatch("aaa", "a*aa")) ## T
print(isMatch("aaca", "ab*a*c*a")) ## T
print(isMatch("aaa", "ab*a*c*a")) ## T
print(isMatch("bbbba", ".*a*a")) ## T
print(isMatch("ab", ".*..")) ## T
print(isMatch("mississippi", "mis*is*ip*."))## T
print(isMatch("abbbcd", "ab*bbbcd"))##T
print(isMatch("abcdede", "ab.*de"))##T