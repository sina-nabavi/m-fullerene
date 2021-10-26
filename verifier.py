import math
import random

matching = ""

def consistency_first_layer():
    for iN in range(0, n):
        if matching[iN] == '0':
            if iN == 0:
                if matching[(iN + 1)] == '0':
                    print("first node")
                    print("first layer")
                    print("right")
                    print("unoccupied")
                    return -1
                if matching[(n - 1)] == '0':
                    print("first node")
                    print("first layer")
                    print("left")
                    print("unoccupied")
                    return -1
            elif iN == n-1:
                if matching[0] == '0':
                    print("last node")
                    print("first layer")
                    print("right")
                    print("unoccupied")
                    return -1
                if matching[iN - 1] == '0':
                    print("last node")
                    print("first layer")
                    print("left")
                    print("unoccupied")
                    return -1
            else:
                if matching[(iN + 1)] == '0':
                    print("first layer")
                    print("right")
                    print("unoccupied")
                    return -1
                if matching[(iN - 1)] == '0':
                    print("first layer")
                    print("left")
                    print("unoccupied")
                    return -1
            #inter edges
            if matching[((2 * n) + (2*iN))] == '0':
                print("first layer")
                print("inter")
                print("unoccupied")
                return -1
        elif matching[iN] == '3':
            if iN == 0:
                if matching[n - 1] != '1':
                    print("first node")
                    print("first layer")
                    print("left")
                    print("inconsistent")
                    return -1
            else:
                if matching[iN - 1] != '1':
                    print("first layer")
                    print("left")
                    print("inconsistent")
                    return -1

        elif matching[iN] == '1':
            if iN == n - 1:
                if matching[0] != '3':
                    print("last node")
                    print("first layer")
                    print("right")
                    print("inconsistent")
                    return -1
            else:
                if matching[iN + 1] != '3':
                    print("first layer")
                    print("right")
                    print("inconsistent")
                    return -1
        else:
            if matching[(2 * n) + (2*iN)] != '2':
                print("first layer")
                print("inter")
                print("inconsistent")
                return -1
    return 1


def consistency_last_layer():
    for iN in range(0, n):
        if matching[((2 * n) * (k + 2)) + iN] == '0':
            if iN == 0:
                if matching[(((2 * n) * (k + 2)) + iN + 1)] == '0':
                    print("first node")
                    print("last layer")
                    print("right")
                    print("onccupied")
                    return -1
                if matching[(((2 * n) * (k + 2)) + n - 1)] == '0':
                    print("first node")
                    print("last layer")
                    print("left")
                    print("onccupied")
                    return -1
            elif iN == n-1:
                if matching[(((2 * n) * (k + 2)))] == '0':
                    print("last node")
                    print("last layer")
                    print("right")
                    print("onccupied")
                    return -1
                if matching[(((2 * n) * (k + 2)) + iN - 1)] == '0':
                    print("last node")
                    print("last layer")
                    print("left")
                    print("onccupied")
                    return -1
            elif iN < (n - 1):
                if matching[(((2 * n) * (k + 2)) + iN + 1)] == '0':
                    print("last layer")
                    print("right")
                    print("onccupied")
                    return -1
                if matching[(((2 * n) * (k + 2)) + iN - 1)] == '0':
                    print("last layer")
                    print("left")
                    print("onccupied")
                    return -1
            #inter edge layers
            if k % 2 == 1:
                if matching[(((k + 2 - 1) * (2 * n)) + (2 * iN))] == '0':
                    print("last layer")
                    print("inter")
                    print("onccupied")
                    return -1
            else:
                if matching[(((k + 2 - 1) * (2 * n)) + (2 * iN) + 1)] == '0':
                    print("last layer")
                    print("inter")
                    print("onccupied")
                    return -1
        elif matching[((2 * n) * (k + 2)) + iN] == '3':
            if iN == 0:
                if matching[(((2 * n) * (k + 2)) + n - 1)] != '1':
                    print("first node")
                    print("last layer")
                    print("left")
                    print("inconsistenst")
                    return -1
            else:
                if matching[(((2 * n) * (k + 2)) + iN - 1)] != '1':
                    print("last layer")
                    print("left")
                    print("inconsistenst")
                    return -1
        elif matching[((2 * n) * (k + 2)) + iN] == '1':
            if iN == n - 1:
                if matching[(((2 * n) * (k + 2)))] != '3':
                    print("last node")
                    print("last layer")
                    print("right")
                    print("inconsistenst")
                    return -1
            else:
                if matching[(((2 * n) * (k + 2)) + iN + 1)] != '3':
                    print("last layer")
                    print("right")
                    print("inconsistenst")
                    return -1
        else:
            if k % 2 == 1:
                if matching[(((k + 2 - 1) * (2 * n)) + (2 * iN))] != '2':
                    print("last layer")
                    print("inter")
                    print("inconsistenst")
                    return -1
    return 1
        
