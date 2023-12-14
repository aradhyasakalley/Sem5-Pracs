class BaseError(Exception):
    pass
class HighValueError(BaseError):
    pass
class LowValueError(BaseError):
    pass

value = 29
while(1):
    try:
        n = int(input('enter the number : '))
        if n > value:
            raise HighValueError
        elif n < value :
            raise LowValueError
        
    except LowValueError:
        print('the value if too low enter number again !')
        print()
    except HighValueError:
        print('the value if too high enter number again !')
        print()
    else :
        print('nice input value is optimal! ')
        break