import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_content():
    escolha = 0  
    while escolha != 4:  
        print('ʙᴇᴍ ᴠɪɴᴅᴏ ᴀᴏ ᴏᴄᴇᴀɴʜᴇʟᴘ')
        print('(1) Denunciar')
        print('(2) Doar para ONGs')
        print('(3) Lista de animais em extinção')
        print('(4) Sair')
        escolha = int(input('Escolha uma opção\n'))
        
        while escolha < 1 or escolha > 4:
            print('ʙᴇᴍ ᴠɪɴᴅᴏ ᴀᴏ ᴏᴄᴇᴀɴʜᴇʟᴘ')
            print('(1) Denunciar')
            print('(2) Doar para ONGs')
            print('(3) Lista de animais em extinção')        
            escolha = int(input('Opção inválida! Escolha novamente\n'))

        if escolha == 1:
            limpa_tela()
            denuncia()
        elif escolha == 2:
            limpa_tela()
            doacao()
        elif escolha == 3:
            limpa_tela()
            lista_animais()

def denuncia():
    print('O que gostaria de denunciar?')
    print('(1) Maltratos a animais (pesca ilegal, tráfico de animais, etc.')
    print('(2) Poluição de rios, oceanos ou/e praias')
    print('(3) Animal em situação vulnerável (Resgate)')
    print('(4) Voltar')
    escolha = int(input('Escolha uma opção\n'))
    
    while escolha < 1 or escolha > 4:
        escolha = int(input('Opção inválida! Escolha novamente\n'))

    if escolha == 1 or escolha == 2 or escolha == 3:
        caso_denuncia = input('Por favor, descreva o que você viu\n')
        local_denuncia = input('Ok! Agora me diga o local em que ocorreu\n')
        data_denuncia = input('Qual foi a data do ocorrido?\n')
        confirmacao = int(input(f'Ok, antes de enviar confirme as informações.\nCaso: {caso_denuncia}\nLocal: {local_denuncia}\nData: {data_denuncia}\n(1) Confirmar\n(2) Cancelar\n'))
        
        while confirmacao == 2:
            caso_denuncia = input('Por favor, descreva o que você viu\n')
            local_denuncia = input('Ok! Agora me diga o local em que ocorreu\n')
            data_denuncia = input('Qual foi a data do ocorrido?\n')
            confirmacao = int(input(f'Ok, antes de enviar confirme as informações.\nCaso: {caso_denuncia}\nLocal: {local_denuncia}\nData: {data_denuncia}\n 1 - confirmar\n2 - Cancelar\n'))
        
        print('Obrigado! Sua atitude salva vidas!')

    elif escolha == 4:
        limpa_tela()
        return

def doacao():
    print('Obrigado por ajudar!')
    valor = float(input('Qual seria o valor?\nR$'))

    while valor < 0:
        valor = float(input('Valor incorreto! Insira um novo valor\nR$'))
    
    metodo_pagamento = int(input('Qual seria o método de pagamento?\n(1) Cartão Débito\n(2) Pix\n'))

    if metodo_pagamento == 1:
        metodo_pagamento_str = 'Cartão de Débito'
    elif metodo_pagamento == 2:
        metodo_pagamento_str = 'Pix'
    else:
        print("Método de pagamento inválido!")
        return

    limpa_tela()
    confirmacao = int(input(f'Confirme os dados: R${valor}\nMétodo de pagamento: {metodo_pagamento_str}\n(1) Confirmar\n(2) Cancelar\n'))
    
    while confirmacao == 2:
        valor = float(input('Qual seria o valor?\nR$'))
        while valor < 0:
            valor = float(input('Valor incorreto! Insira um novo valor\nR$'))      
        metodo_pagamento = int(input('Qual seria o método de pagamento?\n(1) Cartão Débito\n(2) Pix\n'))
        if metodo_pagamento == 1:
            metodo_pagamento_str = 'Cartão de Débito'
        elif metodo_pagamento == 2:
            metodo_pagamento_str = 'Pix'
        else:
            print("Método de pagamento inválido!")
            return
        limpa_tela()
        confirmacao = int(input(f'Confirme os dados: R${valor}\nMétodo de pagamento: {metodo_pagamento_str}\n(1) Confirmar\n(2) Cancelar\n'))
           
    if metodo_pagamento == 1:
        num_cartao = input("Número impresso no cartão:")
        dat_validade = input('Data de vencimento:')
        cvv = input('CVV do cartão:')
        confirmacao = int(input(f'Confirme os dados\nNúmero do cartão: {num_cartao}\nData de validade: {dat_validade}\nCVV: {cvv}\n(1) Confirmar\n(2) Cancelar\n'))
        if confirmacao == 1:
            print("Doação realizada com sucesso!")
        else:
            print("Doação cancelada")
            return
    elif metodo_pagamento == 2:
        print('Sua chave pix:\n00020101021226880014BR.GOV.BCB.PIX0136com.ong.oceanhelp0137Brasil OceanHelp52040000530398654041.005802BR5923OceanHelp LTDA6009SAO PAULO62190528AD3\nObrigado por colaborar!')
    

def adicionar_animais(lista):
    raca = input('Digite a raça do animal:\n')
    especie = input('Digite a espécie:\n')
    nome = input('Digite o nome científico do animal:\n')
    lista.append(raca)
    lista.append(especie)
    lista.append(nome)

def lista_animais():
    escolha = 0  
    while escolha != 3:  
        print('(1) Adicionar animais em extinção')
        print('(2) Listar animais em extinção')
        print('(3) Voltar')
        escolha = int(input('Escolha uma opção\n'))
        
        while escolha < 1 or escolha > 3:
            escolha = int(input('Opção inválida! Escolha novamente\n'))

        if escolha == 1:
            adicionar_animais(animais)
        elif escolha == 2:
            print(f'Animais em extinção: {animais}')

animais = []

main_content()
