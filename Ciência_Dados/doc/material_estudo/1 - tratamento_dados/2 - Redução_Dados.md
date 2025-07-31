# Introdução

# Objetivo da redução de dados 

### Por que reduzir dados?

- Redução do custo computacional 
    (Bases de dados podem ser extremamente volumosas)

    Algumas atributos ou colunas podem ter o mesmo sentido, exemplo: idade da pessoa e data de nascimente da pessoa, para minimizar o custo computacional, podemos ignorar ou até mesmo deleter, excluir uma dessas colunas ou atributos, pois as duas coisas passa a mesma informação (redundâncias)

- Eliminação de redundância

    Dados duplicados ou que possuem o mesmo valor semântico de informação.

- Evitar maldição da dimensionalidade 

    Em geral, na busca por melhores resultados na aprendizagem, modelagem e exploração,criam-se vetores (vetor de entrada) de características com mais informações para explicar alguma ação, evento ou fenômeno desnecessáriamente.

    Ou seja, precisamos evitar o excesso de atributos, configurações.

## O que é a maldição da dimensionalidade

## Estratégias para redução de dados

### Redução de dimensionalidade

Dimensões - Númetos de atributos que possuimos na basa, isto é, linhas, colunas dependendo da situação: tensor...

Eliminar - atributos pouco relevantes 

Reduzir -  tempo de processamento

Facilitar - visualização - Quantos mais dimensões, mais difícil é visualizar dados em um espaço cartesiano (altura, largura/ linhas e colunas) só vemos bém até 3 dimensões

Exemplo de dimensionalidade:
```python

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
print(np.arange(250000))
    
# criando um array (matriz de duas dimensões ) de quinhentas linhas com quinhentas colunas
matriz_2d = np.arange(250000).reshape(500,500)

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
``` 

**observações:** sempre que possível ou antes de tudo, nas técnicas de redução de dimensionalidade, remova os identificadores eles quase sempre irrelevantes, quando não atrapalham a análise de dados

**Ténicas para redução de dimensionalidade:**

PCA (Principal Components Analtsis)

### Seleção de atributos

- **Remoção** de atributos irrelevantes

    Pode ser feitas usando **matriz de correlação**

**Matriz de correlação simples**

|paramet| X    | Y    | Z    |
| ----- | ---- | ---- | ---- |
| **X** | 1.00 | 0.85 | 0.40 |
| **Y** | 0.85 | 1.00 | 0.30 |
| **Z** | 0.40 | 0.30 | 1.00 |

Uma matriz de correlação é uma tabela quadrada que mostra o nível de correlação estatística entre duas ou mais variáveis numéricas.

Em termos práticos:

    Cada linha e coluna representa uma variável.

    Cada célula mostra o coeficiente de correlação entre o par de variáveis.

    O coeficiente mais comum é o coeficiente de correlação de Pearson — varia de -1 a 1.

**o que isso significa?**

| Valor | Interpretação                                                        |
| ----- | -------------------------------------------------------------------- |
| 1     | Correlação **perfeita positiva** (as duas variáveis aumentam juntas) |
| 0     | **Sem correlação linear**                                            |
| -1    | Correlação **perfeita negativa** (uma aumenta, outra diminui)        |

Valores entre -1 e 1 indicam o grau de relação linear:

Próximo de 1: forte relação direta.

Próximo de -1: forte relação inversa.

Próximo de 0: relação linear fraca ou inexistente.

Por que usar?

Uma matriz de correlação é fundamental em:

    Análise exploratória de dados (EDA) → entender se variáveis estão relacionadas.

    Seleção de variáveis (feature selection) → descartar atributos redundantes.

    Detecção de multicolinearidade → em modelos estatísticos (ex: regressão linear).

- Seleção manual dos atributos

Usa-se quando há conhecimento profundo sobre os dados, normalmente com a participação de um especialista no negócio

- Seleção automático

Entre variáveis contínuas, pode-se usar correlação

### Amostragem 

### Compressão

## 7 técinas para redução da dimensionalidade

### Filtro por Proporção de Valores Ausentes (Missing Values Ratio)

Colunas de dados com muitos valores ausentes provavelmente carregam pouca informação útil. Assim, colunas de dados com quantidade de valores ausentes superior a um limite definido podem ser removidas. Quanto maior o limite, mais agressiva será a redução.

### Filtro de Baixa Variância (Low Variance Filter)

