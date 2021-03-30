


#1.匯入資料庫
#2 中英各一串
#3 英文中找一個單字
#4 sample找三個中文
#5 餘數決定ABCD
#6 計算得分 10題OVER 人生只有一次

import random
English=[]
Chinese=[]
file=open('英文單字資料庫.txt','r',encoding='utf-8')
list_line=file.readlines()
file.close()



for i in list_line:
    hold=i.strip().split(',')
    
    English.append(hold[0])
    Chinese.append(hold[1])


correct=0
for n in range(1,11):
    Y=0
    Q=random.randint(1,199-Y)
    ele=English.pop(Q)
    ele1=Chinese.pop(Q)
    A=random.sample(Chinese,k=3)
    Y+=1
    
    print('第',n,'題:',ele)
    A.insert(Q%4,ele1)
    for i in range(4):
        print(i+1,A[i],end=' ')

    Answer=input(',請輸入答案(請輸入1~4):')
    if int(Answer)==Q%4+1:
        print('恭喜你/妳答對了!')
        correct+=1
    else:
        print("答錯了!正確答案是",ele1)
print('恭喜你/妳答對了',correct,"題")

