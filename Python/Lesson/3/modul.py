# Модульность
# Вы когда-нибудь задавались вопрос, как например работает функция .append Это же точно такая же функция, как и sumNumbers(n), 



# import function_file
# 5
# print(function_file.f(1)) # Целое
# print(function_file.f(2.3)) # 23
# print(function_file.f(28)) # None

# def new_string(symbol, count):
# return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # TypeError missing 1 required ...

# def new_string(symbol, count=3):
# return symbol * count
# print(new_string('!', 5)) # !!!!!
# print(new_string('!')) # !!!
# print(new_string(4)) # 12


# def concatenatio(*params):
# res = ""
# for item in params:
# res += item
# return res
# print(concatenatio('a', 's', 'd', 'w')) # asdw
# print(concatenatio('a', '1')) # a1
# # print(concatenatio(1, 2, 3, 4)) # TypeError: