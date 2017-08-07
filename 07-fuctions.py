# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hello, {}".format(name))


name1 = "marco"
name2 = "jane"
name3 = "john"
name4 = "tom"
name5 = "marco"
name6 = "jane"
name7 = "john"
name8 = "tom"
# print("hello, {}".format(name1))
# print("hello, {}".format(name2))
# print("hello, {}".format(name3))
# print("hello, {}".format(name4))
# print("hello, {}".format(name5))
# print("hello, {}".format(name6))
# print("hello, {}".format(name7))
# print("hello, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 입력값 o, 반환값 o
def sum(a, b):
    return a + b
# 입력값 o, 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))

# 입력값 x, 반환값 o
def return_1():
    return 1

# 입력값 x, 반환값 x
def hello_world():
    print("hello world")

num_1 = return_1()
print(num_1)
