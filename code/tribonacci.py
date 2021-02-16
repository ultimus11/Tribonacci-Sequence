def tribonacci(signature, n):
    output=[]
    if n==0:
        return[]
    for number_of_times in range(1,n-2):
        add=0
        for last_three in signature[-3:]:
            add+=last_three
        signature.append(add)
    for nthelement in signature[:n]:
        output.append(nthelement)
    return output

print(tribonacci([1,1,1],20))

#0,1,1,2,3,5,8,13,21.... fibonacci
#0,1,1,2,4,7... tribonacci