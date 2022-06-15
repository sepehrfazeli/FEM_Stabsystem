import math

import numpy as np


def infoMaker(inp):
    info = np.zeros((5, 4))

    for i in range(5):
        for j in range(4):
            info[i][j] = inp[i][j]

    return info


def RMaker(resistance):
    RR = []
    for x in resistance:
        RR.append((x[0] - 1) * 2 + x[1])
    RR.sort(reverse=True)
    # print(RR)
    return RR


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
        Kee = KeCal(Re, Kr)
        Ke.append(Kee)
        parametrs.append([Re, Kr, Kee])
    Eleman.append(Ke)
    Eleman.append(parametrs)
    return Eleman


def KgCal(Element):
    Kg = np.zeros((8, 8))

    shift0 = 0
    shift2 = 2

    x = 0
    Kg[0 + x][0 + x] = Element[2][0 + shift0][0 + shift0] \
                       + Element[3][0 + shift0][0 + shift0] \
                       + Element[4][0 + shift0][0 + shift0]
    Kg[0 + x][1 + x] = Element[2][0 + shift0][1 + shift0] \
                       + Element[3][0 + shift0][1 + shift0] \
                       + Element[4][0 + shift0][1 + shift0]
    Kg[1 + x][0 + x] = Element[2][1 + shift0][0 + shift0] \
                       + Element[3][1 + shift0][0 + shift0] \
                       + Element[4][1 + shift0][0 + shift0]
    Kg[1 + x][1 + x] = Element[2][1 + shift0][1 + shift0] \
                       + Element[3][1 + shift0][1 + shift0] \
                       + Element[4][1 + shift0][1 + shift0]

    x = 2
    Kg[0 + x][0 + x] = Element[0][0 + shift2][0 + shift2] \
                       + Element[1][0 + shift2][0 + shift2] \
                       + Element[2][0 + shift2][0 + shift2]
    Kg[0 + x][1 + x] = Element[0][0 + shift2][1 + shift2] \
                       + Element[1][0 + shift2][1 + shift2] \
                       + Element[2][0 + shift2][1 + shift2]
    Kg[1 + x][0 + x] = Element[0][1 + shift2][0 + shift2] \
                       + Element[1][1 + shift2][0 + shift2] \
                       + Element[2][1 + shift2][0 + shift2]
    Kg[1 + x][1 + x] = Element[0][1 + shift2][1 + shift2] \
                       + Element[1][1 + shift2][1 + shift2] \
                       + Element[2][1 + shift2][1 + shift2]

    x = 4
    Kg[0 + x][0 + x] = Element[0][0 + shift0][0 + shift0] + Element[3][0 + shift2][0 + shift2]
    Kg[0 + x][1 + x] = Element[0][0 + shift0][1 + shift0] + Element[3][0 + shift2][1 + shift2]
    Kg[1 + x][0 + x] = Element[0][1 + shift0][0 + shift0] + Element[3][1 + shift2][0 + shift2]
    Kg[1 + x][1 + x] = Element[0][1 + shift0][1 + shift0] + Element[3][1 + shift2][1 + shift2]

    x = 6
    Kg[0 + x][0 + x] = Element[1][0 + shift0][0 + shift0] + Element[4][0 + shift2][0 + shift2]
    Kg[0 + x][1 + x] = Element[1][0 + shift0][1 + shift0] + Element[4][0 + shift2][1 + shift2]
    Kg[1 + x][0 + x] = Element[1][1 + shift0][0 + shift0] + Element[4][1 + shift2][0 + shift2]
    Kg[1 + x][1 + x] = Element[1][1 + shift0][1 + shift0] + Element[4][1 + shift2][1 + shift2]

    aa = [[2, 0, 2, [shift2, shift0]], [4, 0, 3, [shift2, shift0]], [6, 0, 4, [shift2, shift0]],
          [4, 2, 0, [shift2, shift0]], [6, 2, 1, [shift2, shift0]],
          [0, 2, 2, [shift0, shift2]], [0, 4, 3, [shift0, shift2]], [0, 6, 4, [shift0, shift2]],
          [2, 4, 0, [shift0, shift2]], [2, 6, 1, [shift0, shift2]]]

    for x in aa:
        Kg[0 + x[1]][0 + x[0]] = Element[x[2]][0 + x[3][0]][0 + x[3][1]]
        Kg[0 + x[1]][1 + x[0]] = Element[x[2]][0 + x[3][0]][1 + x[3][1]]
        Kg[1 + x[1]][0 + x[0]] = Element[x[2]][1 + x[3][0]][0 + x[3][1]]
        Kg[1 + x[1]][1 + x[0]] = Element[x[2]][1 + x[3][0]][1 + x[3][1]]

    return Kg


def UCal(kg, red, p):
    #####################################Kred##################################
    Kred = np.zeros((8 - len(red), 8 - len(red)))

    loop = [0, 1, 2, 3, 4, 5, 6, 7]
    for x in red:
        loop.remove(x)

    for i, x in enumerate(loop):
        for j, y in enumerate(loop):
            Kred[j][i] = kg[y][x]
    # print(Kred)

    #####################################Kred##################################
    for x in red:
        del p[x]
    P1 = np.zeros((5, 1))
    for i, x in enumerate(P1):
        x[0] = p[i]
    # print(P1)

    #####################################P1##################################
    Kred_1 = np.linalg.inv(Kred)
    # print(Kred_1)
    # print(P1)
    U = np.dot(Kred_1, P1)
    # print(U)

    U1 = np.zeros((8, 1))
    # print(U)
    # print(loop)

    for i, x in enumerate(loop):
        U1[x] = U[i]
    # print(U1)

    return U1

    #####################################U##################################


def WeAndSCal(ElemanP, u):
    SS = []
    WW = []
    result = []
    aa = [[4, 5, 2, 3],
          [6, 7, 2, 3],
          [0, 1, 2, 3],
          [0, 1, 4, 5],
          [0, 1, 6, 7]]

    for i, x in enumerate(aa):
        Re = ElemanP[i][0]
        Kr = ElemanP[i][1]
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

    result.append(WW)
    result.append(SS)
    return result


def LagerCal(kg, u):
    La = np.dot(kg, u)
    return La


def run(person, Resistance):

    info = infoMaker(person[0])
    red = RMaker(Resistance)
    p = person[1]

    element = elemanCr(info)
    kg = KgCal(element[0])
    u = UCal(kg, red, p)
    WS = WeAndSCal(element[1], u)
    Lager = LagerCal(kg, u)

    # print(Lager)

    result = {
        'ke': element[0],
        'element': element[1],
        'kg': kg,
        'u': u,
        'WS': WS,
        'Lager': Lager
    }
    return result
    # for i, x in enumerate(eleman[0]):
    #     if i == 1:
    #         print(f'{i + 1}\n{x}')

    # for i, x in enumerate(eleman[1][1]):
    #     print(f'{i + 1}\n{x}')
