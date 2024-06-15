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
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


# Laço infinito para o menu
while True:

    deposito = -1
    opcao = input(menu)

    match opcao:
        
        # Caso opção Despositar escolhida
        case 'd':
            while deposito <= 0:
                deposito += float(input('Informe o valor a ser depositado. /n =>'))

                # Laço para verificar se o valor informado é positivo
                if deposito > 0:
                    saldo += deposito
                else:
                    print(f'''
                            #### O valor R$ {deposito} não é um valor válido para deposito! #### 
                                     --- Por favor informar um valor valido. ---

                          ''')


        # Caso opção Sacar escolhida
        case 's':
            pass
        
        # Caso opção Extrato escolhida
        case 'e':
            pass

        # Caso opção Sair escolhida
        case 'q':
            break # Encerra o loop