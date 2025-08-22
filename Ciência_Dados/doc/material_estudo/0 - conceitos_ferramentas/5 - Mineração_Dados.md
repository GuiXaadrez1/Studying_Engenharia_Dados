# Introdução

Este arquivo tem como objetivo explicar o que é mineração de dados, características de uso, exemplos, o que sãõ padrões, probabilidade de detecção de padrões. 

## O que é KDD (Knowledge Discovery in Databases):

É o processo de extração não trivial de conhecimento previamente desconhecido e potencialmente útil de bases de dados.

Dados -> Seleção -> Dados de destino -> Pré-processamento -> Dados pré-processados (ETL) -> transformação -> Dados transformação -> Mineração de Dados -> Padrões -> Interpretação/Avaliação -> Conhecimento ->  Tomada de decisão -> Ação.

## Contexto de cada etapa do KDD


## No  processo KDD:

Á mineração de dados afim de encontrar padrões é uma importante etapa no fluco de KDD que consiste na aplicação de técnicas computacionais para descoberta de padrões relevantes em grandes conjuntos de dados.

## Especificação sobre Mineração de dados (MD) Data mining

MD envolve obrigatoriamente:

- Conhecimento de negócio;

- Técnicas adequadas para cada tipo de problema

- Infraestrutura de TIC (hardware, softaware, rede)

Mineração de dados constitui um processo bem mais proximo da pesquisa e investigação do que do desenvolvimento de software.

Em cenários de grandes volumes de dados, soluções adotadas devem atender a requisitos rígidos de escalabilidade. 

**Nem tudo se resolve com mais recursos de hardware (capacidade de processamento.)**

Processo de exploração de dados á procura de padrões consistentes para detectar relacionamentos sistemáticos entre variáveis.

Esses relacionamentos vão procurar responder: 

- Por que determinados clientes são mais rentáveis?

- Qual tipo de cliente terá interesse pelo meu novo produto?

- Quais clientes podem ir para meus competidores? 

- Quais os hábitos de meus clientes?

Normalmente esses relacionamentos vão ser procurados a serem respondidos por um modelo matémático:

- Abstração: metemática que representa um comportamento;
- Normalmente uma função, y = f(x).

### O que são padrões?

Observe atentamente a sequência de letras abaixo e tente encontrar alguma característica marcante:

ABCXYABCZKABDKCABCTUABEWLABCWO

- Passo 1 -> A primeira etapa é perceber que existe uma sequência de letras que se repete bastante. Encontramos as sequências "AB" e "ABC" e observamos que elas ocorrem com frequência superior á das outras sequências.

**Com uso de REGEX achar padrões em caracteres é mais fácil, rsrsrs**.

- Passo 2 -> Após determinarmos as sequências "ABC" e "AB". verificamos que elas segmentam o padrão original em diversas unidades independentes.

ABCXY ABCZK ABDKC ABCTU ABEWL ABCWO

- Passo 3 -> Podemos fazer induções, que geram algumas representações genéricas dessas unidades.

ABC?? ABD?? ABE?? AB???

podemos induzir quais são as letras com mais probabilidade de aparecer na sequência.

Suponha que a sequência represente o histórico de compras de um cliente em um supermecado, e que a ocorrência de: 

A significa "pão";
B significa "leite";
C indica que o leite é do tipo "desnatado".

A descoberta de uma regra com letras AB significa que toda vez que este cliente comprar pão, também compra leite. 

Os atributos foram associados por um processo de reconhecimento de padrões. 


## MD é um processo iterativo:

Mineração de dados é um processo iterativo que possui o seguinte ciclo:

Modelos:

algoritmos:

sistemas:
 
aplicações:

Relevância:

Utilidade dos padrões: 

Expressividade dos Modelos:

Escalabilidade e Eficiência:

## Links para estudos mais aprofundados

https://mooc41.escolavirtual.gov.br/pluginfile.php/6057989/mod_page/content/14/Chapter1_introduction_knowledge_discovery_in_databases.pdf?time=1718987148616

https://en.wikipedia.org/wiki/Data_mining

