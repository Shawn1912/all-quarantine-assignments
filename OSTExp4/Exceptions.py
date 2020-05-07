import math
import sys
try:
    x = int(input('Please enter a positive number:\n'))
    try:
        print(f'Square Root of {x} is {math.sqrt(x)}')
    except ValueError as ve:
        print(f'You entered {x}, which is not a positive number.')
    y = int(input('Please enter a positive number:\n'))
    try:
        try:
            print("DIVISION: "+(x/y))
        except TypeError as ve:
            print(f'Value Error!')
    except ZeroDivisionError as ve:
        print(f'You entered {y}, which is 0.')
    try:
        print("Calculation Complete!");
    except IndentationError as ve:
        print("There was a syntax error!")
    try:
        abc
    except NameError as ve:
        print("Name Error!")
    assert y != 0, "Invalid Operation"
    print(x / y)

    try:
        X = 10
        X.append(5)
    except AttributeError as ve:
        print("Attribute Error!")
    try:
        a = 10 / 0
        print(a)
    except ArithmeticError:
        print("This statement is raising an arithmetic exception.")
    else:
        print("Success.")
    try:
        n = int(v)
    except Exception:
        print("Couldn't parse")
    try:
        a = [5, 8, 17]
        print(a[17])
    except LookupError:
        print("Index out of bound error.")
    else:
        print("Success")
    try:
        print(math.exp(1000))
    except OverflowError as ve:
        print("Overflow Error!")
    try:
        import module_does_not_exist
    except ImportError as ve:
        print("Import Error!")
    except ValueError as ve:
        print('You are supposed to enter positive number.')
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: {0}".format(err))
    try:
        my_list = [5,6, 8, 4, 17,5]
        print(my_list[6])
    except IndexError as e:
        print(e)
    try:
        spec.loader.exec_module(module)
    except BaseException:
        try:
            del sys.modules[spec.name]
        except KeyError:
            pass
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print ("Could not convert data to an integer.")
except:
    print ("Unexpected error:", sys.exc_info()[0])
