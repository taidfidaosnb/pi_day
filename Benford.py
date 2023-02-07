import itertools
import matplotlib.pyplot as plt
import random
from math import *


def exp_seq(a: int, b: int = 0, c: int = 1, d: int = 0, limit: int = -1):
    """
    Generates an iterator sequence of an exponential function.
    \n a_n = a ^ (n + b) * c + d

    :param a: base
    :param b: negative x moves
    :param c: coefficient
    :param d: positive y moves
    :param limit: last index of the sequence
    :return: Generator[float]
    """
    for i in itertools.count(1):
        yield (a ** (b + i)) * c + d
        if i == limit:
            return


def n_pibo(*args, limit: int = -1):
    """
    Generates an iterator sequence of n-pibonacci.
    \n a_(n+1) = a_n + a_(n-1) + ...

    :param args: initial values
    :param limit: last index of the sequence
    :return: Generator[float]
    """
    temp = list(args)

    for i in range(len(temp)):
        yield temp[i]
        if i + 1 == limit:
            return

    for i in itertools.count(len(temp)):
        temp = temp[1:] + [sum(temp)]
        yield temp[-1]
        if i + 1 == limit:
            return


def cha_pol(*args, rank=None, limit: int = -1):
    """
    Generates an iterator sequence of recurrence relation.
    \n 0 = a_(n+1) * k_(n+1) + a_n * k_n + a_(n-1) * k_(n-1) + ...

    :param args: initial values
    :param rank: coefficients
    :param limit: last index of the sequence
    :return: Generator[float]
    """
    if rank is None:
        rank_tmp = [-1] * len(args) + [1]
    else:
        rank_tmp = list(rank)
    temp = list(args)

    if len(temp) + 1 != len(rank_tmp):
        raise IndexError

    for i in range(len(temp)):
        yield temp[i]
        if i + 1 == limit:
            return

    for i in itertools.count(len(temp)):
        tmp = 0
        for j in range(len(temp)):
            tmp += temp[j] * rank_tmp[j]
        temp = temp[1:] + [-1 * tmp / rank_tmp[-1]]
        yield temp[-1]
        if i + 1 == limit:
            return


def func_iter(*args, func=lambda x: x + 1, limit: int = -1, noargs: int = 0):
    '''

    :param args:
    :param func:
    :param limit:
    :param noargs:
    :return:
    '''
    if not noargs:
        if args:
            for i in itertools.count(1):
                yield func(i, args)
                if i + 1 == limit:
                    return
        for i in itertools.count(1):
            yield func(i)
            if i + 1 == limit:
                return
    for i in itertools.count(1):
        yield func()
        if i + 1 == limit:
            return


def get_benford_graph(iter, limit):
    '''
    
    :param iter: 
    :param limit: 
    :return: 
    '''
    bff = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i, j in zip(iter, range(1, limit + 1)):
        bff[int(str(i)[0])] += 1
    bff = [i / limit for i in bff]

    bnfdval = []
    for i in range(1, 10):
        bnfdval.append(log10(i + 1) - log10(i))

    plt.rc("font", family="NanumGothic")
    plt.plot(list(range(1, 10)), bnfdval, color="red", label="이론상 분포")
    plt.plot(list(range(1, 10)), bff[1:], color="blue", label="실제 분포")
    plt.legend(loc="best")
    plt.rcParams["axes.unicode_minus"] = False
    plt.show()


if __name__ == "__main__":
    # print(list(n_pibo(1, 1, 1, 1, 1, limit=10000)))
    # print(list(func_iter(3, func=lambda x, y: y[0] ** x, limit=30)))
    get_benford_graph(func_iter(func=lambda x: x**x), 1000)
