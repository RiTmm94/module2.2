first = int(input('Введите первое, любое, целое число: ' ))
second = int(input('Введите второе, любое, целое число: ' ))
third = int(input('Введите третье, любое, целое число: ' ))
if first == second and first == third and second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)