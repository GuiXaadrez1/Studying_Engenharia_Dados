# Introdução 
Este documento visa explicar de forma suncinta a respeito da técnica de limpeza de dados 

## O que é limpeza de dados 

A limpeza de dados é um processo essencial para preparar dados brutos para aplicações de machine learning (ML) e business intelligence (BI). Dados brutos podem conter vários erros, que podem afetar a precisão dos modelos de ML e levar a previsões incorretas e causar um impacto negativo nos negócios. 

As principais etapas da limpeza de dados incluem: 
    
- modificar e remover campos de dados incorretos ou incompletos.

- identificar e remover informações duplicadas ou dados não relacionados e corrigir formatação.

- valores ausentes ou erros de ortografia.

Para chegar a resultados consistentes e confiáveis a partir de uma análise de dados é fundamental que a base satisfaça algumas condições – exigidas pelo formalismo matemático e pelos algoritmos que sintetizam a informação de caráter quantitativo (OLIVEIRA, GRECO e BRANDÃO, 2015), uma vez que estimativas apontam que cerca de 40% dos dados coletados estão comprometidos de alguma forma (FAYYAD, 2003).

Na etapa de limpeza (alcunhada por alguns autores como pré-processamento) são identificadas as anomalias e discrepâncias que podem vir a comprometer a análise. Para tal, é necessário partir de uma inspeção criteriosa da base de dados, identificando as inconsistências e procedendo com as medidas necessárias para sua adequação. Nesta primeira etapa já é possível unir métodos estatísticos aos recursos de detecção de anomalias, para chegar aos valores que devem ser manipulados e, por fim, definir a melhor estratégia para lidar com eles.

O processo de limpeza de uma base de dados, entretanto, não deve se limitar à resolução das inconsistências, podendo também atuar no enriquecimento da base. A agregação ou desagregação de um número de telefone (DDD e número de telefone) ou um endereço (logradouro, número, bairro, CEP, cidade e estado), por exemplo, pode melhorar o processamento e a visualização dos dados.

### Alguns exemplos de tarefas executadas durante a limpeza (ou pré-processamento) dos dados são:

1. **A exclusão ou substituição de valores duplicados.** Podemos dizer que redundâncias em uma base de dados podem gerar alguns conflitos que comprometerão a análise, colocando em risco a confiabilidade de todos os resultados obtidos. Se, por exemplo, você estiver lidando com dados transacionais relacionados a uma base de 200 cadastros de clientes, onde 5 estão duplicados – resultando em 10 registros redundantes – cada venda realizada pode ser atribuída a um cadastro de cliente diferente, gerando um problema no momento de analisar as transações;

2. **A identificação, exclusão ou tratamento de valores nulos ou inconsistentes.** Em muitos casos, registros nulos sequer serão considerados pelas ferramentas que darão suporte ao processo, fazendo com que retornem erro, incapacitando a condução de análises. Os valores inconsistentes – que podem ser, por exemplo, registros alfanuméricos preenchidos em campos exclusivamente numéricos – também podem resultar em erros na etapa do processamento ou da transformação dos dados;

3. **A adequação na distribuição dos dados, a partir da identificação e do tratamento de valores atípicos ou aberrantes (muito superiores ou muito inferiores ao que pode ser encontrado na maior parte dos registros da base de dados – também chamados de outliers).** A ocorrência de registros aberrantes pode acabar por enviesar os resultados. Um exemplo de problema que pode ser enfrentado caso não sejam removidos ou tratados os outliers é o impacto do registro aberrante na aferição da média dos valores da variável impactada.

É importante lembrar que a limpeza dos dados também faz parte do controle de qualidade e, por isso, podemos concluir que este pré-processamento figura como uma etapa essencial para que os resultados de uma análise sejam confiáveis.

Negligenciar este passo pode comprometer total ou parcialmente as etapas subsequentes da análise de dados, portanto, recomenda-se que o processo seja conduzido com muita atenção e de forma criteriosa, para que as técnicas de limpeza sejam aplicadas considerando o valor estratégico dos dados trabalhados e o cerne da questão que mobiliza o esforço analítico.

Antes de aplicarmos qualquer técnica de limpeza de dados é necessário buscar em cada coluna os valores dos dados coletados que seguem o seguinte badrão abaixo.

### O Dados podem estar e quase sempre estarão:

- Incompletos

    Atributos ausentes;
    Valores de atributos ausentes;
    Dados agregados (frequente em DWs);

- Com ruídos 
    
    Erros ( idade = - 50 error! );
    Outliers (valores discrepantes);

- Inconsistentes 

**Exemplo:**

    idade = 43 e data nascimento = 03/07/1997;
    atributos com valores: "1,2,3" para assumir "a,b,c";

### Observações

É sempre importante criar gráficos de dispersão, histogramas, métricas estatística como: 
    
    média, moda, mediana, minímo, máximo, desvio padrão para a identificação destas inconsistências

Causas mais comuns para dados ausentes: 

- Mau funcionamento de equipamentos
- Dado originalmente não foi considerado importante
- Dado inconsistente, geralmente são removidos da base
- NO caso do banco de dados, modelagem física mal feita e etc... 

Como tratar? 

- Ignorar registro ou atributo
- Preencher valores de forma manual, ou seja, manualmente
- Preencher valores automaticamente:

    Seguindo estes parâmetros - Constante, mediana, média dos vizinhoa, média global, média de registros da mesma classe, métodos de aprendizado de máquina.

**Sempre que fizer uma análise exploratória, isto é, explorar os dados e colunas dos nossos arquivos a serem analisados é interessante descobrir qual é o seu tipo de dado para quem é de banco de dados, domínio predominante naquela momento a fim de fazermos casting ou seja, mudar o tipo dado daquela dado rsrsrs...**

Exemplo:
```python
    # estou criando um script em python usando pandas como exemplo

    import pandas as pd

    # criando uma dicionário de dados

    dados = {
        'Nome':['Guilherme','Maria','João'],
        'Idade':[20,25,30]
    }

    # OBSERVAÇÃO, DICIONÁRIO CRIA DATAFRAME E LISTAS SERIES 
    # UMA COLUNA É UMA SERIE, UM DATAFRAME É UMA COLEÇÃO DE SERIES

    # criando um DataFrame utilizandoo nosso dicionário de dados
    df = pd.DataFrame(dados)

    print(type(df)) # vai retornar um DataFrame como tipo de dado

    # para ser uma Series

    print(type(df['Idade'])) # saída -> <class 'pandas.core.series.Series'>

    # para ser o valor que aquela Series comporta

    print(type(df['Idade'][1])) # saida -> <class 'numpy.int64'> 

    # logo descobrimos que a coluna idade comporta tipo de dados do numpy int64  bytes     

    # Para fazer o casting, isto é, converter toda a coluna 
    # do DataFrame original para strinf podemos fazer o seguinte

    df['Idade'] = df['Idade'].astype(str)

    # estamos atribuindo uma nova coluna com todos os seu valores string para a coluna 
    # 'idade' do nosso DataFrame, neste caso implícitamente estamos sobrescrevendo
    # e realizando o casting

    print(type(df['Idade'][1])) #saida -> <class 'str'> 

```

**Com base no exemplo acima, podemos constatar que é sempre interessante dar uma olhada nos atributos, colunas, tipos de dados para determinados a qualidade dos dados que estamos analisando e manipulando.**

## Tipos de limpeza de dados

## Como fazer uma limpeza de dados


## Referências:

- https://ibpad.com.br/comunicacao/uma-visao-geral-sobre-a-limpeza-dos-dados/
- https://aws.amazon.com/pt/what-is/data-cleansing/
