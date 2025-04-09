D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }

#DictComprehension - union
print("DictComprehension - union")
union = {}
union.update({key:D2[key] for key in D2.keys() if key not in D1.keys()})
print(union)


#DictComprehension - intersection
print({key : D1[key ]for key in D2.keys() if key in D1.keys()})


#DictComprehension - subtraction
print({key : D1[key] for key in D1.keys() if key not in D2.keys()})

#merge
merge = D1.copy()
for key in D2.keys():
    if key in merge:
        merge[key] += D2[key]
    else:
        merge[key] = D2[key]
print(merge)



