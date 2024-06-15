menu = """

########## Menu do Sistema Bancário ##########

           --- Escolha uma opção ---

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


# Variáveis
saldo = 0
LIMITE = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
depositos = []
saques = []


# Laço infinito para o menu
while True:

    deposito = -1
    opcao = input(menu)

    match opcao:
        
        # Caso opção Despositar escolhida
        case 'd':
            while deposito <= 0:
                deposito = float(input('\nInforme o valor a ser depositado. \n=> '))

                # Laço para verificar se o valor informado é positivo
                if deposito > 0:
                    saldo += deposito
                    depositos.append(deposito)
                else:
                    print(f'''
                            #### O valor R$ {deposito} não é um valor válido para deposito! #### 
                                     --- Por favor informar um valor valido. ---

                          ''')


        # Caso opção Sacar escolhida
        case 's':
            # Verifica se não exedeu o limite de saques diários
            if numero_saques == 3:
                print('O limite diário de saques é de no máximo 3!')

            else:
                status_saque = 1

                while status_saque != 0:
                    saque = float(input('\nInforme o valor a ser sacado. \n => '))

                    # Verifica se não exedeu o valor limite do saques
                    if saque > LIMITE:
                        print(f'''   
                        $$$ Valores para saque: $$$
                    
                    Mínimo - R$ 1.00
                    Máximo - R$ {str(LIMITE)}
                    ''')

                    else:
                        # Verifica se o cliente possui salddo suficiente
                        if (saldo - saque) <= 0:
                            print(f'''
                                    Você não possui saldo suficiente para realizar esse saque!
                                    Saldo: R$ {str(saldo)}
                                ''')                        
                        else:
                            saldo -= saque
                            saques.append(saque)
                            numero_saques += 1 
                            status_saque = 0                                          
               
        
        # Caso opção Extrato escolhida
        case 'e':
            pass

        # Caso opção Sair escolhida
        case 'q':
            break # Encerra o loop