# IA Previsão Salário — Apresentação do Projeto

## O que é

Um sistema de previsão de salário para profissionais de TI, construído do zero: desde a coleta de dados reais até uma API funcional, testada e containerizada. O objetivo não foi só treinar um modelo — foi construir algo que se parecesse com um produto de verdade, aplicando práticas reais de engenharia de dados e desenvolvimento de software.

**Repositório completo:** [github.com/fabriciotonetta/ia-previsao-salario](https://github.com/fabriciotonetta/ia-previsao-salario)

---

## O problema que resolvi

Profissionais de TI frequentemente não têm um parâmetro claro de quanto deveriam ganhar, dado seu perfil (país, experiência, cargo, formação, modelo de trabalho). Usei dados reais de mais de 65 mil desenvolvedores (Stack Overflow Developer Survey 2024) para construir um modelo que estima essa faixa salarial.

---

## Como abordei o projeto

1. **Coleta e limpeza de dados** — filtrei o dataset para respondentes CLT full-time, tratei valores textuais inconsistentes (como "Less than 1 year" na coluna de experiência), e removi outliers usando corte por percentil, documentando cada decisão.

2. **Comparação de modelos, não só treino** — treinei três modelos diferentes (Regressão Linear, Random Forest, Gradient Boosting) e comparei com métricas MAE e RMSE, escolhendo o Gradient Boosting por apresentar o menor erro. Importante: quando o Random Forest teve desempenho pior que a Regressão Linear, documentei isso honestamente, em vez de esconder — é um resultado real e explicável.

3. **Análise crítica do próprio modelo** — identifiquei que a variável de país (especificamente, ser dos EUA) domina a previsão, respondendo por 58% da importância total. Validei essa observação com um experimento controlado (removendo a variável e medindo o impacto no erro: piora de 41,44%), em vez de apenas aceitar o resultado da importância de variáveis sem verificação.

4. **Transformação em produto** — encapsulei o modelo numa API REST com FastAPI, com validação de dados de entrada, documentação automática (Swagger), testes automatizados cobrindo casos de sucesso, erro e borda, e um pipeline de integração contínua (GitHub Actions) rodando os testes a cada alteração de código.

5. **Containerização** — criei um Dockerfile validado localmente, garantindo que a aplicação roda de forma idêntica em qualquer ambiente compatível com Docker.

---

## Resultado técnico

| Modelo | MAE (USD) | RMSE (USD) |
|---|---|---|
| Regressão Linear | 28.981,59 | 42.549,79 |
| Random Forest | 30.125,79 | 45.031,14 |
| **Gradient Boosting** | **28.544,25** | **42.322,54** |

O modelo final erra, em média, cerca de USD 28.500 na previsão de salário anual — um resultado esperado dado o alto grau de variação salarial global no setor de TI, mas consistente o suficiente para demonstrar viabilidade técnica.

---

## Uma decisão que quero destacar

Durante o projeto, planejei publicar a API com um link público de deploy. Ao tentar, descobri que as principais plataformas gratuitas (Render, Hugging Face Spaces, Koyeb) mudaram recentemente suas políticas, passando a exigir cartão de crédito mesmo em planos gratuitos. Decidi não prosseguir com o deploy público para não depender de meio de pagamento pessoal — a aplicação está validada e pronta via Docker, testável localmente por qualquer pessoa que clonar o repositório, com instruções completas no README.

Considero essa uma decisão de engenharia, não uma limitação do projeto: identifiquei uma restrição externa, avaliei alternativas, e documentei a decisão de forma transparente — em vez de forçar uma solução frágil só para "ter um link".

---

## Tecnologias utilizadas

Python · Pandas · Scikit-learn · FastAPI · Pydantic · Docker · Pytest · GitHub Actions · Git

---

## Sobre mim

Estou construindo minha entrada na área de dados e IA através de projetos como este: montados do zero, errando e corrigindo no processo, e documentando cada decisão no caminho. Não cheguei aqui sabendo tudo — cheguei aprendendo enquanto construía, o que inclusive me obrigou a entender de verdade cada etapa (por que um modelo teve desempenho pior que outro, por que uma variável domina uma previsão, como diagnosticar um erro silencioso de configuração) em vez de só seguir um tutorial. É esse processo que quero continuar tendo a chance de fazer, agora dentro de uma equipe.