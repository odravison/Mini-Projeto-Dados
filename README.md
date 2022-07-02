# Mini-Projeto-Dados
Mini-projeto de dados para conclusão de aula de introdução a programação
# Jogo de Apostas
Objetivo do Jogo: Acumular dinheiro a partir de apostas bem-sucedidas
Regras: 
- O jogador tem, inicialmente, 30 moedas para apostar.
- Serão usados dois dados, cada um com faces numeradas de 1 a 6.
- A cada rodada, o jogador deverá escolher um tipo de aposta (segundo tabela a seguir) e o computador será responsável por lançar os dados e obter resultados aleatoriamente
- Na Aposta em Número, o jogador escolhe um número entre 2 e 12, e será premiado caso acerte a soma dos resultados dos dados sorteados, independentemente da combinação (Ex: se o número apostado for 5, o jogador pode ganhar com 1 e 4 ou com 2 e 3).
- Na Aposta em Tipo de Números, o jogador aposta se os números sorteados nos dados serão pares ou ímpares, e só será premiado caso acerte o resultado nos dois dados.
- Na Aposta em Tipo de Resultado, o jogador aposta se a soma dos resultados dos dados sorteados será par ou ímpar e será premiado caso acerte.
- Caso a aposta do jogador coincida com o resultado sorteado nos dados, ele receberá a quantidade de moedas equivalente ao prêmio. Caso contrário, ele perderá todas as moedas que tenha apostado na rodada.
- O jogo acaba após 7 rodadas, ou antes, caso o jogador fique sem moedas suficientes para apostar, ou caso ele decida abandonar o jogo.
- Ao fim do jogo, deverão ser exibidos o nome do jogador, a quantidade de rodadas vencidas e seu saldo de moedas.
# Aspectos avaliados no código: 
uso de recursos (laços de repetição, estruturas de decisão, funções, bibliotecas, listas, etc) da linguagem de forma apropriada; comentários no código; qualidade do código (uso de variáveis em vez de números mágicos, repetição desnecessária de instruções, reuso de código, etc); jogabilidade da interface; lógica da aplicação
# Pseudo-Codigo
- Receber nome do jogador
- Oferecer 30 moedas para apostar
- Escolher o tipo de aposta
- Verificar se jogador apostou o valor mínimo
- verificar se jogador escolheu números aceitos 
- verificar o valor dos dados 
- verificar regra para ganhar 
- verificar se ganhou
- se ganhar, receber prêmio
- se perder, perder moedas apostadas
- se perder todas moedas, desistir ou passar 7 rodadas, acabar jogo
- exibir nome do jogador, quantidade de rodadas vencidas e saldo de moedas.
