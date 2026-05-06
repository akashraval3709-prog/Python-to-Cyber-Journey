def AccessSimulator(func):
    def wrapper(*args,**kwargs):
        if args[0]=='admin':
            print('Access successfully...')
            func(*args,**kwargs)
        else:
            print("\nAccess Denied")
    return wrapper

@AccessSimulator
def access(role):
   print(f'Welcome {role}, program started...')

access('admin')
access('user')
