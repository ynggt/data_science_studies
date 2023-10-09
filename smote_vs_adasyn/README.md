# Comparando SMOTE e ADASYN para o Tratamento de Desequilíbrio de Classes em Aprendizado de Máquina #

### Introdução ### 

O desequilíbrio de classes é um desafio comum no aprendizado de máquina, onde uma classe tem significativamente menos instâncias do que outra. Isso pode levar a modelos enviesados que têm um desempenho ruim na classe minoritária. Técnicas de oversampling como o SMOTE (Synthetic Minority Over-sampling Technique) e o ADASYN (Adaptive Synthetic Sampling) são usadas para lidar com esse problema. Este repositório explora as diferenças entre o SMOTE e o ADASYN e seu impacto em algoritmos de classificação.

#### SMOTE (Synthetic Minority Over-sampling Technique) ####
O SMOTE funciona criando amostras sintéticas para a classe minoritária. Ele seleciona uma instância aleatória da classe minoritária, identifica seus k vizinhos mais próximos e gera instâncias sintéticas ao longo dos segmentos de linha que os conectam. Esse processo aumenta a representação da classe minoritária.

##### ADASYN (Adaptive Synthetic Sampling) ####
O ADASYN adapta a geração de amostras sintéticas com base na distribuição de densidade da classe minoritária. Ele identifica instâncias que são mais difíceis de aprender, considerando as razões de classificação incorreta. Ele gera amostras sintéticas com maior densidade em regiões desafiadoras, enfatizando a classe minoritária lá.

#### Principais Diferenças ####
**Estratégia de Geração:** O SMOTE gera o mesmo número de instâncias sintéticas para todas as instâncias minoritárias, enquanto o ADASYN ajusta o número de instâncias sintéticas com base no nível de dificuldade de cada instância.
**Adequação:** O SMOTE funciona bem em cenários com desequilíbrio moderado de classes, enquanto o ADASYN é mais eficaz em conjuntos de dados altamente desequilibrados e com fronteiras de decisão complexas.
Conteúdo do Repositório
main.py: Script em Python que demonstra o uso do SMOTE e do ADASYN em um conjunto de dados sintético.
README.md (este arquivo): Visão geral do projeto, métodos e resultados.
requirements.txt: Pacotes Python necessários para executar o código.

#### Resultados ####
Testamos quatro algoritmos de classificação (Árvore de Decisão, Floresta Aleatória, Regressão Logística e SVC) nos conjuntos de dados balanceados criados com o SMOTE e o ADASYN. Aqui estão algumas métricas de desempenho para o modelo de Árvore de Decisão como exemplo:

**Modelo de RandomForest com SMOTE**

Precisão: 0.95

Recall: 0.95

F1-score: 0.95

**Modelo de RandomForest com ADASYN**

Precisão: 0.88

Recall: 0.88

F1-score: 0.88

Métricas semelhantes foram calculadas para os outros três modelos de classificação.

**Conclusão**
Este projeto demonstra o uso do SMOTE e do ADASYN para lidar com o desequilíbrio de classes no aprendizado de máquina. A escolha entre esses métodos depende das características do conjunto de dados e da complexidade do problema de classificação. Experimentação e avaliação são essenciais para determinar qual método funciona melhor para seu cenário específico. No Cenário apresentado, o SMOTE saiu melhor que o ADASYN. Porém, futuramente veremos outros cenários em que ADASYN saia melhor.


