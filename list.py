my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

# 新增
my_list.insert(2, 10)
print(my_list) 
my_list.extend([7, 8, 9])

# 查詢
print(my_list[0]) 

# 更新
my_list[3] = 15
print(my_list)

# 刪除
my_list.remove(15)
print(my_list)

popped_element = my_list.pop(2)
print(popped_element)
print(my_list)