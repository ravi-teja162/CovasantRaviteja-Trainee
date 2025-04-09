def mergeNestedList(lst):
    final_list = []
    for i in lst:
        if type(i) is int:
            final_list.append(i)
        else:
            sub = mergeNestedList(i)
            final_list= final_list+sub
    return final_list
            



lst = [1,2,3, [1,2,3,[3,4],2]]
print(mergeNestedList(lst))