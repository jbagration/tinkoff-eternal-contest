/*Костя подключен к мобильному оператору «Мобайл». Абонентская плата Кости составляет ﻿AA﻿ рублей в месяц. За эту стоимость Костя получает ﻿BB﻿ мегабайт интернет-трафика. Если Костя выйдет за лимит трафика, то каждый следующий мегабайт будет стоить ему ﻿CC﻿ рублей.

Костя планирует потратить ﻿DD﻿ мегабайт интернет-трафика в следующий месяц. Помогите ему сосчитать, во сколько рублей ему обойдется интернет.

Формат входных данных
Вводится ﻿44﻿ целых положительных числа ﻿A, B, C, D (1\leq A, B, C, D \leq100)A,B,C,D(1≤A,B,C,D≤100)﻿ — стоимость тарифа Кости, размер тарифа Кости, стоимость каждого лишнего мегабайта, размер интернет-трафика Кости в следующем месяце. Числа во входном файле разделены пробелами.


Формат выходных данных
Выведите одно натуральное число — суммарные расходы Кости на интернет.


Замечание

В первом примере Костя сначала оплатит пакет интернета, после чего потратит на ﻿55﻿ мегабайт больше, чем разрешено по тарифу. Следовательно, за ﻿55﻿ мегабайт он дополняет отдельно, получившаяся стоимость ﻿100+12\times5=160100+12×5=160﻿ рублей.
Во втором примере Костя укладывается в тарифный план, поэтому платит только за него. */

import java.util.Scanner;
 
public class Main {
    static Scanner scn = new Scanner(System.in);
 
    public static void main(String[] args) {
        int a = scn.nextInt();
        int b = scn.nextInt();
        int c = scn.nextInt();
        int d = scn.nextInt();
        int sum = a;
        if (d - b > 0) {
            sum += (d - b) * c;
        }
        System.out.println(sum);
    }
}
