n=int(input("Enter first Number: "));
m=int(input("Enter second Number: "));

op=(input("Enter Operator: "));
print("Result: ")
if(op=="+"):
    print(n+m);
elif(op=="-"):
    print(n-m);
elif(op=="*"):
    print(n*m);
elif(op=="/"):
    print(n/m);
elif(op=="%"):
    print(n%m);
else:
    print("Invalid Operator");