def consistency():
    if (consistency_first_layer() == -1 ) or (consistency_rest_layers() == -1) or (consistency_last_layer() == -1):
        return -1
    return 1

def consistency_rest_layers():
    for iK in range(1, k + 2):
        for iN in range(0, 2*n):
            ##check for duality
            if matching[((2 * n) * (iK)) + iN] == '0':
                if iN == 0:
                    if matching[(((2 * n) * (iK)) + iN + 1)] == '0':
                        print("first node")
                        print("right")
                        print("unoccupied")
                        return -1
                    if matching[(((2 * n) * (iK)) + (2 * n) - 1)] == '0':
                        print("first node")
                        print("left")
                        print("unoccupied")
                        return -1
                elif iN == (2 * n) -1:
                    if matching[(((2 * n) * (iK)))] == '0':
                        print("last node")
                        print("right")
                        print("unoccupied")
                        return -1
                    if matching[(((2 * n) * (iK)) + iN - 1)] == '0':
                        print("last node")
                        print("left")
                        print("unoccupied")
                        return -1
                else:
                    if matching[(((2 * n) * (iK)) + iN + 1)] == '0':
                        print("right")
                        print("unoccupied")
                        return -1
                    if matching[(((2 * n) * (iK)) + iN - 1)] == '0':
                        print("left")
                        print("unoccupied")
                        return -1

                ## Inter Layer Edges
                
                if iK % 2 == 1:
                    if iN % 2 == 1:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] == '0':
                                print("inter")
                                print("unoccupied")
                                return -1

                    else:
                        if iK != 1:
                            if matching[(((2 * n) * (iK - 1)) + iN)] == '0':
                                print("inter")
                                print("unoccupied")
                                return -1

                else:
                    if iN % 2 == 1:
                        if matching[(((2 * n) * (iK - 1)) + iN)] == '0':
                            print("inter")
                            print("unoccupied")
                            return -1
                    else:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] == '0':
                                print("inter")
                                print("unoccupied")
                                return -1

            elif matching[((2 * n) * (iK)) + iN] == '3':
                if iN == 0:
                    if matching[(((2 * n) * (iK)) + (2 * n) - 1)] != '1':
                        print("first node")
                        print("left")
                        print("inconsistent")
                        return -1
                else:
                    if matching[(((2 * n) * (iK)) + iN - 1)] != '1':
                        print("left")
                        print("inconsistent")
                        print(((2 * n) * (iK)) + iN - 1)
                        return -1

            elif matching[((2 * n) * (iK)) + iN] == '1':
                if iN == (2 * n ) - 1:
                    if matching[(((2 * n) * (iK)))] != '3':
                        print("last node")
                        print("right")
                        print("inconsistent")
                        return -1
                else:
                    if matching[(((2 * n) * (iK)) + iN + 1)] != '3':
                        print("right")
                        print("inconsistent")
                        print(((2 * n) * (iK)) + iN - 1)
                        return -1
            
            else:
                if iK % 2 == 1:
                    if iN % 2 == 1:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] != '2':
                                print("inter")
                                print("inconsistent")
                                return -1

                    else:
                        if iK != 1:
                            if matching[(((2 * n) * (iK - 1)) + iN)] != '2':
                                print("inter")
                                print("inconsistent")
                                return -1

                else:
                    if iN % 2 == 1:
                        if matching[(((2 * n) * (iK - 1)) + iN)] != '2':
                            print("inter")
                            print("inconsistent")
                            return -1
                    else:
                        if iK != k + 1:
                            if matching[(((2 * n) * (iK + 1)) + iN)] != '2':
                                print("inter")
                                print("inconsistent")
                                return -1
    return 1

a = list(range(0,100))
def to_base_4(n):
    s = ""
    while n:
        s = str(n % 4) + s
        n //= 4
    return s
n = int(input("please enter the number of cycle nodes of m-barrel fullerene graph "))
k = int(input("please enter the number of layers of m-barrel fullerene graph "))

matching = "13130000130130131313"
if consistency() != -1:
    print("I have found a matching")
    print(matching)