De forma semelhante à técnica anterior, colunas de dados com pouca variação carregam pouca informação. Portanto, todas as colunas de dados com variância inferior a um determinado limite são removidas. Atenção: a variância depende da faixa de valores; portanto, é necessário normalizar os dados antes de aplicar essa técnica.

### Filtro de Alta Correlação (High Correlation Filter)

Colunas de dados com tendências muito semelhantes provavelmente carregam informações redundantes. Nesse caso, apenas uma delas é suficiente para alimentar o modelo de aprendizado de máquina. Aqui calcula-se o coeficiente de correlação entre colunas numéricas (Coeficiente de Correlação Produto-Momento de Pearson) e entre colunas nominais (teste qui-quadrado de Pearson). Pares de colunas com coeficiente de correlação acima de um limite definido são reduzidos a apenas uma. Atenção: a correlação é sensível à escala; por isso, é necessário normalizar as colunas para que a comparação de correlação faça sentido.

### Florestas Aleatórias / Árvores de Decisão em Conjunto (Random Forests / Ensemble Trees)

Conjuntos de Árvores de Decisão, também conhecidos como Florestas Aleatórias (Random Forests), são úteis não apenas como classificadores eficazes, mas também para seleção de atributos. Uma abordagem de redução de dimensionalidade é gerar um conjunto grande e cuidadosamente construído de árvores contra um atributo-alvo e, em seguida, usar as estatísticas de uso de cada atributo para encontrar o subconjunto de atributos mais informativos. Especificamente, podemos gerar um conjunto grande (por exemplo, 2000) de árvores rasas (2 níveis), treinando cada árvore com uma fração pequena (3) do número total de atributos. Se um atributo é frequentemente selecionado como melhor divisão (split), é muito provável que seja uma característica informativa a ser mantida. Uma pontuação calculada com base nas estatísticas de uso dos atributos na floresta aleatória indica — em relação aos outros atributos — quais são os mais preditivos.

### Análise de Componentes Principais (Principal Component Analysis — PCA)

A Análise de Componentes Principais (PCA) é um procedimento estatístico que transforma ortogonalmente as n coordenadas originais de um conjunto de dados em um novo conjunto de n coordenadas, chamadas de componentes principais (principal components). Como resultado dessa transformação, o primeiro componente principal possui a maior variância possível; cada componente subsequente possui a maior variância possível, sob a restrição de ser ortogonal (isto é, não correlacionado) aos componentes anteriores. Manter apenas os primeiros m < n componentes reduz a dimensionalidade dos dados, preservando a maior parte da informação — isto é, a variabilidade dos dados. Atenção: a transformação PCA é sensível à escala relativa das variáveis originais; portanto, é necessário normalizar os intervalos das colunas antes de aplicar o PCA. Também é importante observar que as novas coordenadas (PCs) não são mais variáveis reais produzidas pelo sistema. Aplicar PCA em seu conjunto de dados faz com que ele perca interpretabilidade. Se a interpretabilidade dos resultados for importante para sua análise, o PCA não é a transformação indicada para o seu projeto.

### Eliminação Regressiva de Atributos (Backward Feature Elimination)

Nesta técnica, em uma dada iteração, o algoritmo de classificação selecionado é treinado com n atributos de entrada. Em seguida, removemos um atributo de entrada por vez e treinamos o mesmo modelo com n-1 atributos de entrada n vezes. O atributo cuja remoção provocar o menor aumento na taxa de erro é descartado, restando n-1 atributos. O processo é repetido usando n-2 atributos, e assim por diante. Cada iteração k produz um modelo treinado com n-k atributos e uma taxa de erro e(k). Definindo a taxa de erro máxima tolerável, determina-se o menor número de atributos necessários para alcançar aquele desempenho de classificação com o algoritmo de aprendizado de máquina escolhido.

### Construção Progressiva de Atributos (Forward Feature Construction)

Este é o processo inverso da Eliminação Regressiva. Começa-se com apenas 1 atributo, adicionando progressivamente mais 1 atributo por vez — ou seja, aquele que produzir o maior aumento no desempenho. Ambos os algoritmos (Eliminação Regressiva e Construção Progressiva) são computacionalmente caros e exigem muito tempo. Na prática, são aplicáveis apenas a conjuntos de dados que já possuem um número relativamente pequeno de colunas de entrada.

## Referências 

https://mineracaodedados.wordpress.com/2015/06/13/7-tecnicas-para-reducao-da-dimensionalidade/