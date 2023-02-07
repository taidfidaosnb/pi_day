from math import *
import matplotlib.pyplot as plt

def get_fdigit_count(function, n):
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(1, n+1):
        k = function(i)
        result[int(str(k)[0])] += 1
    for i in range(10):
        result[i] = result[i] / n
    return result

def get_benford_graph(r):
    bnfdval = []
    for i in range(1, 10):
        bnfdval.append(log10(i + 1) - log10(i))
    print(bnfdval, r)
    plt.rc("font", family='NanumGothic')
    plt.plot(list(range(1, 10)), bnfdval, color = 'red', label = "이론상 분포")
    plt.plot(list(range(1, 10)), r[1:], color = 'blue', label="실제 분포")
    plt.legend(loc='best')
    plt.rcParams['axes.unicode_minus'] = False
    plt.show()


