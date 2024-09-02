my_dict = {"name": "John", "age": 30, "city": "New York"}

# 新增
my_dict["email"] = "john@example.com"
print(my_dict)  

#查詢
print(my_dict["name"])

#更新
my_dict["age"] = 31
print(my_dict) 

#刪除
age = my_dict.pop("age")
print(age)
print(my_dict)

del my_dict["email"]
print(my_dict)  