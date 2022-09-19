def coloca_gap(dna, posicao):
    base = dna[posicao]
    dna[posicao] = '-'
    dna.append(0)

    cont = -1
    while (dna[cont] != '-'):
        dna[cont] = dna[cont-1]
        cont -=1

    dna[posicao+1] = base
    return dna


dna1 = ['a','c','b','d']
dna2 = ['d','c','b','a']
# dna1 = ['a','b','c','d']
# dna2 = ['b','d','a','b']
dna3 = ['b','d','c','a']
dna4 = ['d','a','c','b']
dna = [dna1, dna2, dna3, dna4]

"""
a b c d
a d b c
b a c d 
c a d b 
a c b d

a b c d
a - - d b c
- - - - b a c d
- - - - - - c a d b
- - - - - - - a c b d
"""

#A,C,T,G 

for i in range(0, len(dna)):
    try:
        
        dna1 = dna[i]
        dna2 = dna[i+1]

        cont = 0 
        p = len(dna1)

        while (cont < p):
            base1 = dna1[cont]
            base2 = dna2[cont]
            
            if (base1 != base2):
                print(dna1)
                print(dna2)
                print('\n')
                try:
                    jumps = 1
                    aux = dna1[cont+jumps]

                    while (base2 != aux): 
                        jumps += 1
                        aux = dna1[cont+jumps]
                    #se eu colocar 1 gap, ou seja, mover uma parte do dna para direita, iguala a base
                    # if (base2 == aux):
                    dna2 = coloca_gap(dna2, cont)
                except:
                    pass
            cont += 1
        dna[i+1] = dna2
        
    except:
        pass

for i in dna:
    print(i)