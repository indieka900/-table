def break_all():
    for j in range(1, 5):
        for i in range(1,4):
            if i*j == 6:
                return(i) # will stop when i*j = 6
            print(i*j)
#reak_all()
def break_loop():
    for i in range(1, 5):
        if (i == 4):
            return(i)
        print(i)
    return(5)
#break_loop()
#for index, item in enumerate(['one', 'two', 'three', 'four']):
    #print(index, '::', item)
d = {"a": 1, "b": 2, "c": 3}
#for key in d:
#    print(key)
#for values in d.values():
#    print(values)
lst = ['alpha', 'bravo', 'charlie', 'delta', 'echo']
#for s in lst:
    #print(s[:1])  #will display the first letter in each of the element
#for idx, s in enumerate(lst):
#    print("%s has an index of %d" % (s, idx)) #will display index of each element in a list
from array import *
my_array = array('i', [1,2,3,4,5])
#my_array.append(6)  # will insert 6 as a last digit
#my_array.insert(0,9)  #will insert 9 in index 0
my_extnd_array = array('i', [7,8,9,10])
my_array.extend(my_extnd_array)  #it extends the array
for i in my_array:
    print(i)