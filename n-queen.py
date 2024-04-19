

n=int(input("ENTER SIZE : "))

b=[]

#c=[[0]*n for i in range(n)]

for i in range(n):
    temp=[]
    for j in range(n):
        temp.append(0)
    b.append(temp)



def isSafe(i,j):

    for a in range(n):
        if b[i][a] ==1 or b[a][j] ==1:
            return False

    
    for c in range(n):
        for d in range(n):
            if i+j==c+d or i-j==c-d:
                if b[c][d]== 1:
                    return False
    return True

def nqueen(number_of_queen):

    

    if number_of_queen==0:
        return True

    
    for i in range(n):
        for j in range(n):
            if b[i][j] !=1 and isSafe(i,j):
                 b[i][j]=1

                 if nqueen(number_of_queen-1)== True:
                     return True
                 b[i][j]=0
                
    return False
        


nqueen(n)


for i in range(n):
    for j in range(n):
        print(b[i][j], end=" ")
    print()


