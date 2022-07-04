import random 

jogador = input('Seja bem vindo ao jogo, por favor digite seu Nome: \n'); #Nome do usuario
resposta_jogador = None;
numeroApostado = None;
moedas = 30;
valorApostado = 0;
TotalDeMoedas = 0;
lista_aposta = ['par' , 'impar', 'numero', 'resultado']; #Lista do tipo de aposta
tipo_da_aposta = None;
dado1 = 0;
dado2 = 0;
soma_dos_dados = 0;

def jogarDados():
    valor1 = random.randint(1,6);
    valor2 = random.randint(1,6);
    return valor1 , valor2
   
while True:
    print("Escolha qual tipo de aposta: " + str(lista_aposta));
    resposta_jogador = input();

    if resposta_jogador == 'par':
        print("Você escolheu o tipo de aposta números pares \n");

        print('Escolha algum valor par de 2 a 12 : ');
        numeroApostado = int(input());

        print("O valor minimo da aposta é de 3 moedas \n");
        print("Quantas moedas você que apostar: \n ")
        valorApostado = int(input());

        print("Jogando os dados...");
        dado1, dado2 = jogarDados();
        print("Resultado = " + str(dado1 + dado2));

        if numeroApostado != jogarDados:
            print("Você perdeu! \n");
            TotalDeMoedas = int(moedas) - int(valorApostado);
            print("Seu Saldo é de: " + str(TotalDeMoedas) + " moedas");
        else:
            print("Parabéns! Você ganhou"); 
            TotalDeMoedas = int(moedas) + int(valorApostado);
            print("Seu Saldo é de: " + str(TotalDeMoedas) + " moedas"); 

    elif resposta_jogador == 'impar':
        print("Você escolheu o tipo de aposta números impares ");

        print('Escolha algum valor impar de 3 a 11 : ')
        numeroApostado = int(input());

        print("O valor minimo da aposta é de 3 moedas \n");
        print("Quantas moedas você que apostar: \n ")
        valorApostado = int(input());

        print("Jogando os dados...");
        dado1, dado2 = jogarDados();
        print(str(dado1 + dado2));

        if numeroApostado != jogarDados:
            print("Você perdeu! \n");
            TotalDeMoedas = int(moedas) - int(valorApostado);
            print("Seu Saldo é de: " + str(TotalDeMoedas) + " moedas");
        else:
            print("Parabéns! Você ganhou"); 
            TotalDeMoedas = int(moedas) + int(valorApostado);
            print("Seu Saldo é de: " + str(TotalDeMoedas) + " moedas"); 
 

    elif resposta_jogador == 'numero':
        print("Você escolheu o tipo de aposta números numero ");
        print("Você escolheu o tipo de aposta números pares \n");

        print('Escolha algum valor par de 2 a 12 : ');
        numeroApostado = int(input());

        print("O valor minimo da aposta é de 3 moedas \n");
        print("Quantas moedas você que apostar: \n ")
        valorApostado = int(input());

        print("Jogando os dados...");
        dado1, dado2 = jogarDados();
        print("Resultado = " + str(dado1 + dado2));

        if numeroApostado != jogarDados:
            print("Você perdeu! \n");
            TotalDeMoedas = int(moedas) - int(valorApostado);
            print("Seu Saldo é de: " + str(TotalDeMoedas) + " moedas");
        else:
            print("Parabéns! Você ganhou"); 
            TotalDeMoedas = int(moedas) + int(valorApostado);
            print("Seu Saldo é de: " + str(TotalDeMoedas) + " moedas"); 

    elif resposta_jogador == 'resultado':
        print("Você escolheu o tipo de aposta de acerta o resultado dos dados ");

    else:
        print("Você escolheu alternativa errada")
    
