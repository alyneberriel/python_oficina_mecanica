def Nota_Fiscal():
    formata('NOTA FISCAL ELETRÔNICA')
    for c in range(0, len(nota_fiscal)):

        for d in range(0, len(nota_fiscal[c])):
            print(f'{nota_fiscal[c][d]:<18}', end='')
        print()
    print(f'Valor total:', f'R${totalnota:<18}')
    print('==' * 20)

def formata(f):
    print('\033[34m==\033[m' * 20)
    print(f'\033[34m{f:^40}\033[m')
    print('\033[34m==\033[m' * 20)

def escolha(*esc):
    texto = formata('Escolha uma opção para iniciar')
    for c, v in enumerate(esc):
        print(f'{v}', )

def escolha2(*esc):
    texto = formata('Escolha uma opção para continuar')
    for c, v in enumerate(esc):
        print(f'{v}', )

def troco(t):
    total = t
    ced = 50
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            print(f'total de {totced} de R$ {ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            elif ced == 5:
                ced = 2
            elif ced == 2:
                ced = 1
            totced = 0
            if total == 0:
                break


def Adicionar_Produtos():
    formata("PRODUTOS")

    total_produto = 0

    def Escolha_Produto():
        print("\n")
        escolha_produto = str(input(f'Produtos disponíveis:\n'
                                    '\033[33m[1]\033[m' f' Pneu:\t\t\t R${produtos_valor[0]}\n'
                                    '\033[33m[2]\033[m' f' Vela:\t\t\t R${produtos_valor[1]}\n'
                                    '\033[33m[3]\033[m' f' Disco de Freio:\t\t R${produtos_valor[2]}\n'
                                    '\033[33m[4]\033[m' f' Tambor de Freio:\t\t R${produtos_valor[3]}\n'
                                    '\033[33m[5]\033[m' f' Lonas:\t\t\t R${produtos_valor[4]}\n'
                                    '\033[33m[6]\033[m' f' Fluido de Freio:\t\t R${produtos_valor[5]}\n'
                                    '\033[33m[7]\033[m' f' Óleo de Motor:\t\t R${produtos_valor[6]}\n'
                                    '\033[33m[8]\033[m' f' Baterias:\t\t\t R${produtos_valor[7]}\n'
                                    f'Digite o número de um produto ou digite ''\033[33m[9]\033[m'' para voltar:').strip())
        return escolha_produto

    while True:
        produto_opcao = ['Pneu',
                         'Vela',
                         'Disco de Freio',
                         'Tambor de Freio',
                         'Lonas',
                         'Fluido de Freio',
                         'Óleo de Motor',
                         'Baterias']
        produtos_valor = [280, 95, 130, 83, 95, 36, 25, 499]

        z = Escolha_Produto()

        if z == "9":
            return total_produto

        lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while z not in lista:
            print("Por favor, digite apenas um número inteiro na lista: ")
            z = Escolha_Produto()
            if z == "9":
                return total_produto
        z = int(z)
        print('\n')
        escolha_quantidade_produto = str(input(f"Escolha quantidade de {produto_opcao[int(z) - 1]}: ").strip())

        while True:
            if escolha_quantidade_produto.isnumeric() == False or int(escolha_quantidade_produto) <= 0:
                escolha_quantidade_produto = str(input(f"Escolha quantidade de {produto_opcao[int(z) - 1]}: ").strip())
            else:
                escolha_quantidade_produto = int(escolha_quantidade_produto)
                break

        cont = 0
        tot = 0
        for c in range(0, escolha_quantidade_produto):
            tot += produtos_valor[int(z) - 1]
            cont += 1
            total_produto += produtos_valor[int(z) - 1]
        pre_nota.append(produto_opcao[int(z) - 1])
        pre_nota.append(f'x{cont}')
        pre_nota.append(f'R${tot}')
        nota_fiscal.append(pre_nota[:])
        pre_nota.clear()

        print("\n")
        verificar = str(input("Deseja continuar adicionando produtos? \033[33m[S/N]\033[m: ").upper().strip())
        while verificar != "S" and verificar != "N":
            verificar = str(input("Deseja continuar adicionando produtos? \033[33m[S/N]\033[m: ").upper().strip())

        if verificar == "N":
            return total_produto

def Adicionar_Servicos():
    formata("SERVIÇOS")

    def Escolha_Servico():
        print("\n")
        escolha_servico = (input(f'Serviços disnponíveis:\n'
                                 '\033[33m[1]\033[m' f' Troca de pastilha de freio:\t\t R${servico_valor[0]}\n'
                                 '\033[33m[2]\033[m' f' Troca de óleo e filtro de óleo:\t R${servico_valor[1]}\n'
                                 '\033[33m[3]\033[m' f' Troca de Amortecedor:\t\t R${servico_valor[2]}\n'
                                 '\033[33m[4]\033[m' f' Limpeza do TBI:\t\t\t R${servico_valor[3]}\n'
                                 '\033[33m[5]\033[m' f' Troca de vela e ignição:\t\t R${servico_valor[4]}\n'
                                 '\033[33m[6]\033[m' f' Troca de embreagem:\t\t\t R${servico_valor[5]}\n'
                                 '\033[33m[7]\033[m' f' Sangria do óleo de freio:\t\t R${servico_valor[6]}\n'
                                 '\033[33m[8]\033[m' f' Troca do disco de freio:\t\t R${servico_valor[7]}\n\n'
                                 f'Digite o número de um serviço ou digite ''\033[33m[9]\033[m'' para voltar: ').strip())
        return escolha_servico

    valor_total = 0
    while True:
        servico_opcao = ['Troca de pneu',
                         'SUB past de freio',
                         'SUB Amortecedor',
                         'Limpeza do TBI',
                         'Troca de vela',
                         'Troca de embreagem',
                         'SUB óleo de freio',
                         'SUB disco de freio']
        servico_valor = [40, 30, 130, 70, 75, 200, 80, 65]

        z = Escolha_Servico()

        if z == "9":
            return valor_total

        lista = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        while z not in lista:
            print("Por favor, digite apenas um número inteiro: ")
            z = Escolha_Servico()
            if z == "9":
                return valor_total
        z = int(z)

        pre_nota.append(servico_opcao[int(z) - 1])
        pre_nota.append(' ')
        pre_nota.append(f'R${servico_valor[int(z) - 1]}')
        valor_total += servico_valor[int(z) - 1]
        nota_fiscal.append(pre_nota[:])
        pre_nota.clear()

        print("\n")
        verificar = input("Deseja continuar adicionando serviços? \033[33m[S/N]\033[m: ").upper().strip()
        while verificar != "S" and verificar != "N":
            verificar = input("Deseja continuar adicionando servços? \033[33m[S/N]\033[m: ").upper().strip()

        if verificar == "N":
            return valor_total

def Revisao():
    formata("REVISÃO")
    tipo = input("Escolha para que tipo de veículo deseja uma revisão:\n"
                 "\033[33m[1]\033[m Moto\n"
                 "\033[33m[2]\033[m Carro\n\n")
    while tipo != "1" and tipo != "2":
        tipo = input("Escolha para que tipo de veículo deseja uma revisão:\n"
                     "\033[33m[1]\033[m Moto\n"
                     "\033[33m[2]\033[m Carro\n\n")

    if tipo == "1":
        print("Serviços inclusos na revisão:\n"
              "-Checagem da água\n"
              "-Troca de óleo e filtro de óleo\n"
              "-Pneus\n"
              "-Sistemas de freios\n"
              "-Checagem de luzes\n\n")
        formata("Valor: R$100,00")
        while True:
            verificar = str(input("Você aceita estes serviços por este valor? \033[33m[S/N]\033[m").upper().strip())
            if verificar == "S":
                pre_nota.append('Revisão Carro')
                pre_nota.append(' ')
                pre_nota.append(f'R${100}')
                nota_fiscal.append(pre_nota[:])
                pre_nota.clear()
                return 100
            elif verificar == "N":
                return 0


    elif tipo == "2":
        print("Serviços inclusos na revisão:\n"
              "- Troca de óleo\n"
              "- Filtro de ar do motor\n"
              "- Ar condicionado\n"
              "- Filtro de combustível\n"
              "- Sistema de freios\n")

        formata("Valor: R$500,00")
        while True:
            verificar = str(input("Você aceita estes serviços por este valor? \033[33m[S/N]\033[m").upper().strip())
            if verificar == "S":
                pre_nota.append('Revisão Carro')
                pre_nota.append(f'R${500}')
                nota_fiscal.append(pre_nota[:])
                pre_nota.clear()
                return 500
            elif verificar == "N":
                return 0

def Finalizar_Compra():
    formata(f'Valor total R${totalnota}')
    formata('Forma de pagamento')
    opcoes_pague = ["1","2","3","4","5"]
    escolha_pague = input('\033[33m[1]\033[m' ' Dinheiro\n'
                          '\033[33m[2]\033[m' ' PIX\n'
                          '\033[33m[3]\033[m' ' Cartão de crédito\n'
                          '\033[33m[4]\033[m' ' Cartão de débito\n'
                          '\033[33m[5]\033[m' ' Desistir da compra\n\n'
                          'Escolha opção: ').strip()

    while escolha_pague not in opcoes_pague:
        formata('Forma de pagamento')
        escolha_pague = input('\033[33m[1]\033[ Dinheiro\n'
                              '\033[33m[2]\033[ PIX\n'
                              '\033[33m[3]\033[ Cartão de crédito\n'
                              '\033[33m[4]\033[ Cartão de débito\n'
                              '\033[33m[5]\033[ Desistir da compra\n\n'
                              'Escolha opção: ').strip()

    if escolha_pague == "1":
        dinheiro = 0
        Nota_Fiscal()

        while True:
            dinheiro = input(f'O total da compra foi: {totalnota}, troco para quanto?')
            while True:
                if dinheiro.isnumeric() == False or int(dinheiro) <= 0:
                    dinheiro = str(
                        input(f'O total da compra foi: {totalnota}, troco para quanto?').strip())
                else:
                    dinheiro = int(dinheiro)
                    break

            difCliente = dinheiro - totalnota

            if difCliente < 0:
                print('Valor insuficiente')

            elif difCliente == 0:
                print('PARABENS COMPRA CONCLUIDA')
                return difCliente
            else:
                print('Seu troco: ')
                troco(difCliente)
                break

    elif escolha_pague == "2":
        Nota_Fiscal()
        print('A chave de pagamento é: 999999999, o prazo de validade da chave são de 30 minutos')

    elif escolha_pague == "3":
        Nota_Fiscal()
        print('Pago com cartão de crédito com sucesso!')

    elif escolha_pague == "4":
        Nota_Fiscal()
        print('Pago com cartão de débito com sucesso!')

    elif escolha_pague == "5":
        Nota_Fiscal()
        desistir = input(f'Tem certeza que deseja desistir dos itens \033[33m[S/N]\033[m: ').upper().strip()
        while desistir != "S" and desistir != "N":
            desistir = input(f'Tem certeza que deseja desistir dos itens \033[33m[S/N]\033[m: ').upper().strip()
        if desistir == "S":
            print('Obrigada pela visita')
            desistencia = 1
        else:
            escolha_pague = 0
            Finalizar_Compra()


# Codigo principal
formata('Bem Vindo ao Auto center')
desistencia = 0
totalnota = int(0)

while True:
    escolha('\033[33m[A]\033[m Para acessar o programa', '\033[33m[F]\033[m Para finalizar o programa\n')
    inicio = str(input('Digite sua opção: ')).upper().strip()
    if inicio != "A" and inicio != "F":
        print('\033[31mOpção inválida\033[m')
    elif inicio == 'F':
        if totalnota != 0 and desistencia != 0:
            Nota_Fiscal()
        print('Volte sempre!!, Se precisar é só me procurar')
        break

    elif inicio == "A":
        escolha1 = ['1', '2', '3', '4', '5']

        # variáveis
        nota_fiscal = []
        total_produto = []
        total_compra = []
        pre_nota = []
        totalnota = int(0)
        desistencia = 0

        while True:

            escolha2('\033[33m[1]\033[m Adicionar produto',
                     '\033[33m[2]\033[m Adicionar servico',
                     '\033[33m[3]\033[m Revisão',
                     '\033[33m[4]\033[m Finalizar compra',
                     '\033[33m[5]\033[m Sair\n')
            x = str(input('Digite sua opção: ')).upper().strip()
            if x != '1' and x != '2' and x != '3' and x != '4' and x != "5":
                print('\033[31mOpção inválida, Digite uma opção válida\033[m')
            if x == "1":
                totalnota += Adicionar_Produtos()
            elif x == "2":
                totalnota += Adicionar_Servicos()
            elif x == '3':
                totalnota += Revisao()
            elif x == '4':
                if totalnota == 0:
                    saida = input("Você não efetuou nenhuma compra, você voltará ao início do programa.")
                    break
                Finalizar_Compra()
                break
            elif x == "5":
                desistencia=0
                break
