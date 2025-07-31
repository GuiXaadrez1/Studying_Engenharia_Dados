# Introdução

Em projetos de Ciência de Dados, Análise Estatística e Machine Learning, pré-processar os dados é uma etapa crítica para garantir qualidade, consistência e performance dos algoritmos.

Dois conceitos fundamentais nesse contexto são:

    Normalização: ajustar escalas de atributos numéricos.

    Discretização: transformar variáveis contínuas em categorias ou faixas de valores.

Essas técnicas visam eliminar distorções, reduzir viés causado por escalas diferentes e viabilizar algoritmos que requerem dados categóricos.


## O que é Normalização?

Normalização é o processo de ajustar a escala de um atributo numérico para um intervalo específico ou uma distribuição padronizada.

Por que fazer?

    Evitar que variáveis com magnitudes muito diferentes dominem o modelo.

    Acelerar convergência de algoritmos baseados em gradiente.

    Tornar resultados comparáveis entre atributos.

## Tipos de Normalização Mais Comuns

### ⚙️ 3.1 Min-Max

Descrição: Reescala os valores originais para um novo intervalo definido [ nmin, nmax ]

    v'= ( v - min / max - min  ) * ( nmax − nmin ) + nmin

Exemplo:

    Suponha valores entre 12.000 e 98.000. Queremos normalizar para [0, 1]:

    v' = 73.600 ⇒ v'= (  73.600−12.000 / 98.000−12.000 ) * (1−0) + 0 = 0,716

Observação prática:

    Mantém proporção original, mas não elimina outliers.

### Z-Score (Padronização)

Descrição: Reescala os dados para uma distribuição normal padrão — média 0 e desvio padrão 1.

Fórmula:

   v' = ( v - μ / σ )
​  
- μ = média aritmética
    
- σ = desvio padrão

Exemplo: Idade média: 35 anos, desvio padrão: 12. Para idade = 50:

    v′ = (50−35/12) = 1,25

Observação prática:

Útil quando o modelo assume distribuição normal (ex: regressão logística, SVM linear).

### Escala Decimal

Descrição: Desloca a casa decimal dos valores até que fiquem dentro de um intervalo menor que 1.

Fórmula:

    v′ = (v/10^j)

Onde: j é o menor inteiro tal que ∣v′∣ < 1.

Exemplo: Valor máximo do atributo = 5.000. Então:

j = 4 (pois 5.000/10^4 = 0,5)

v = 2.450 ⟶ 𝑣′ = 0,245 

Observação prática:

Simples, mas não considera distribuição. Útil para pré-processar grandes magnitudes.
​
## Discretização

### O que é Discretização?

A discretização transforma atributos numéricos contínuos em categorias ou intervalos.

Usada quando algoritmos só aceitam dados categóricos.

Também facilita interpretação e descoberta de padrões, como regras de associação.

### Como Funciona?

Escolhe-se os intervalos (bins) — fixos, quantis ou baseados em alguma heurística.

Cada valor é mapeado para o intervalo correspondente.

O valor contínuo original é substituído por uma etiqueta de faixa.

### Exemplo Prático

Atributo: idade

Intervalos definidos:

```bash
    (0, 20], (20, 30], (30, 40], (40, 50], (50, 65], (65, 80], (80, ∞]
```

| Idade Original | Intervalo |
| -------------- | --------- |
| 18             | (0, 20]   |
| 29             | (20, 30]  |
| 67             | (65, 80]  |


### Função de Discretização

Em pseudo-código, uma função de discretização pode ser:

```python

def discretizar_idade(idade):
    if idade <= 20:
        return "(0, 20]"
    elif idade <= 30:
        return "(20, 30]"
    elif idade <= 40:
        return "(30, 40]"
    elif idade <= 50:
        return "(40, 50]"
    elif idade <= 65:
        return "(50, 65]"
    elif idade <= 80:
        return "(65, 80]"
    else:
        return "(80, ∞]"


resultado = discretizar_idade(45)
print(resultado) # "(40, 50]"
```

## Resumo — Quando Usar

| Técnica            | Para quê?                                                                                                        |
| ------------------ | ---------------------------------------------------------------------------------------------------------------- |
| **Min-Max**        | Garantir intervalo definido. Ideal para redes neurais.                                                           |
| **Z-Score**        | Assumir distribuição normal, padronizar atributos.                                                               |
| **Escala Decimal** | Reduzir ordem de grandeza de forma simples.                                                                      |
| **Discretização**  | Transformar atributos contínuos em categorias. Ideal para regras de associação, árvores de decisão, Naive Bayes. |

## Recomendações Avançadas

Verifique outliers antes de normalizar.

Nunca normalize variáveis categóricas.

Discretização perde informação de precisão — avalie se isso impacta o seu modelo.

Em pipelines reais, combine Sklearn (MinMaxScaler, StandardScaler, KBinsDiscretizer) com Pandas para maior contro

