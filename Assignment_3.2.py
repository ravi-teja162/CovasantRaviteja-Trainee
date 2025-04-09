def fun(ls):
    for i in ls[0]:
        #i = [ '(0,1,2)' , '(3,4,5)']
        for j in range(len(i)):
            temp = []
            print(j)
            for k in range(len(i[j])):
                if k%2 !=0:
                    temp.append(int(i[j][k]))
            print(temp)
            i[j] = temp
            
            temp = []
    return ls
    
            
        
    






lst = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
print(fun(lst))

#[[[[0,1,2],[3,4,5]],[[5,6,7],[9,4,2]]]]
#[[[[0, 1, 2], [3, 4, 5]], [[5, 6, 7], [9, 4, 2]]]]