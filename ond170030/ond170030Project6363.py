import sys


class Jewel:
    def __init__(self, weight, profit, minQuantity, maxQuantity, fine, cap):
        self.weight = weight
        self.profit = profit
        self.minQuantity = minQuantity
        self.maxQuantity = maxQuantity
        self.fine = fine
        self.cap = cap

    def toString(self):
        print(self.weight, self.profit, self.minQuantity, self.maxQuantity, self.fine, self.cap)


class Pair:
    def __init__(self, p, n):
        self.p = str(p)
        self.n = str(n)
        print(self.p + " " + self.n)


def Process(G, jewl, nItems):
    # print(G, n)
    # r = (nItems+1)*[(G+1)*[0]]
    r = [[0 for j in range(0, G + 1)] for i in range(0, nItems + 1)]
    cnt = [[0 for j in range(0, G + 1)] for i in range(0, nItems + 1)]
    for x in range(0, G + 1):
        cnt[0][x] = 1
    # print(r)

    # Optimal Solution
    for i in range(1, nItems + 1):
        for k in range(0, G + 1):
            # profit[i][k] = i
            w = jewl[i].weight
            p = jewl[i].profit
            n = jewl[i].minQuantity
            x = jewl[i].maxQuantity
            f = jewl[i].fine
            c = jewl[i].cap
            localMax = -sys.maxsize
            for q in range(0, x + 1):
                if k - w * q >= 0:
                    if n > q:
                        # deficit
                        r[i][k] = (p * q - min(f * (n - q), c) + r[i - 1][k - w * q])
                        # if r[i][k] == r[i-1][k-w*q] + p*q - min(f*(n-q), c):
                        #     c[i][k] = c[i][k] + c[i-1][k-w*q]

                    else:
                        # no deficit
                        r[i][k] = (p * q + r[i - 1][k - w * q])
                        # if r[i][k] == r[i-1][k-w*q] + p*q:
                        #     c[i][k] = c[i][k] + c[i-1][k-w*q]
                    localMax = max(r[i][k], localMax)
                r[i][k] = localMax
    # print(r[nItems][-1])

    # counting solutions
    # print(c)
    for i in range(1, nItems + 1):
        for k in range(0, G + 1):
            # profit[i][k] = i
            w = jewl[i].weight
            p = jewl[i].profit
            n = jewl[i].minQuantity
            x = jewl[i].maxQuantity
            f = jewl[i].fine
            c = jewl[i].cap
            for q in range(0, x + 1):
                if k - w * q >= 0:
                    if n > q:
                        # deficit
                        if r[i][k] == p * q - min(f * (n - q), c) + r[i - 1][k - w * q]:
                            cnt[i][k] = cnt[i][k] + cnt[i - 1][k - w * q]
                    else:
                        # no deficit
                        if r[i][k] == p * q + r[i - 1][k - w * q]:
                            cnt[i][k] = cnt[i][k] + cnt[i - 1][k - w * q]
    # print("#Output: ")
    Pair(r[nItems][-1], cnt[-1][-1])
    try:
        if arguments[2] == 0:
            pass
            # print("Yes the second argument is zero")
        elif int(arguments[2]) > 0:
            # list of element Quantities
            s = [0 for x in range(0, nItems + 1)]
            # print("#List of Optimal Solutions: ")
            enumerate(s, nItems, G, jewl, r)
    except IndexError:
        pass
        # print("No second argument")
    # return Pair(0,0)


def enumerate(s, i, G, jewl, r):
    # print(s, i, G)
    if i == 0:
        for x in s[1:]:
            print(x, end=" ")
        print()
    else:
        w = jewl[i].weight
        p = jewl[i].profit
        n = jewl[i].minQuantity
        x = jewl[i].maxQuantity
        f = jewl[i].fine
        c = jewl[i].cap
        for q in range(0, x + 1):
            if (G - w * q >= 0):
                if n > q:
                    # deficit
                    if r[i][G] == p * q - min(f * (n - q), c) + r[i - 1][G - w * q]:
                        s[i] = q
                        enumerate(s, i - 1, G - w * q, jewl, r)
                else:
                    # no deficit
                    if r[i][G] == p * q + r[i - 1][G - w * q]:
                        s[i] = q
                        enumerate(s, i - 1, G - w * q, jewl, r)


