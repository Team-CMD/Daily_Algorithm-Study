'''
#민준
string = input()

for i in range(97,123):
    print(string.find(chr(i)), end=" ")



#형순
Word = input()
Word = list(str(Word))
Alp = [-1]*26

# a = 97 ~ (- 97)
for i in range (len(Word)):
    index = ord(Word[i]) - 97 
    if(Alp[index] == -1):
        Alp[index] = i

for i in range (len(Alp)):
    print(Alp[i], end = ' ')
'''
#승현
def check(l:list):
    for i in range(97,123):
        if chr(i) in l:
            print(l.index(chr(i)), end=' ')

        else:
            print("-1",end=' ')

if __name__=="__main__":
    S = list(input())
    check(S)

#

    

        

        
        

