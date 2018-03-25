##python program to find hcf
x=int(input("enter 1st num:"))
y=int(input("enter 2nd num:"))
rem=1
if(y>x):
    
    while rem!=0:
        rem=y%x
        y=x
        if rem!=0:
            x=rem
        
    print('hcf',x)
    
else:
    while rem!=0:
        rem=x%y
        x=y
        if rem!=0:
            y=rem
        
    print('hcf=',y)
    
    
    
