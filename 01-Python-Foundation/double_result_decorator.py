def Double(func):
    def wrapper():
        result=func()
        newResult=result*2
        return newResult
    return wrapper
        
@Double
def getNumber():
    return 10
    
print(getNumber())