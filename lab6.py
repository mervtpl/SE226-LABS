#Q1
def fuctorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * fuctorial(x-1)

#Q2
y=lambda n,x: pow(-1,n)*pow(x,2*n+1)/fuctorial(2*n+1)

def sine_x(x,n):
 for i in range(1,n+1):
    sum = 0
    sum += y(i,x)
    return sum

#Q3
value= 0
def H(v):
    """This function calculates the sum of the harmonic series up to n"""
    global value

    if v==1:
        value += 1
    else:
        value += 1/v
        H(v-1)


print(fuctorial(5))
print(sine_x(2,1))

H(3)
print(value)

