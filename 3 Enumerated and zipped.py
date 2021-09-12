list=['a','b','c','d']
tuple=('apple','banana','cat','dog')
dict={'name' : 'Mike' , 'ref' : 'Python' , 'sys' : 'Win' }
print(list)
for l in list:
    print(l)
print(tuple)
for t in tuple:
    print(t)
#enumerate list and print its relative index number......
for e1 in enumerate(list):
    print(e1)
for e2 in enumerate(tuple):
    print(e2)
##Zipping of a list, tuple and a dictionary..............
for z1,z2 in zip(list,tuple):
    print(z1,z2)
for z1,z2,z3 in zip(list,tuple,dict.keys()):
    print(z1,z2,z3)
##writing pairs of dictionary............................
for k,v in dict.items():
    print(k,'=',v)