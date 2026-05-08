def EvenNumbers():
    num=0
    while True:
        yield num
        num+=2

even=EvenNumbers()

for num in even:
        if num==1000:
            break
        print(num,end=' ')