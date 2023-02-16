a = input("Введите пароль")
if len(a) < 5:
    print("Легкий пароль")
elif a[0:6] == "qwert":
    print("Легкий пароль")
else:
 print("OK")


