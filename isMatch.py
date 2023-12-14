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
                starRun(sl, sp[index])
                index += 1
                while index < len(sp) - 1 and len(starList) > 0 and sp[index+1] in starList:
                    if sp[index+1] in sl or sp[index+1] =='.':
                        break
                    i = starList.index(sp[index+1])
                    maxAdd = 0
                    k = index+1 
                    for j in range(i, len(starList)):
                        if j + maxAdd < len(sp)-1 and k < len(sp):
                            if starList[j] == sp[k]:
                                maxAdd +=1
                                k+=1
                            else:
                                maxAdd = 0
                        else:
                            break
                    index += maxAdd
                    # if (starList[0] == sp[index+1] or sp[index+1] == '.') and index < len(sp) - 2 and sp[index+2] == '*':
                    #     index+=2
                    # elif starList[0] == sp[index+1] or sp[index+1] == '.':
                    #     starList.pop(0)
                    #     if sp[index+1] != '.' or len(sl) == 0:
                    #         index+=1
                    break
            else:
                if len(sl) > 0: 
                    if sp[index] != "." and sl[0] != sp[index]:
                        return False
                    else:
                        sl.pop(0)
                        starList.clear()
                else: 
                    return False
            index += 1
        return len(sl) == 0

# print(isMatch("hhhhddd", "h*d*")) ## T
# print(isMatch("hhhhddd", ".*")) ## T
# print(isMatch("ddd", "h*d*")) ## T
# print(isMatch("hit", "h*t")) ## False
# print(isMatch("hit", "h.t")) ## T 
# print(isMatch("ddd", "d*t")) ## F
# print(isMatch("tddd", "d*")) ## F
# print(isMatch("aab", "c*a*b")) ## T 
# print(isMatch("aaa", "a*a")) ## T
# print(isMatch("aaa", "a*aa")) ## T
# print(isMatch("aaca", "ab*a*c*a")) ## T
# print(isMatch("aaa", "ab*a*c*a")) ## T
print(isMatch("bbbba", ".*a*a")) ## T
print(isMatch("ab", ".*..")) ## T
# print(isMatch("mississippi", "mis*is*ip*."))## T
# print(isMatch("abbbcd", "ab*bbbcd"))##T
# print(isMatch("abcdede", "ab.*de"))##T