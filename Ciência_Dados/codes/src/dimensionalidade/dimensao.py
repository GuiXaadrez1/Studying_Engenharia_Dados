import numpy as np
import pandas as pd
import sys

# fazendo uma matriz 2d (tabela), com duas linhas
# o numpy realiza essa matriz com uma lista de listas
# ou uma lista de tuplas.

array_simples = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])

print(array_simples)
print() # print vazio só para quebrar linha

'''''
Saida: 
        [
            [ 1  2  3  4  5  6]
            [ 7  8  9 10 11 12]
        ]
'''

# Veja que temos duas dimensões: altura e largura 
# a largura tem 6 colunas 
# a altura tem duas linhas

# np.arange criando um array unidimensional numpy com 250 mil colunas em uma só linha
#print(np.arange(250000))
    
# criando um array (matriz de duas dimensões ) de quinhentas linhas com quinhentas colunas
#matriz_2d = np.arange(250000).reshape(500,500)

# desativar abreviação do array
np.set_printoptions(threshold = sys.maxsize)

#print(matriz_2d)

'''
Peguei uma parte da SAIDA:

    ...239890 239891 239892 239893 239894 239895 239896 239897 239898 239899   
    239900 239901 239902 239903 239904 239905 239906 239907 239908 239909
    239910 239911 239912 239913 239914 239915 239916 239917 239918 239919
    239920 239921 239922 239923 239924 239925 239926 239927 239928 239929
    239930 239931 239932 239933 239934 239935 239936 239937 239938 239939
    239940 239941 239942 239943 239944 239945 239946 239947 239948 239949
    239950 239951 239952 239953 239954 239955 239956 239957 239958 239959
    239960 239961 239962 239963 239964 239965 239966 239967 239968 239969
    239970 239971 239972 239973 239974 239975 239976 239977 239978 239979
    239980 239981 239982 239983 239984 239985 239986 239987 239988 239989
    239990 239991 239992 239993 239994 239995 239996 239997 239998 239999]
    [240000 240001 240002 240003 240004 240005 240006 240007 240008 240009... 
'''

# Veja que criamos um exemplo de dimensionalidade um pouco mais complexo
# não pelo conceito, mas pela quantidade de volume de dados, informações 
# que temaos ao criar certo evento para infomar uma certa coisa
# quanto mais vamos adicionando atributos, para justificar ou explicar um certo
# fenômeno, mais os nossos dados crescem, assim geramos a maldição da dimensionalidade
# impossibilitando a plena visualização dos dados de forma clara

# criando um tensor, isto é uma array de 3 ou mais dimensões
tensor = np.arange(250000).reshape(50,50,100)

print(tensor)

# Agora criamos um tensor que representa as dimensões 3D isto é: 
# altura, largura e profundidade

'''

Parte da Saida:
  ...249900 249901 249902 249903 249904 249905 249906 249907 249908 249909
   249910 249911 249912 249913 249914 249915 249916 249917 249918 249919
   249920 249921 249922 249923 249924 249925 249926 249927 249928 249929
   249930 249931 249932 249933 249934 249935 249936 249937 249938 249939
   249940 249941 249942 249943 249944 249945 249946 249947 249948 249949
   249950 249951 249952 249953 249954 249955 249956 249957 249958 249959
   249960 249961 249962 249963 249964 249965 249966 249967 249968 249969
   249970 249971 249972 249973 249974 249975 249976 249977 249978 249979
   249980 249981 249982 249983 249984 249985 249986 249987 249988 249989
   249990 249991 249992 249993 249994 249995 249996 249997 249998 249999]]]...
'''

# informando o tamanho do nosso tensor
print('\n',tensor.shape) # (50, 50, 100)

# quantidade total de elementos que existe nele
print(tensor.size) # 250000

# Veja que aumentamos ainda mais a quantidade de informações e atributos 
# para explicarmos determinada informação, ou evento, aumentando o nível de complexidade
# das nossas amostras e dificultando ainda mais as visualização plena e clara dos dados
# para podermos processar de forma eficiente no treinamento de modelos de Machine Learning
# Por isso que a redução de dimensões e volumes de dados é importante na
# análise e ciência de dados, para poupar tempo de execução, processamento e recursos
# computacionais.
