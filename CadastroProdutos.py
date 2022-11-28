import mysql.connector
import PySimpleGUI as sg

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='daniel12345678910',
    database='cadastro_produtos'
)

cursor = conexao.cursor()

layout = [
    [sg.Text('Cadastrar um produto:')],
    [sg.Text('Código:')],
    [sg.InputText(key='nome_codigo')],
    [sg.Text('Descrição:')],
    [sg.InputText(key='nome_descricao')],
    [sg.Text('Preço:')],
    [sg.InputText(key='preco_produto')],
    [sg.Button('Cadastrar'), sg.Button('Cancelar')],
    [sg.Text('', key='msg')]
]

janela = sg.Window('Cadastro de Produtos', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    nome_codigo = valores['nome_codigo']
    nome_descricao = valores['nome_descricao']
    preco_produto = valores['preco_produto']
    if evento == 'Cadastrar':
        if nome_codigo != '' and nome_descricao != '' and preco_produto != '':
            comando = f'INSERT INTO produtos (Código, Descrição, Preço) VALUES ("{nome_codigo}", ' \
                      f'"{nome_descricao}", {preco_produto})'
            cursor.execute(comando)
            conexao.commit()
            janela['msg'].update('Cadastro Concluído!')
            janela['nome_codigo'].update('')
            janela['nome_descricao'].update('')
            janela['preco_produto'].update('')
        else:
            janela['msg'].update('Preencha todos os campos!')
    if evento == 'Cancelar':
        janela['nome_codigo'].update('')
        janela['nome_descricao'].update('')
        janela['preco_produto'].update('')

cursor.close()
conexao.close()
janela.close()
