'''Ваня принес на кухню рулет, который он хочет разделить с коллегами. Для этого он хочет разрезать рулет на ﻿NN﻿ равных частей. Разумеется, рулет можно резать только поперек. Соотвественно, Костя сделает ﻿N - 1N−1﻿ разрез ножом через равные промежутки.

По возвращению с кофе-брейка Ваня задумался — а можно ли было обойтись меньшим числом движений, будь нож Вани бесконечно длинным (иначе говоря, если он мог бы сделать сколько угодно разрезов за раз, если эти разрезы лежат на одной прямой)? Считается, что места для разрезов намечены заранее, и все разрезы делаются с ювелирной точностью.
Оказывается, что можно. Например, если Ваня хотел бы разделить рулет на ﻿44﻿ части, он мог бы обойтись двумя разрезами — сначала он разделил бы рулет на две половинки, а потом совместил бы две половинки и разрезал обе пополам одновременно.
Вам дано число ﻿NN﻿, требуется сказать, каким минимальным числом разрезов можно обойтись.


Формат входных данных
Дано одно натуральное число ﻿N(1\leq N\leq 2 \times10^9)N(1≤N≤2×10^9 )﻿ — количество людей на кофе-брйке.


Формат выходных данных
Выведите одно число — минимальное число движений, которое придется сделать Косте.


Замечание
Чтобы разрезать рулет на ﻿66﻿ частей, Ване сначала придется разрезать его на две равные части, после чего совместить две половинки и сделать два разреза.
Чтобы разрезать рулет на ﻿55﻿ частей, Ване понадобится разделить его в соотношении ﻿2:32:3﻿, после чего совместить два рулета по левому краю и разрезать бОльший рулет на одинарные кусочки — меньший тоже разделится на одинарные.
'''

#OK
n = int(input())
print(n.bit_length() - (n & (n - 1) == 0))
