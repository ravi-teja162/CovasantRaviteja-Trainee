D1 = {'ok': 1, 'nok': 2}
D2 = {'ok': 2, 'new':3 }
#union 
union = D1.copy()
for key in D2.keys():
    if key not in union.keys():
        union[key] = D2[key]
print(union)

#DictComprehension - union
union.update({key:D2[key] for key in D2.keys() if key not in D1.keys()})
print(union)
#inrersection
intersection = {}
for key in D2.keys():
    if key in D1.keys():
        intersection[key] = D1[key]
print(intersection)
#DictComprehension - intersection
print({key : D1[key ]for key in D2.keys() if key in D1.keys()})

#Subtraction (D1-D2)
sub = {}
for key in D1.keys():
    if key not in D2.keys():
       sub[key] = D1[key]
print(sub)
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



