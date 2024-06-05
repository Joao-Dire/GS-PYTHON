import os

def limpa_tela():
    os.system('cls')  # limpa a tela para mostrar o resultado

def main_content():
    print('ʙᴇᴍ ᴠɪɴᴅᴏ ᴀᴏ ᴏᴄᴇᴀɴʜᴇʟᴘ')
    print('(1) Denunciar')
    print('(2) Doar para ONGS')
    print('(3) Lista de animais em extinção')
    escolha = int(input('Escolha uma opção\n'))
    while escolha < 1 or escolha > 3:
        print('ʙᴇᴍ ᴠɪɴᴅᴏ ᴀᴏ ᴏᴄᴇᴀɴʜᴇʟᴘ')
        print('(1) Denunciar')
        print('(2) Doar para ONGS')
        print('(3) Lista de animais em extinção')       
        escolha = int(input('opção inválida! Escolha novamente\n'))
    return escolha

def denuncia():

    print('O que gostaria de denunciar?')
    print('(1) Maltratos a animais (pesca ilegal, trafico de animais, etc.')
    print('(2) Poluição de rios, oceanos ou/e praias')
    print('(3) Animal em situação vulnerável (Resgate)')
    escolha = int(input('Escolha uma opção\n'))
    while escolha < 1 or escolha > 3:
        escolha = int(input('opção inválida! Escolha novamente\n'))
    if escolha == 1 or escolha == 2 or escolha == 3:
        caso_denuncia = input('Por favor, descreva o que você viu\n')
        local_denucia = input('Ok! Agora me diga o local em que ocorreu\n')
        data_denuncia = input('Qual foi a data do ocorrido?\n')
        confirmacao = int(input(f'Ok, antes de enviar confirme as informações.\nCaso: {caso_denuncia}\nLocal: {local_denucia}\nData: {data_denuncia}\n(1) Confirmar\n(2) Cancelar\n'))
        while confirmacao == 2:
            caso_denuncia = input('Por favor, descreva o que você viu\n')
            local_denucia = input('Ok! Agora me diga o local em que ocorreu\n')
            data_denuncia = input('Qual foi a data do ocorrido?\n')
            confirmacao = int(input(f'Ok, antes de enviar confirme as informações.\nCaso: {caso_denuncia}\nLocal: {local_denucia}\nData: {data_denuncia}\n 1 - confirmar\n2 - Cancelar\n'))
        print('Obrigado! Sua atitude salva vidas!')

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
        print(f'Confirme os dados\nNúmero do cartão: {num_cartao}\nData de validade: {dat_validade}\nCVV: {cvv}')
    
    print("Doação realizada com sucesso!")


if __name__ == '__main__':
    escolha = main_content()
    if escolha == 1:
        limpa_tela()
        denuncia()
    elif escolha == 2:
        limpa_tela()
        doacao()
    elif escolha == 3:
        print('Função de lista de animais em extinção ainda não implementada.')
