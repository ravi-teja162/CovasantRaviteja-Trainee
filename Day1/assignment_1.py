D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#DictComprehension - union
union = D1.copy()
union.update({key:D2[key] for key in D2.keys() if key not in D1.keys()})
print("Union: ",union)


#DictComprehension - intersection
print("Intersection: ",{key : D1[key ]for key in D2.keys() if key in D1.keys()})


#DictComprehension - subtraction
print("Subtraction(D1-D2): ",{key : D1[key] for key in D1.keys() if key not in D2.keys()})

#merge
merge = D1.copy()
for key in D2.keys():
    if key in merge:
        merge[key] += D2[key]
    else:
        merge[key] = D2[key]
print("Merge: ",merge)
