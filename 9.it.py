                                      #9

#3)
"""3. (3) Программа. На вход программе подаётся последовательность целых положительных чисел, не
превосходящих 30000. Признак конца ввода — ноль. Выведите наибольший общий делитель всех введённых чисел.
"""
s = input()
A = [int(s) for s in s.split()]
MIN = min(A)
flag = False
while not flag:
    k = 0
    for i in range(len(A)):
        if not(A[i] % MIN):
            k += 1
    if k == len(A):
        flag = True
    else:
        MIN -= 1
print(MIN)
#5)
"""5. (3) Программа. Вводится последовательность символов. Точка — признак конца. Верно ли, что данная последовательность
является правильной записью нечётного числа в двенадцатеричной системе счисления? Вывести ответ в форме «yes/no».
Напомним, что в двенадцатеричной системе счисления используются цифры 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B."""
"""Если основание системы счисления исходного числа чётно, то при переводе числа в 10 систему счисления получится чётное
число, если последняя цифра исходного числа чётна. Иначе, получится нечётное числою."""
a = input()
k = 0
k_special = 0
while a != ".":
    k += 1
    if a in "0123456789AB":
        k_special += 1
    if a.isalpha:
        if a == "A":
            a = 10
        elif a == "B":
            a = 11
    tmp = a
    a = input()
if tmp % 2 and k == k_special:
    print("YES")
else:
    print("NO")
#3)
"""3. (3) Программа. На вход программе подаётся натуральное число, не превосходящее 2 * 10^9. Выведите
на экран его разложение на простые делители, перечислив их в порядке возрастания.
Например, для числа 36 программа должна вывести «2 2 3 3»."""
""""""

#6)
"""6. (4) Программа. Вводится последовательность символов. Точка — признак конца. Необходимо подсчитать количество
различных символов во введённой последовательности. Напишите программу для решения данной задачи."""
A = []
a = input()
while a != ".":
    A.append(a)
    a = input()
k = 0
for i in range(len(A)):
    if A.count(A[i]) >= 2:
        k += 1
print(len(A) - k)
