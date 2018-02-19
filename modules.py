# coding: utf-8
import numpy as np


def upper(base_list, comp_list, t):
    sub_list = comp_list - base_list
    index = np.where(sub_list > t)
    return index[0]


def downer(base_list, comp_list, t):
    sub_list = base_list - comp_list
    index = np.where(sub_list > t)
    return index[0]


if __name__ == '__main__':
    base = np.array([0, 5, 6, 2, 5])
    comp = np.array([4, 1, 3, 2, 7])
    index = downer(base, comp, 3)
    print(index)
