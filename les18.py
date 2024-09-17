#list-method


number_list = [1, 2,3,1,10,14]
number_list.append(20)
number_list.insert(1,7)
number_list.remove(2)
number_list.sort()
number_list.reverse()
print(number_list)
print(12 in number_list)
print(number_list.count(1))
print(number_list.index(10))
number_list.pop()

number_list2 = number_list.copy()
number_list2.clear()
print(number_list2)