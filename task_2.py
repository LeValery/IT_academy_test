# -*- coding: utf-8 -*-

def norm(vect):
    a = sum(list(elem**2 for elem in vect))**(1/2)
    return a

def cos_dist(vect_1, vect_2):
    if len(vect_1) == len(vect_2):
        dot_prod = sum(list(x*y for x, y in zip(vect_1, vect_2)))
        norm_v1 = norm(vect_1)
        norm_v2 = norm(vect_2)
        if norm_v1 * norm_v2:
            print(f'Косинусное расстояние: {round(dot_prod/norm_v1/norm_v2, 4)}')
        else:
            print('В функцию передан нулевой вектор, по определению косинусное расстояние:', 0.0)
    else:
        print('В функцию переданы векторы разных размерностей, косинусное расстояние для них не определено.')
        
       
"""
cos_dist([1, -1, 2], [2, 3, -5])
cos_dist([1, -1, 2], [2, 3])
cos_dist([1, -1, 2], [0, 0, 0])
cos_dist([1, -1, 2], [-2, 2, -4])
"""
