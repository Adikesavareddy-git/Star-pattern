"""print("\nNormal pyramid")
for i in range(5):
    x='*'
    x=x*i
    print(f'{x:^10}')"""
    
#
#
"""rows =5
for i  in range(1,rows+1):
    print(' ' *(rows-i)+'*' *(2*i-1))
rows =5
for i  in range(rows,0,-1):
    print(' ' *(rows-i)+'*' *(2*i-1))"""
    
    
"""rows = 5
for i in range(rows):
    if i==0 or i==rows+1:
        print('*'*rows)
    else:
        print('*'+' '*(rows-2)+'*') """
        
"""rows =5
for i in range(rows,0,-1): 
    print('*'* i)
rows =5
for i in range(1,rows+1): 
    print(''*(rows-1)+'*'*i)"""
    
"""rows = 5
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if i==j or i+j==rows+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()"""

rows = 5
for i in range(1,rows+1):
    print('*' * i+ ' '*(2*(rows-i))+'*'*i)
for i in range(rows,0,-1):
     print('*'* i +' '*(2*(rows-i))+'*'*i) 