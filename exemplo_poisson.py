## codigo  referente  ao  exercicio  23 ##

import math # biblioteca  para  realizar  as  operacoes  de  fatorial e exponencial

media = 3.87  # media  das  distribuicoes
A = 2608 # normalizacao

f_exp = [57,203,389,525,532,408,273,139,45,27,10,6] # valores medidos
f_teo = [] # criar  uma  lista  vazia

for m in range(0,12):
    f_teo.append(A * media**( m )/( math.factorial( m ) ) * math.exp( - media ) )
# o loop "for" calcula  para  cada  valor de m indo 0 ate 11 as  frequencias e guarda  na lista f com o atributo "append"   

import numpy as np # importa a biblioteca numpy para facilitar os calculos

chi2 = ( np.array( f_exp ) - np.array( f_teo ) ) **2/ np.array( f_teo )
print( chi2.sum() ) # o chi quadrado de fato e caculado aqui, quando somamos todas as contribuicoes

from scipy.stats import chisquare # biblioteca para importada para o calculo do chi2
print( chisquare( f_exp,f_teo ) ) # podemos checar o valor com a funcao chisquare do scipy.stats
