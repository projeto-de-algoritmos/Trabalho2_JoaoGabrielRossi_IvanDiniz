import random
import pygame
A = []
D = []
verificador = 1
pipu = 0
n = int(input("Escolha o numero maximo de vértices"))
while n > 0:
    g = [[0] * n for i in range(n)]
    count0 = [0] * n
    while verificador == 1:
        # generating random graph
        for i in range(n):
            for j in range(5):
                v1 = random.randint(0, n - 1)
                v2 = random.randint(0, n - 1)
                if v1 > v2:
                    g[v1][v2] = 1
                elif v1 < v2:
                    g[v2][v1] = 1


        for p in range(n):
            for z in range(n):
                #print("{0}".format(g[p][z]), end = " ")
                if g[p][z]==1:
                    count0[z]+=1
            #print('\n')

        # throwing initial vertexes with 0 count0 into lists
        for i in range(n):
            if count0[i] == 0:
                A.append(i)
                D.append(i)
                pipu += 1
                # print("haahha{0}".format(i))

        i=0
        # topological order
        #for f in range(n):
            #print("count0[{0}] = {1}".format(f, count0[f]))
            #print("\n")
        while (len(A) != 0):
            c = A[0]
            i+=1
            print("Hello hello{0} and i = {1}".format(c, i))
            A.remove(c)


            for o in range(n):
                # print("iello{0}".format(0))
                if g[c][o] == 1:
                    #print("count0[{0}] = {1}".format(o, count0[o]))
                    count0[o] = count0[o] - 1
                    #print("count0[{0}] = {1}".format(o,count0[o]))
                    if count0[o] == 0:
                        #print("ok{0}".format(o))
                        A.append(o)
                        D.append(o)
                        pipu += 1
                #for f in range(n):
                    #print("count0[{0}] = {1}".format(f, count0[f]))
                #print("\n")
        # if not topological reset everything and try again
        if pipu != n:
            print("nooooooooooooooooooo")
            for u in range(n):
                count0[u] = 0
                pipu = 0
                for j in range(n):
                    g[i][j] = 0
            A.clear()
            D.clear()
            continue
        else:
            print("uyeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
            verificador = 0

    while True:
        tentativa = int(input("Enter your choice"))
        print(tentativa)
        print(D[0])
        if tentativa != D[0]:
            print("Voce perdeu otario")
            break
        else:
            D.remove(D[0])
        if len(D) == 0:
            print("You Won")
            break
    # reset
    verificador = 1
    for u in range(n):
        count0[u] = 0
        pipu = 0
        for j in range(n):
            g[i][j] = 0
        A.clear()
        D.clear()
    n = int(input("Faça outra escolha de tamanho total de vertices"))


