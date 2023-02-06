import math, itertools


def exp_seq(a, b=0, c=1, d=0, limit=-1):  # a^(n + b) * c + d
    for i in itertools.count(1):
        yield (a ** (b + i)) * c + d
        if i == limit:
            return


def n_pibo(*args, limit=-1):  # a_(n+1) = a_n + a_(n-1) + ...
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


def cha_pol(
    *args, rank=None, limit=-1
):  # 0 = a_(n+1) * k_(n+1) + a_n * k_n + a_(n-1) * k_(n-1) + ...
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


if __name__ == "__main__":
    print(list(cha_pol(1, 1, 1, 1, 1, rank=[-1, -1, -1, -1, -1, 1], limit=10)))
