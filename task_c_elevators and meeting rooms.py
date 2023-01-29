'''
У Кати насыщенный день на работе. Ей надо передать n разных договоров коллегам. Все встре- чи происходят на разных этажах, а между этажами можно перемещаться только по лестничным пролетам — считается, что это улучшает физическую форму сотрудников. Прохождение каждого пролета занимает ровно ﻿11﻿ минуту.
Сейчас Катя на парковочном этаже, планирует свой маршрут. Коллег можно посетить в любом порядке, но один из них покинет офис через ﻿tt﻿ минут. С парковочного этажа лестницы нет — только лифт, на котором можно подняться на любой этаж.
В итоге план Кати следующий:


Подняться на лифте на произвольный этаж. Считается, что лифт поднимается на любой этаж за ﻿00﻿ минут.
Передать всем коллегам договоры, перемещаясь между этажами по лестнице. Считается, что договоры на этаже передаются мгновенно.
В первые ﻿tt﻿ минут передать договор тому коллеге, который планирует уйти.
Пройти минимальное количество лестничных пролетов.
Помогите Кате выполнить все пункты ее плана.


Формат входных данных
В первой строке вводятся целые положительные числа ﻿n﻿ и ﻿t﻿ ﻿(2\leq n,t \leq 100)(2≤n,t≤100)﻿ — количество сотрудников и время, когда один из сотрудников покинет офис (в минутах). В следующей строке n чисел — номера этажей, на которых находятся сотрудники. Все числа различны и по абсолютной величине не превосходят 100. Номера этажей даны в порядке возрастания. В следующей строке записан номер сотрудника, который уйдет через t минут.


Формат выходных данных
Выведите одно число — минимально возможное число лестничных пролетов, которое понадобится пройти Кате.


Замечание
В первом примере времени достаточно, чтобы Катя поднялась по этажам по порядку.
Во втором примере Кате понадобится подняться к уходящему сотруднику, а потом пройти всех остальных — например, в порядке ﻿\{1,2,3,4,6\}{1,2,3,4,6}
'''

# Пройденные тесты 5.
n,t = map(int,input().strip().split())
floors = list(map(int,input().strip().split()))
pers = int(input())

def time_floor(n,t,floors, pers):
    if t>floors[pers-1]:
        return max(floors)-1
    else: 
        return max(floors[:pers-1]+floors[pers:])+floors[pers-1]-2
   
print(time_floor(n,t,floors, pers))



# Пройденные тесты 44.
def function():
    employees, time_to_leave = [int(x) for x in input().split()]
    floors = [int(x) for x in input().split()]
    employee = int(input())

    deadline = floors[employee - 1]

    min_floor = floors[0]
    max_floor = floors[-1]

    if deadline - min_floor < time_to_leave:
        summary_time = max_floor - min_floor

    else:
        up = max_floor - min_floor + max_floor - deadline
        down = max_floor - min_floor + deadline - min_floor
        summary_time = min(up, down)

    return str(summary_time)


if __name__ == "__main__":
    print(function())
