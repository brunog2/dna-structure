dna1 = ['a','b','c','d']
dna2 = ['b','d','a','b']
dna3 = ['a','d','c','a']
dna4 = ['d','a','c','b']

#A,C,T,G 

dna = [dna1, dna2,dna3,dna4]


def coloca_gap(dna,posicao):
    base = dna[posicao]
    dna[posicao] = '-'
    dna.append(0)

    cont = -1
    while (dna[cont] != '-'):
        dna[cont] = dna[cont-1]
        cont -=1

    dna[posicao+1] = base
    return dna


for i in range(0,len(dna)):
    try:
        
        dna1 = dna[i]
        dna2 = dna[i+1]

        cont = 0 
        p = len(dna1)

        while (cont < p):
            base1 = dna1[cont]
            base2 = dna2[cont]
            
            if(base1 != base2):
                try:
                    aux = dna1[cont+1]
                    if(base2 == aux):
                        #se eu colocar 1 gap, ou seja, mover uma parte do dna para direita, iguala a base
                        dna2 = coloca_gap(dna2,cont)
                except:
                    pass
            cont += 1
        dna[i+1] = dna2
        
    except:
        pass

for i in dna:
    print(i)