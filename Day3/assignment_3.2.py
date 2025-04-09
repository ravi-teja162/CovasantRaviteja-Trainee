def tupleToList_fun(lst):
    for i in lst[0]:
        #i = [ '(0,1,2)' , '(3,4,5)']
        for j in range(len(i)):
            temp = []
            for k in range(len(i[j])):
                if k%2 !=0:
                    temp.append(int(i[j][k]))
            i[j] = temp
            
            temp = []
    return lst
    
          
lst = [[[ '(0,1,2)' , '(3,4,5)'], ['(5,6,7)' , '(9,4,2)']]]
print(tupleToList_fun(lst))
