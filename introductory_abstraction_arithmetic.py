def operator(a,b):
    oper=input("enter operation: ")
    if oper=="-" :
        return (a-b)
    elif oper=="+" :
        return (a+b)
    elif oper=="*" :
        return (a*b)
    elif oper=="/" :
        return (a/b)
    elif oper=="//" :
        return (a//b)
a=float(input("enter first number: "))
b=float(input("enter second number: "))
print(operator(a,b))