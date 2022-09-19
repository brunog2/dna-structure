
alfabeto = {'q':1,'w':2,'e':3,'r':4,'t':5,'y':6,'u':7,'i':8,'o':9,'p':10,'á':11,'ã':12,'a':11,'s':9,'d':7,'f':5,
'g':3,'h':1,'j':11,'k':9,'l':7,'ç':5,'é':3,'í':1,'z':2,'x':4,'c':6,'v':8,'b':10,'n':12,'m':2,'ó':4,'õ':6,'ô':8,'â':10,'ê':12}

first_name = input('Digite o primeiro nome: ').lower()

def subs_name(name):
    subs = ''
    for i in name:
        subs += str(alfabeto[i])
    return subs

subs_first_name = subs_name(first_name)

calc = int(subs_first_name) % 3

alfa = 0
beta = 0
gamma = 0

if(calc==0):
    alfa = 1
    beta = 0
    gamma = -1
elif(calc ==1):
    alfa = 2
    beta = 0
    gamma = -1
elif(calc == 2):
    alfa = 1
    beta = 0
    gamma = -2

last_name = input('Digite o último nome: ').lower()

subs_last_name = subs_name(last_name)

calc = int(subs_last_name) % 3

gaps = ''

if(calc == 0):
    gaps = 'Preferencialmente no início da sequência'
elif(calc == 1):
    gaps = 'Preferencialmente no final da sequência'
elif(calc == 2):
    gaps = 'Preferencialmente no final da sequência'


middle_name = input('Digite o nome do meio: ')

subs_middle_name = subs_name(middle_name).lower()

calc = int(subs_middle_name) % 2

space_gaps = ''

if(calc == 0):
    space_gaps = 'Gaps Juntos'
else:
    space_gaps = 'Gaps Separados'