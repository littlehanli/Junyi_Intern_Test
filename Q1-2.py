'''Jun Yi Academy'''

### Q1. ###
def reverseString(in_str):
    out_str = ''
    for i in range(len(in_str)-1,-1,-1):
        out_str += in_str[i]
    return out_str

def reverseVoc(in_str):
    list_str = in_str.split(' ')
    out_str = ''
    for i,item in enumerate(list_str):
        out_str += reverseString(item)
        if i < len(list_str)-1:
            out_str += ' '
    return out_str
    
#s1 = 'junyiacademy'
s1 = input('Q1-1. 請輸入一段英文字串\n')
print(reverseString(s1))
#s2 = 'flipped class room is important'
s2 = input('Q1-2.請輸入一段英文句子\n')
print(reverseVoc(s2))



### Q2. ###
def primeFactor(n):
    factor = list(range(1,n+1))
    remove = []
    for i in range(len(factor)):
        if (factor[i]%3 == 0 or factor[i]%5 == 0) and not (factor[i]%3 == 0 and factor[i]%5 == 0):
            remove.append(factor[i])
    out_list = list(set(factor).difference(set(remove)))
    return len(out_list)
    
#n = 15
n = int(input('Q2. 請輸入一個數字\n'))
print(primeFactor(n))