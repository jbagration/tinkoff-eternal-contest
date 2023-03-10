'''
Во время разработки некоторой задачи Саша решил сгенерировать несколько новых тестов. Каждый тест Саши должен представлять собой натуральное число, не меньшее ﻿ll﻿ и не большее ﻿rr﻿. Кроме того, натуральное число в тесте обязательно должно состоять из одинаковых цифр.
Например, число ﻿999﻿ подходит под это требование, а число ﻿123﻿ — нет. Какое максимальное число различных тестов сможет создать Саша?


Формат входных данных 
В единственной строке вводятся два натуральных числа ﻿l,r l,r﻿ ﻿(1 \leq l,r \leq 10^{18})(1≤l,r≤10^18)﻿— ограничения на тесты Саши.
Обратите внимания, что эти числа не вместятся в ﻿32﻿-битный тип данных, используйте ﻿64﻿-битный при необходимости


Формат выходных данных
Выведите одно число — количество тестов, которое может сделать Саша.


Замечание

В первом тесте Саше подходят номера ﻿[4,5,6,7]﻿.
Во втором тесте подходят все числа, кратные ﻿11﻿, от ﻿11﻿ до ﻿99﻿.
'''

#OK. Пройденные тесты 69.
def function():
    lesser, bigger = (int(x) for x in input().split())

    digits = len(str(bigger))
    tests = []

    for k in range(1, 10):
        if digits == 1:
            if lesser <= k <= bigger:
                tests.append(k)
        else:
            for digit in range(1, digits + 1):
                test = int(str(k) * (digit))
                if lesser <= test <= bigger:
                    tests.append(test)

    tests = set(tests)
    return str(len(tests))


if __name__ == "__main__":
    print(function())
