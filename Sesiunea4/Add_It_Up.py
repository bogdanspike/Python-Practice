def add_it_up(num):
    sum=0
    i=1
    if type(num) is int:
        for i in range(1,num):
            if i!=num:
                sum=sum+i
    else:
        sum=0
    print(sum)    
add_it_up(1.5)                 
        