num = input("Input number: ")
revers = 0
isminus = False
if int(num) < 0:
    isminus = True
for i in range(len(num)):
    remm = int(abs(int(num))) % 10
    revers = revers * 10 + remm
    num = int(num) / 10
if isminus:
    print(int((revers * -1) / 10))
else:
    print(revers)
