import math

import numpy as np


# Example
def infoMaker():
    info = np.zeros((5, 4))

    info[0][0] = 57.99
    info[0][1] = 0.105
    info[0][2] = 8.2 * 10 ** 8
    info[0][3] = 14.15

    info[1][0] = 180
    info[1][1] = 0.021
    info[1][2] = 8.2 * 10 ** 8
    info[1][3] = 9

    info[2][0] = 90
    info[2][1] = 0.021
    info[2][2] = 4.1 * 10 ** 8
    info[2][3] = 12

    info[3][0] = 180
    info[3][1] = 0.105
    info[3][2] = 4.1 * 10 ** 8
    info[3][3] = 7.5

    info[4][0] = 53.13
    info[4][1] = 0.105
    info[4][2] = 4.1 * 10 ** 8
    info[4][3] = 15

    return info


def RMaker():
    # R = [[3, 1], [4, 0], [4, 1]]
    R = [[1, 0], [3, 1], [4, 1]]
    RR = []
    for x in R:
        RR.append((x[0] - 1) * 2 + x[1])
    RR.sort(reverse=True)
    # print(RR)
    return RR


def PMaker():
    P = [0, 6400, -4800, 0, -3200, 0, 0, 0]
    return P


def ReCal(alpha):
    alpha = alpha / (180 / np.pi)
    Re = np.zeros((4, 2))
    Re[0][0] = round(math.cos(alpha), 7)
    Re[1][0] = round(math.sin(alpha), 7)
    Re[2][1] = round(math.cos(alpha), 7)
    Re[3][1] = round(math.sin(alpha), 7)
    # print(Re)
    return Re


def KrCal(F, E, L):
    Kr = np.ones((2, 2))
    Kr[0][1] = -1
    Kr[1][0] = -1
    Kr = (F * E / L) * Kr
    # print(Kr)
    return Kr


def KeCal(Re, Kr):
    Re_1 = Re.transpose()
    Ke = np.dot(Re, Kr)
    Ke = np.dot(Ke, Re_1)
    return Ke


def elemanCr(info):
    Eleman = []
    Ke = []
    parametrs = []
    for x in range(5):
        Re = ReCal(info[x][0])
        Kr = KrCal(info[x][1], info[x][2], info[x][3])
        Ke.append(KeCal(Re, Kr))
        parametrs.append([Re, Kr, Ke])
    Eleman.append(Ke)
    Eleman.append(parametrs)
    return Eleman


