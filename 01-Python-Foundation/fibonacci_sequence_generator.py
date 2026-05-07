def Fibonacci_Sequence():
    x=0
    y=1    
    while True:
        yield x
        x,y=y,x+y


fibo=Fibonacci_Sequence()

cou=0
for num in fibo:
    if cou== 10:
        break
    print(num,end=' ')
    cou+=1 
