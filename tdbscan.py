import math
import numpy as np
import pylab as pl

# 数据集：每三个一组，分别是编号，和两维度数据
data = """1,0.697,0.46,2,0.774,0.376,3,0.634,0.264,4,0.608,0.318,5,0.556,0.215,6,0.403,0.237,7,0.481,0.149,8,0.437,0.211,9,0.666,0.091,10,0.243,0.267,11,0.245,0.057,12,0.343,0.099,13,0.639,0.161,14,0.657,0.198,15,0.36,0.37,16,0.593,0.042,17,0.719,0.103,18,0.359,0.188,19,0.339,0.241,20,0.282,0.257,21,0.748,0.232,22,0.714,0.346,23,0.483,0.312,24,0.478,0.437,25,0.525,0.369,26,0.751,0.489,27,0.532,0.472,28,0.473,0.376,29,0.725,0.445,30,0.446,0.459"""
a = data.split(",")
print("a: ", a)

# 数据处理成（x1, x2）列表的形式
dataset = [(float(a[i]), float(a[i+1])) for i in range(1, len(a)-1, 3)]
print("dataset: ", dataset)

# 计算欧式距离
def dist(a, b):
    return math.sqrt((math.pow((a[0] - b[0]), 2) + math.pow((a[1] - b[1]), 2)))

# 获取满足聚类条件的邻近点
def getNeighbors(d, D, e):
    neightbors = [i for i in D if dist(d, i) <= e]
    return neightbors

# 扩展聚类
# def expandCluster():


def DBSCAN(D, e, Minpts):
    T = set() # 核心对象集合
    k = 0     # 聚类个数
    C = []    # 聚类集合
    P = set(D)#未访问集合

    for d in D:
        # 计算核心对象并加入到T
        if len(getNeighbors(d, D, e)) >= Minpts:
            T.add(d)
    # 开始聚类
    while len(T):
        P_old = P
        o = list(T)[np.random.randint(0, len(T))]
        print("o: ", o)
        P = P - set(o)
        Q = []
        Q.append(o)
        while len(Q):
            q = Q[0]
            Nq = getNeighbors(q, D, e)
            if len(Nq) >= Minpts:
                S = P & set(Nq)
                Q += (list(S))
                P = P - S
            Q.remove(q)
        k += 1
        Ck = list(P_old - P)
        T = T - set(Ck)
        C.append(Ck)

    MaxId = -1
    C_1 = 0
    T_1 = []
    for d in D:
        # 计算核心对象并加入到T
        if len(getNeighbors(d, D, e)) >= Minpts:
            T_1.append(d)

    return C

def draw(C):
    colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    for i in range(len(C)):
        coo_X = []
        coo_Y = []

        for j in range(len(C[i])):
            coo_X.append(C[i][j][0])
            coo_Y.append(C[i][j][1])
        pl.scatter(coo_X, coo_Y, marker='x', color=colValue[i%len(colValue)], label=i)
        n = range(len(coo_X))
        for i, txt in enumerate(n):
            pl.annotate(txt, [coo_X[i], coo_Y[i]])
    pl.legend(loc='upper right')
    pl.show()

def draw_dataset(dataset):
    # colValue = ['r', 'y', 'g', 'b', 'c', 'k', 'm']
    coo_X = []
    coo_Y = []

    for i in range(len(dataset)):
        coo_X.append(dataset[i][0])
        coo_Y.append(dataset[i][1])
        pl.scatter(coo_X, coo_Y, marker='x')
        n = range(len(coo_X))
        for j, txt in enumerate(n):
            pl.annotate(txt, [coo_X[j], coo_Y[j]])
    pl.legend(loc='upper right')
    pl.show()

C = DBSCAN(dataset, 0.11, 5)
print("C: ", C)
draw_dataset(dataset)
draw(C)
