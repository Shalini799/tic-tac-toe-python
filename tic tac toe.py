def display_board(l):
        print(l[6],"|",l[7],"|",l[8],"|")
        print("---------")
        print(l[3],"|",l[4],"|",l[5],"|")
        print("---------")
        print(l[0],"|",l[1],"|",l[2],"|")
def player():
        print("Enter player 1 marker: X or O")
        marker1=input()
        print("Enter player 2 marker:X or O")
        marker2=input()
        return marker1,marker2   
def guess():
        print("Player 1 enter where you want to place:")
        k=int(input())
        print("Player 2 enter where you want to place:")
        j=int(input())
        return k,j
def replace(l,marker1,marker2):
    ch=True
    while ch:
       k,j=guess()
       l[k]=marker1
       l[j]=marker2
       display_board(l)
       if contin().upper()=='N':
           ch=False
    return l
def contin():
    print("Do you want to continue: Y or N")
    choice=input()
    return choice
def result():
    j=''
    for i in l:
        if i==0 or i==3 or i==6:
           if l[i]==l[i+1]==l[i+2]:
              j=l[i]
        if i==6 or i==7 or i==8:
           if l[i]==l[i+3]==l[i+6]:
              j=l[i]
        if i==0:
           if l[i]==l[i+2]==l[i+4]:
              j=l[i]
        if i==2:
           if l[i]==l[i+4]==l[i+8]:
              j=l[i]
    if l[j]=='X':
        print("player 1 won the game")
    elif l[j]=='O':
        print("player 2 won the game")
    else:
        print("its a tie")
l=['','','','','','','','','']
marker1,marker2=player()
replace(l,marker1,marker2)
result()
        
