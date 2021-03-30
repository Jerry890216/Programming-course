import random
def check_type(num):
    try:
        int(num)
    except ValueError:   
        result=False                   #有發生例外時，將變數result的內容設為False
    else:
        result=True                  #沒有發生例外時，將變數result的內容設為True
    finally:
        return result
while True:
    print('歡迎來到酒吧app，若想使用查詢功能請按1，若想嘗試酒吧知識王請按2，若想結束程式請按0')
    choice=input('你想使用的功能是:')
    if choice=='1':
        name=['文山區','中正區','信義區','大安區','都可以']
        price2=['200-300','300-400','400以上','都可以']
        style2=['多人聚會','少人小酌','都可以']

        file=open('酒吧資料新.txt','r',encoding='utf-8')
        line=file.readlines()
        file.close

        line2=[]
        for x in line:
                line2.append(x.strip().split(','))
        
        area=input('一、請輸入想要的地區:(1)文山區(2)中正區(3)信義區(4)大安區(5)都可以 :')
        while True:
            if check_type(area):
                area1=int(area)
                if area1 not in range(1,6):
                    area=input('請依正確格式重新輸入:')
                else:
                    area_name=name[int(area)-1]
                    break
            else:
                area=input('請依正確格式重新輸入:')
        price=input('二、請輸入想要的價格區間:(1)200~300(2)300~400(3)400以上(4)都可以 :')
        while True:
            if check_type(price):
                price1=int(price)
                if price1 not in range(1,5):
                    price=input('請依正確格式重新輸入:')
                else:
                    price_name=price2[int(price)-1]
                    break
            else:
                price=input('請依正確格式重新輸入:')
        style=input('三、喜歡的酒吧風格是 (1)多人聚會(2)少人小酌(3)都可以 :')
        while True:
            if check_type(style):
                style1=int(style)
                if style1 not in range(1,4):
                    style=input('請依正確格式重新輸入:')
                else:
                    style_name=style2[int(style)-1]
                    break
            else:
                style=input('請依正確格式重新輸入:')

        a=[]
        b=[]
        c=[]
        for i in line2:    
            if area=='5':
                a.append(i)                    
            elif i[0]==area_name:
                a.append(i)
        for x in a:
            if price=='4' :
                b.append(x)
            elif x[6]==price_name:
                b.append(x)
        for y in b:
            if style=='3':
                c.append(y)
            elif y[5]==style_name:
                c.append(y)
        if c==[]:
            print('查無符合條件的酒吧')
        else:
            for z in c:
                print('店名:',z[1],'\n特色酒品:',z[2],'\nGoogle星數:',z[3],'\n交通方式:',z[4],'\n')
    elif choice=='2':
        Question=[]
        ANswer=[]
        file=open('酒精資料庫.txt','r',encoding='utf-8')
        list_line=file.readlines()
        file.close()

        for i in list_line:
            hold=i.strip().split(',')
            Question.append(hold[0])
            ANswer.append(hold[1])
            
        correct=0
        for n in range(1,11):
            Y=0
            Q=random.randint(1,36-Y)
            ele=Question.pop(Q)
            ele1=ANswer.pop(Q)
            A=random.sample(ANswer,k=3)
            Y+=1
    
            print('第',n,'題:',ele)
            A.insert(Q%4,ele1)
            for i in range(4):
                print(i+1,A[i],end=' ')

            Answer=input(',請輸入答案(請輸入1~4):')
            while True:
                if check_type(Answer):
                    Answer1=int(Answer)
                    if Answer1 not in range(1,5):
                        Answer=input('請依正確格式重新輸入:')
                    else:
                        break
                else:
                    Answer=input('請依正確格式重新輸入:')
            if int(Answer)==Q%4+1:
                print('恭喜你/妳答對了!')
                correct+=1
            else:
                print("答錯了!正確答案是",ele1)
        print('恭喜你/妳答對了',correct,"題")

    elif choice=='0':
        break

