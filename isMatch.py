def isMatch(s: str, p: str) -> bool:
        starList = []
        def starRun(sl, c):
            if c == '.' and len(sl) > 0:
                while len(sl) > 0 and sl[0].isalpha():
                    starList.append(sl.pop(0))
            elif len(sl) > 0:
                while len(sl) > 0 and sl[0] == c:
                    starList.append(sl.pop(0))

        sl = list(s)
        sp = list(p)
        index = 0
        while index < len(sp):
            if index < len(sp) - 1 and sp[index+1] == '*':
                c = sp[index] ## find index of dup char
                starRun(sl, sp[index])
                index += 1
                if len(starList) > 0 and starList[0] == sl[]
            else:
                if len(sl) > 0: 
                    if sp[index] != "." and sl[0] != sp[index]:
                        return False
                    else:
                        sl.pop(0)
                else: 
                    return False
            index += 1
        return len(sl) == 0
# print(isMatch("hhhhddd", "h*d*")) ## T
#print(isMatch("hhhhddd", ".*")) ## T
# print(isMatch("ddd", "h*d*")) ## T
# print(isMatch("hit", "h*t")) ## False
# print(isMatch("hit", "h.t")) ## T 
# print(isMatch("ddd", "d*t")) ## F
#print(isMatch("tddd", "d*")) ## F
#print(isMatch("aab", "c*a*b")) ## T 
print(isMatch("aaa", "a*a")) ## T
print(isMatch("aaa", "a*aa")) ## T
