from time import sleep
print('\033[1;34;40mPROGRAMA DOAÇÃO DE SANGUE\033[m')
nome = str(input('Digite seu nome para iniciarmos: ')).strip().upper()
print(f'Olá {nome}, seja bem vindo(a) ao programa Doação de Sangue. Aqui você poderá verificar a compatibilidade \ndos tipos de sangue.')
sleep(5)
tipo_sanguineo = str(input('Você sabe seu tipo sanguíneo? S/N: ')).strip().upper()[0]
while tipo_sanguineo not in 'SN':
    tipo_sanguineo = str(input('Respota inválida. Digite S para \033[1;32mSim\033[m e N para \033[1;31mNão\033[m: ')).strip().upper()[0]
if tipo_sanguineo == 'S':
    print('Vamos começar.')
    while True:
        print("""Escolha um número das opções abaixo de acordo com seu tipo sanguíneo:
        
        \033[1;33m[1] A positivo  A+  [3] B positivo  B+  [5] AB positivo  AB+  [7] O positivo  O+\033[m
        \033[1;33m[2] A negativo  A-  [4] B Negativo  B-  [6] AB negativo  AB-  [8] O negativo  O-\033[m
         """)
        opcao_tipo_sanguineo = str(input('Qual é a opção escolhida? ')).strip().upper()[0]
        while opcao_tipo_sanguineo not in '12345678':
            opcao_tipo_sanguineo = str(input('Opção não listada. Escolha o tipo utilizando números entre 1 e 8: ')).strip().upper()[0]
        print('Deixa eu verificar...')
        sleep(2)
        if opcao_tipo_sanguineo == '1':
            print('Você pode doar para A+ e AB+ e receber de A+, A-, O+ e O-.')
        elif opcao_tipo_sanguineo == '2':
            print('Você pode doar para A+, A-, AB+ e AB- e receber de A- e O-.')
        elif opcao_tipo_sanguineo == '3':
            print('Você pode doar para B+ e AB+ e receber de B+, B-, O+ e O-.')
        elif opcao_tipo_sanguineo == '4':
            print('Você pode doar para B+, B-, AB+ e AB- e receber de B- e O-.')
        elif opcao_tipo_sanguineo == '5':
            print('Seu sangue é o receptor universal, você pode receber de A+, A-, B+, B-, AB+, AB- O+ e O- e doar \nsomente para AB+.')
        elif opcao_tipo_sanguineo == '6':
            print('Você pode doar para AB+ e AB- e receber de A-, B-, AB- e O-.')
        elif opcao_tipo_sanguineo == '7':
            print('Você pode doar para A+, B+, AB+ e O+ e receber de O+ e O-.')
        else:
            print('Seu tipo sanguíneo é o doador universal. Você pode doar para A+, A-, B+, B-, AB+, AB- e O+ e receber \nsomente de outro O-.')
        nova_consulta = str(input('Deseja realizar uma nova consulta? S/N ')).strip().upper()[0]
        while nova_consulta not in 'SN':
            nova_consulta = str(input('Para realizar uma nova consulta responda S para \033[1;32mSim\033[m e N para \033[1;31mNão\033[m: ')).strip().upper()[0]
        if nova_consulta == 'N':
            print('Obrigado por utilizar o programa.')
            break
else:
    print('Não poderemos continuar com o programa. Você pode descobrir seu tipo sanguíneo realizando um exame \nlaboratorial de sangue ou fazendo cadastro em centros de doação.')
print('-'*30)
print('Referências bibliográficas do sistema ABO: https://www.mdsaude.com/hematologia/tipos-sanguineos-sistema-abo/ ')
