#python project
#Your task is to find if it is possible to cut the cake in the below mentioned ways for a given value of N.
#Given an integer N and a cake which can be cut into pieces, each cut should be a straight line going from the center of the cake to its border. Also, the angle between any two cuts must be a positive integer. Two pieces are equal if their appropriate angles are equal. 
#The given cake can be cut in following three ways: 
#•	Cut the cake into N equal pieces.
#•	Cut the cake into N pieces of any size.
#•	Cut the cake into N pieces such that no two of them are equal.


#input : First line contains a single integer T denoting the number of test cases. Each of the following T lines contain a single integer N denoting the number of pieces Chef wants to make.


#output: For each test case, output one line containing 3 space separated characters. Above, we defined the 3 questions that Chef will ask. Output 'T' for True or 'F' for False (quotes for clarity) for each of those questions. Answers for 3 questions (in the order above) must be space separated on the same line.

t=int(input())
for k in range(t):
    n=int(input())
    opt = ['f','f','f']
    if 360%n==0:
        opt[0] = 't'
    if n<=360:
        opt[1] = 't'
    if (n*(n+1)/2)<=360:
        opt[2] = 't'
    print(*opt)
    

    
