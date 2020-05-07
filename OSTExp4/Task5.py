def example1():
    for i in range( 3 ):
        x = int( input( "\nenter a number : " ) )
        y = int( input( "enter another number : " ) )
        print( x, '/', y, '=', x/y )
def example2( L ):
    print("\n\nExample 2" )
    sum = 0
    sumOfPairs = []
    for i in range( len( L ) ):
        if i == len(L) - 1:
            sumOfPairs.append(L[i] + L[1])
        else:
            sumOfPairs.append( L[i]+L[i+1] )
        print( "sumOfPairs = ", sumOfPairs )
def main():
    while True:
        try:
            example1()
            L = [ 10, 3, 5, 6, 9, 3 ]
            example2( L )
            example2( [ 10, 3, 5, 6, 3 ] )
            example3( [ 10, 3, 5, 6 ] )
        except ZeroDivisionError:
            print("Please enter a non-zero number!")
        except ValueError:
            print("Please enter an integer value!")
        except IndexError:
            print("Array bounds out of range")
        except TypeError:
            print("Cannot add str and int datatypes")
        except NameError:
            print("Undefined variable or function")
        else:
            print("Everything's fine!")
            break;

main()