def KgCal(Eleman):
    Kg = np.zeros((8, 8))

    shift0 = 0
    shift2 = 2
    x = 0
    Kg[0 + x][0 + x] = Eleman[2][0 + shift0][0 + shift0] + Eleman[3][0 + shift0][0 + shift0] + Eleman[4][0 + shift0][
        0 + shift0]
    Kg[0 + x][1 + x] = Eleman[2][0 + shift0][1 + shift0] + Eleman[3][0 + shift0][1 + shift0] + Eleman[4][0 + shift0][
        1 + shift0]
    Kg[1 + x][0 + x] = Eleman[2][1 + shift0][0 + shift0] + Eleman[3][1 + shift0][0 + shift0] + Eleman[4][1 + shift0][
        0 + shift0]
    Kg[1 + x][1 + x] = Eleman[2][1 + shift0][1 + shift0] + Eleman[3][1 + shift0][1 + shift0] + Eleman[4][1 + shift0][
        1 + shift0]
    x = 2
    Kg[0 + x][0 + x] = Eleman[0][0 + shift2][0 + shift2] + Eleman[1][0 + shift2][0 + shift2] + Eleman[2][0 + shift2][
        0 + shift2]
    Kg[0 + x][1 + x] = Eleman[0][0 + shift2][1 + shift2] + Eleman[1][0 + shift2][1 + shift2] + Eleman[2][0 + shift2][
        1 + shift2]
    Kg[1 + x][0 + x] = Eleman[0][1 + shift2][0 + shift2] + Eleman[1][1 + shift2][0 + shift2] + Eleman[2][1 + shift2][
        0 + shift2]
    Kg[1 + x][1 + x] = Eleman[0][1 + shift2][1 + shift2] + Eleman[1][1 + shift2][1 + shift2] + Eleman[2][1 + shift2][
        1 + shift2]
    x = 4
    Kg[0 + x][0 + x] = Eleman[0][0 + shift0][0 + shift0] + Eleman[3][0 + shift2][0 + shift2]
    Kg[0 + x][1 + x] = Eleman[0][0 + shift0][1 + shift0] + Eleman[3][0 + shift2][1 + shift2]
    Kg[1 + x][0 + x] = Eleman[0][1 + shift0][0 + shift0] + Eleman[3][1 + shift2][0 + shift2]
    Kg[1 + x][1 + x] = Eleman[0][1 + shift0][1 + shift0] + Eleman[3][1 + shift2][1 + shift2]
    x = 6
    Kg[0 + x][0 + x] = Eleman[1][0 + shift0][0 + shift0] + Eleman[4][0 + shift2][0 + shift2]
    Kg[0 + x][1 + x] = Eleman[1][0 + shift0][1 + shift0] + Eleman[4][0 + shift2][1 + shift2]
    Kg[1 + x][0 + x] = Eleman[1][1 + shift0][0 + shift0] + Eleman[4][1 + shift2][0 + shift2]
    Kg[1 + x][1 + x] = Eleman[1][1 + shift0][1 + shift0] + Eleman[4][1 + shift2][1 + shift2]

    aa = [[2, 0, 2, [shift2, shift0]], [4, 0, 3, [shift2, shift0]], [6, 0, 4, [shift2, shift0]],
          [4, 2, 0, [shift2, shift0]], [6, 2, 1, [shift2, shift0]],
          [0, 2, 2, [shift0, shift2]], [0, 4, 3, [shift0, shift2]], [0, 6, 4, [shift0, shift2]],
          [2, 4, 0, [shift0, shift2]], [2, 6, 1, [shift0, shift2]]]

    for x in aa:
        Kg[0 + x[1]][0 + x[0]] = Eleman[x[2]][0 + x[3][0]][0 + x[3][1]]
        Kg[0 + x[1]][1 + x[0]] = Eleman[x[2]][0 + x[3][0]][1 + x[3][1]]
        Kg[1 + x[1]][0 + x[0]] = Eleman[x[2]][1 + x[3][0]][0 + x[3][1]]
        Kg[1 + x[1]][1 + x[0]] = Eleman[x[2]][1 + x[3][0]][1 + x[3][1]]

    return Kg


def UCal(kg, red, p):
    #####################################Kred##################################
    Kred = np.zeros((8 - len(red), 8 - len(red)))
    loop = [0, 1, 2, 3, 4, 5, 6, 7]
    for x in red:
        loop.remove(x)
    xx = -1
    for x in loop:
        xx += 1;
        yy = -1
        for y in loop:
            yy += 1;
            Kred[yy][xx] = kg[y][x]
    # print(Kred)

    #####################################Kred##################################
    for x in red:
        del p[x]
    P1 = np.zeros((5, 1))
    i = 0
    for x in P1:
        x[0] = p[i]
        i += 1
    # print(P1)

    #####################################P1##################################
    U = np.dot(np.linalg.inv(Kred), P1)
    # print(U)

    U1 = np.zeros((8, 1))
    # print(U)
    # print(loop)
    UU = 0
    for x in loop:
        U1[x] = U[UU]
        # U1[x] = UU
        UU += 1
    # print(U1)

    return U1

    #####################################U##################################


def WeAndS(ElemanP, u):
    SS = []
    WW = []
    result = []
    aa = [[4, 5, 2, 3],
          [6, 7, 2, 3],
          [0, 1, 2, 3],
          [0, 1, 4, 5],
          [0, 1, 6, 7]]
    y = 0
    for x in aa:
        Re = ElemanP[y][0]
        Kr = ElemanP[y][1]
        u1 = np.zeros((4, 1))
        # print(u)
        for i in range(4):
            u1[i] = u[x[i]]
        We = np.dot(Re.transpose(), u1)
        S = np.dot(Kr, We)
        # print(u1)
        # print(Re)
        # print(We)
        # print(S)
        SS.append(S)
        WW.append(We)
        y += 1
    result.append(WW)
    result.append(SS)
    return result


def Lager(kg, u):
    La = np.dot(kg, u)
    return La


info = infoMaker()
red = RMaker()
p = PMaker()

eleman = elemanCr(info)
kg = KgCal(eleman[0])
u = UCal(kg, red, p)
WS = WeAndS(eleman[1], u)
Lager(kg, u)
