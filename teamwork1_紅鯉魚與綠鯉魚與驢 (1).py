print('在政大午餐想吃什麼')
x=int(input("有幾個人要吃飯？(請輸入一個整數)"))
y=input("地點在大門左右？(請左或右)")
z=float(input("想走幾分鐘？(請輸入一個整數)"))
u=input("可接受價格？a=100元以下 b=100元以上(請輸入a或b)")

if x==1 and y=="左"and z<=5 and u=='a':
    print('小木屋,八方雲集,MY麵屋,菁英自助餐')
if x>1 and y=="左"and z<=5 and u=='a':
    print('小木屋,八方雲集,MY麵屋')
if x==1 and y=="左"and z<=5 and u=='b':
    print('波波恰恰')
if x>1 and y=="左"and z<=5 and u=='b':
    print('波波恰恰,四川')
if x==1 and y=="左"and z>5 and u=='a':
    print('京華小館')
if x>1 and y=="左"and z>5 and u=='a':
    print('四五大街')
if x==1 and y=="左"and z>5 and u=='b':
    print('蘭亭')
if x>1 and y=="左"and z>5 and u=='b':
    print('里克')
if x==1 and y=="右"and z<=5 and u=='a':
    print('愛心滷味,佳味自助餐,左撇子,悅來麵館')
if x>1 and y=="右"and z<=5 and u=='a':
    print('左撇子,悅來')
if x==1 and y=="右"and z<=5 and u=='b':
    print('豚將')
if x>1 and y=="右"and z<=5 and u=='b':
    print('滇味廚房,大呼過癮')
if x==1 and y=="右"and z>5 and u=='a':
    print('秀食屋')
if x>1 and y=="右"and z>5 and u=='a':
    print('華越')
if x==1 and y=="右"and z>5 and u=='b':
    print('金鰭')    
if x>1 and y=="右"and z>5 and u=='b':
    print('朴媽媽,金鰭')