if __name__ == "__main__":
    # print(sys.argv)
    arguments = sys.argv
    jewl = list()
    jewl.append(Jewel(0, 0, 0, 0, 0, 0))
    if len(arguments) == 1 or (len(arguments) == 2 and arguments[1] == "-"):
        # parameter from command line
        # print("Input ->")
        G, nItems = input().split(" ")
        G = int(G)
        nItems = int(nItems)
        for z in range(nItems):
            i, w, p, n, x, fine, cap = input().split(" ")
            i = int(i)
            w = int(w)
            p = int(p)
            n = int(n)
            x = int(x)
            fine = int(fine)
            cap = int(cap)
            j = Jewel(w, p, n, x, fine, cap)
            jewl.append(j)
        # print(G, nItems)
        # print(type(jewl))
        # print(len(jewl))
        # jewl[1].toString()
        # jewl[2].toString()
    elif len(arguments) >= 2:
        # print(arguments)
        # File input
        # file = arguments[1]
        # print("Filename->", file)
        file = open(arguments[1], "r")
        G, nItems = file.readline().split(" ")
        # print(G, nItems)
        G = int(G)
        nItems = int(nItems)
        for z in range(nItems):
            i, w, p, n, x, fine, cap = file.readline().split(" ")
            i = int(i)
            w = int(w)
            p = int(p)
            n = int(n)
            x = int(x)
            fine = int(fine)
            cap = int(cap)
            j = Jewel(w, p, n, x, fine, cap)
            jewl.append(j)
        # for x in range(1, nItems + 1):
        #     jewl[x].toString()
    # G, nItems = input().split(" ")
    # G = int(G)
    # nItems = int(nItems)
    # jewl = list()
    # jewl.append(Jewel(0, 0, 0, 0, 0, 0))
    # for x in range(nItems):
    #     i, w, p, n, x, fine, cap = input().split(" ")
    #     i = int(i)
    #     w = int(w)
    #     p = int(p)
    #     n = int(n)
    #     x = int(x)
    #     fine = int(fine)
    #     cap = int(cap)
    #     j = Jewel(w, p, n, x, fine, cap)
    #     jewl.append(j)
    # # print(G, nItems)
    # # for x in range(1, nItems+1):
    # #     jewl[x].toString()
    # # print("Length of Jewel ",len(jewl))
    Process(G, jewl, nItems)

# Test case 1
# 20 2
# 1 2 10 8 10 2 2
# 2 2 10 8 10 2 4


# Test case 2
# 50080 2
# 1 81 4050 913 1227 405 4050
# 2 63 3150 416 4213 315 3150

# Test case 3
# 55645 3
# 1 70 1400 937 2370 140 280
# 2 66 1320 575 4622 132 1320
# 3 49 980 726 2968 98 980

# Test case 4
# 18682 9
# 1 51 5049 55 3644 504 5040
# 2 86 8514 26 645 851 1702
# 3 81 8019 31 1437 801 8010
# 4 50 4950 50 3732 495 4950
# 5 66 6534 24 2944 653 1306
# 6 75 7425 13 1162 742 7420
# 7 97 9603 74 4425 960 1920
# 8 45 4455 52 578 445 890
# 9 80 7920 57 4319 792 1584

# Test case 5
# 38928 40
# 1 54 648 26 2465 64 640
# 2 47 564 2 4928 56 112
# 3 89 1068 19 1828 106 212
# 4 54 648 40 2908 64 128
# 5 55 660 18 972 66 132
# 6 42 504 34 2120 50 500
# 7 90 1080 38 2044 108 1080
# 8 47 564 11 764 56 112
# 9 76 912 33 1645 91 182
# 10 92 1104 22 2853 110 220
# 11 58 696 30 4848 69 138
# 12 47 564 9 4279 56 560
# 13 94 1128 26 2448 112 1120
# 14 98 1176 30 211 117 1170
# 15 62 744 2 1427 74 148
# 16 49 588 3 2772 58 580
# 17 89 1068 32 1095 106 1060
# 18 88 1056 10 3918 105 1050
# 19 78 936 12 3976 93 186
# 20 99 1188 32 1418 118 1180
# 21 61 732 26 3810 73 730
# 22 67 804 14 605 80 800
# 23 91 1092 35 3948 109 1090
# 24 75 900 14 868 90 180
# 25 64 768 32 3528 76 152
# 26 52 624 4 2331 62 124
# 27 40 480 37 3514 48 480
# 28 53 636 40 4508 63 630
# 29 73 876 35 2501 87 870
# 30 66 792 32 1556 79 790
# 31 40 480 4 2062 48 480
# 32 72 864 32 2708 86 860
# 33 83 996 9 3051 99 990
# 34 40 480 31 2351 48 96
# 35 84 1008 15 3906 100 1000
# 36 51 612 34 1101 61 610
# 37 56 672 14 74 67 134
# 38 97 1164 36 4089 116 1160
# 39 64 768 32 3520 76 760
# 40 54 648 36 1836 64 640
