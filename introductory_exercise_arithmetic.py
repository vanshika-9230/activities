'''Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)'''
a=int(input("Enter the number a:"))
b=int(input("Enter the number b:"))
operator=input("Enter the operator:")

if operator=="+":
  print(a+b)
if operator=="-":
   print(a-b)
if operator=="*":
  print(a*b)
if operator=="/":
  print(a/b)
if operator=="**":
   print(a**b)
if operator=="//":
   print(a//b)
if operator=="%":
   print(a%b)