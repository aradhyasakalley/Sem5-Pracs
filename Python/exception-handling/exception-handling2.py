import math

try :
    imp = "import "+ input("Enter the module to be imported: ")
    exec(imp)
    n = {}
    n1,n2,k1,k2 = eval(input('enter the two numbers and their key seperated by comma: '))
    n[k1] = n1
    n[k2] = n2
    result = n[k1]/n[k2]
    m = int(input('enter one more number'))
    print('the result is: ',result/math.sqrt(m))
    if n[k1] == 0 :
        raise RuntimeError
    
except ValueError:
    print('invalid literal !')
except RuntimeError:
    print('may be meaningless !')
except ZeroDivisionError:
    print('cannot divide with zero !')
except ImportError:
    print('module does not exist !')
except KeyboardInterrupt:
    print()
    print('program was interrupyed !')
except KeyError:
    print('requested key was not found !')
except SyntaxError:
    print('invalid syntax !')
except:
    print("Something wrong in input.")
else:
    print("No exceptions.")
finally :
    print('all inputs executed succesfully !')