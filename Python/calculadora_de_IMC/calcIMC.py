import PySimpleGUI as sg

sg.theme('DarkBlue')

def calcularImc():
    peso = float(values['peso'])
    altura = float(values['altura'])
    sexoM = values['masculino']
    sexoF = values['feminino']
    ideal = ''
    situacao = ''
    if altura > 2.5:
        sg.popup('Valor maximo 2.5')
    else:
        IMC = peso / altura ** 2

        if IMC < 18.5:
            situacao = 'Abaixo do peso'
        elif (IMC > 18.5) and (IMC < 24.9):
            situacao = 'Normal'
        elif (IMC > 24.9) and (IMC <= 29.9):
            situacao = 'Sobrepeso'
        elif (IMC > 29.9) and (IMC <= 34.9):
            situacao = 'Obesidade grau 1'
        elif (IMC > 34.9) and (IMC <= 39.9):
            situacao = 'Obesidade grau 2'
        elif IMC > 40:
            situacao = 'Obesidade grau 1'
        janela.Element('imc').Update('{:.3}'.format(IMC))
        janela.Element('situacao').Update(situacao)
    if sexoM is True:
        ideal = ((altura * 100) - 100) * 0.90
        janela.Element('recomendado').Update('{:.3}'.format(ideal))

    else:
        if sexoF is True:
            ideal = ((altura * 100) - 100) * 0.85
            janela.Element('recomendado').Update('{:.3}'.format(ideal))


def verifica():
    peso = values['peso']
    altura = values['altura']
    if (peso is None or peso == '') or (altura is None or altura == ''):
        sg.popup('Todos os campos devem ser preenchidos.')
    else:
        calcularImc()


def calculaPesoIdeal():
    evento, values = janela.read()
    sexoM = values['masculino']
    sexoF = values['feminino']
    altura = float(values['altura'])
    ideal = ''
    if sexoM is True:
        ideal = ((altura * 100) - 100) * 0.90
        janela.Element('recomendado').Update('{:.3}'.format(ideal))

    else:
        if sexoF is True:
            ideal = ((altura * 100) - 100) * 0.85
            janela.Element('recomendado').Update('{:.3}'.format(ideal))


def oImc():
    sg.popup_no_titlebar(""" 
    O Índice de Massa Corporal (IMC) é um parâmetro bastante utilizado para classificar o indivíduo de acordo com seu 
    peso e altura. Seu uso é disseminado principalmente entre profissionais que trabalham com o corpo, como médicos, 
    fisioterapeutas e profissionais de Educação Física. É importante ressaltar que a Organização Mundial da Saúde (OMS) 
    utiliza esse índice como indicador do nível de obesidade nos diferentes países.
    
    Fonte: Brasil escola.
    """)


def oAutor():
    sg.popup_no_titlebar('Projeto desenvolvido por Edson Lucas')


menu_layout = ([['Sobre', ['&O IMC', '&Autor']]])

layout = [
    [sg.MenuBar(menu_layout)],
    [sg.T(size=(8, 0)), sg.T('Calcule seu IMC', font=('Arial', 20, 'bold'))],
    [sg.T()],
    [sg.T('Seu IMC:', font=('Arial', 13)), sg.T(size=(10, 0), key='imc', relief='sunken', text_color='White'), sg.T('Situação:', font=('Arial', 13)), sg.T(size=(15, 0), key='situacao', relief='sunken' , text_color='White', justification='center')],
    [sg.T()],
    [sg.T('Peso recomendado', font=('Arial', 13)), sg.T(size=(10, 0), key='recomendado', relief='sunken', text_color='White')],
    [sg.T()],
    [sg.T('Seu peso', font=('Arial', 13)), sg.T(size=(4, 0)), sg.Input(size=(15, 0), key='peso', tooltip='Ex: 60.0', default_text='50.0')],
    [sg.T()],
    [sg.T('Sua altura ', font=('Arial', 13)), sg.T(size=(3, 0)), sg.Input(tooltip='Ex: 1.50', size=(15, 0), key='altura', default_text='1.50')],
    [sg.T()],
    [sg.T('Seu sexo', font=('Arial', 13), size=(10, 0)), sg.Radio('Masculino', 'RADIO1', key='masculino'), sg.Radio('Feminino', 'RADIO1', default=True, key='feminino')],
    [sg.T()],
    [sg.T(size=(11, 0)), sg.Button('Calcular', size=(10, 0), key='calcular'), sg.Button('Limpar', size=(10, 0), key='limpar')],
    [sg.T()],
    [sg.T('v.1.0', font=('Arial', 7), size=(65,0), justification='right')],
]
janela = sg.Window('Calculadora de IMC', layout, location=(600, 200), border_depth=2)

while True:
    evento, values = janela.read()
    if evento is None:
        break
    if evento == 'calcular':
        verifica()
    if evento == 'limpar':
        janela.Element('imc').Update('')
        janela.Element('situacao').Update('')
        janela.Element('recomendado').Update('')
        janela.Element('peso').Update('60.0')
        janela.Element('altura').Update('1.50')
        janela.Element('feminino').Update(True)

    if evento == 'O IMC':
        oImc()
    if evento == 'Autor':
        oAutor()

