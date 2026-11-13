# n= int(input("ENTER YOUR NUMBER: "))
# for row in range(n):
#     for row in range(n-1-row):
#         print(' ',end=" ")
#     for col in range(row+1):
#         print('*',end='')

# print()

# n= int(input("ENTER YOUR NUMBER: "))
# m= n//2
# for row in range(n):
#     if row <= m:
#         for col in range(row+1):
#             print('*',end='')
#     else:
#         for col in range(n-row):
#             print('*',end='')


# print()
    
# string loop

# n=int(input("ENTER YOUR NUMBER: "))
# m=n//2
# for row in range(n):
#     if row <= m:
#         print('* '*(row+1))
#     else:
#         print('* '*(n -row))

#short form

# n= int(input("ENTER YOUR NUMBER: "))
# m=n//2
# for row in range(n):
#     print('* '*(row+1) if row <= m else '* '*(n -row))

#for square pattern

# n= int(input("ENTER YOUR NUMBER: "))
# for row in range(n):
#     for col in range(n):
#         if row==0 or row==n-1 or col==0 or col==n-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#for plus pattern

#n= int(input("ENTER YOUR NUMBER: "))
# for row in range(n):    
#     for col in range(n):
#         if row==0 or row==n-1 or col==0 or col==n-1 or row==n//2 or col==n//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for cross line pattern

# n= int(input("ENTER YOUR NUMBER: "))
# for row in range(n):
#     for col in range(n):
#         if row==0 or row==n-1 or col==0 or col==n-1 or row==col or col==n-1-row:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#for Alphabet pattern 'G'

# n= int(input("ENTER YOUR SIZE: "))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if i==0 or j==0 or i==n-1 or (j==n-1 and i>=m) or (i==m and j>=m):
#             print('*',end=' ')
#         else:   
#             print(' ',end=' ')              
#     print() 
 
#for Alphabet pattern 'J'

# n=int(input("enter your size:"))
# m=n//2
# for i in range(n):
#    for j in range(n):
#         if i==0 or j==m or (i==n-1 and j<m) or (j==0 and i>=m):
#             print('*',end=' ')
#         else:                                                                                                  
#             print(' ',end=' ')
#    print()

#for Alphabet pattern 'M'

# n=int(input("enter your size: "))
# m=n//2
# for i in range(n):          
#     for j in range(n):
#         if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')

#     print()

#for Alphabet pattern 'K'

# n= int(input("enter the size:"))
# m=n//2
# for i in range(n):
#     for j in range(n):
#         if j==0 or (i+j==m) or (i-j==m):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#for Alphabet pattern 'P'

# n= int(input("enter the size:"))
# m=n//2                  
# for i in range(n):
#     for j in range(n):
#         if j==0  or (i==0 and j<m-0) or (i==m and j<m) or (j==m and i<m):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#for Alphabet pattern 'A'

# n= int(input("enter the size:"))
# m=n//2      
# for i in range(n):          
#     for j in range(n):
#         if (j==0 and i!=0) or (j==n-1 and i!=0) or (i==0 and j>0 and j<n-1) or (i==m):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

#for Alphabet pattern 'E'

# n= int(input("enter the size:"))    
# m=n//2
# for i in range(n):        
#     for j in range(n):
#         if j==0 or (i==0 and j>0) or (i==m and j>0) or (i==n-1 and j>0):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

