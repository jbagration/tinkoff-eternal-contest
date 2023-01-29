/*
Даня в обеденный перерыв ходит в одно и то же кафе. Ему, как сотруднику банка, положено специальное предложение: при каждой покупке больше, чем на ﻿100100﻿ рублей, Даня получает купон на бесплатный обед.
Даня узнал стоимость своих обедов на ближайшие ﻿nn﻿ дней. Ему хочется минимизировать свои затраты, грамотно используя талоны. Требуется найти минимальные суммарные затраты Дани на обеды.



Формат входных данных
В первой строке дается натуральное число ﻿n(0 \leq n \leq 100).n(0≤n≤100).﻿ В каждой из ﻿nn﻿ строк записана стоимость обеда в каждой из дней (неотрицательное целое число, не больше, чем ﻿300300﻿).



Формат выходных данных 
В первой строке выдайте минимально возможную суммарную стоимость обедов.


Замечание 
В первом примере Дане придется купить первые ﻿33﻿ обеда, после чего у него появится талон. Этот талон будет выгоднее всего потратить на последний обед. Таким образом, он купит первые ﻿44﻿ обеда и получит пятый бесплатный.
*/

/* PT. Пройденные тесты	13. */

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class T09 {
    public static void main(String[] args) {
        int n; // 0 ≤ n ≤ 100
        int[] prices; // неотрицательное целое число, не больше, чем 300
        try (Scanner scanner = new Scanner(System.in)) {
            n = scanner.nextInt();
            prices = new int[n];
            for (int i = 0; i < n; i++) {
                prices[i] = scanner.nextInt();
            }
        }
        int sum = countStep(prices, -1, 0, 0, false);
        System.out.println(sum);
    }

    private static int countStep(int[] prices, int step, int sum, int coupon, boolean couponUsed) {
        if (step >= prices.length - 1) return sum;
        if (step > -1 && !couponUsed && prices[step] > 100) {
            coupon++;
        }
        int sum1 = -1;
        int sum2 = -1;
        step++;
        
            if (coupon == 0) {
            while (coupon == 0) {
                if (step >= prices.length) return sum;
                sum += prices[step];
                if (prices[step] > 100) coupon++;
                step++;
            }
        }
        if (coupon < (prices.length - step)) {
            sum1 = countStep(prices, step, sum + prices[step], coupon, false);
        } else return sum;
        if (coupon > 0) {
            sum2 = countStep(prices, step, sum, coupon - 1, true);
        }


        if (sum1 == -1 && sum2 == -1) return sum;
        if (sum1 == -1) return sum2;
        if (sum2 == -1) return sum1;
        return Math.min(sum1, sum2);
    }
}
