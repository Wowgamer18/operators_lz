n = int(input("Введите пожалуйста число и мы узнаем, является ли оно простым или нет: "))
if n > 1 and 1 <= n <= 25:
    flag = True
    i = 2
    while i * i <= n:
        if n % i == 0:
            flag = False
            break
        i += 1
    if flag is True:
        print("Y")
    else:
        print("N")
else:
    print("N")