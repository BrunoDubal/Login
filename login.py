import random
import smtplib
from email.message import EmailMessage
import mysql.connector

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='login'
)
cursor = banco.cursor()


#Seleciona login ou cadastro
def opcao():
    while True:
        opc = int(input('''Selecione uma opção:
        [1] Login
        [2] Cadastro de novo usuário
        [3] Parar execução
        '''))
        if opc == 1 or opc == 2 or opc == 3:
            return opc
        else:
            print('Opção invalida.')

def logout():
    while True:
        opc2 = int(input('''Selecione uma opção:
        [1] Logout
        [2] Finalizar
        '''))
        if opc2 == 1 or opc2 == 2:
            return opc2
        else:
            print('Opção invalida.')


def cod():
    codi = random.randint(10000, 99999)
    return codi


#Tela login
while True:
    opc = opcao()
    if opc == 1:
        name = str(input('ID: '))
        password = str(input('Password: '))
        comando_sql = f'select nome, senha from pessoas where nome = "{name}" and senha = "{password}";'
        cursor.execute(comando_sql)
        valores = cursor.fetchall()
        if valores[0][0] == name and valores[0][1] == password:
            print('Login realizado com sucesso!\n\n')
            opc2 = logout()
            if opc2 == 2:
                break
            else:
                print('Logout realizado.\n\n')
        else:
            print('Credenciais invalidas. Tente novamente.')

#Tela cadastro
    elif opc == 2:
        while True:
            name = str(input('ID: '))
            tel = str(input('Telefone: '))
            mail = str(input('Email: '))
            password = str(input('Password: '))
            conf_password = str(input('Confirm password: '))
            if password == conf_password:
                comando_sql = f'select nome, fone, mail from pessoas where nome = "{name}" or mail = "{mail}" or fone = "{tel}";'
                cursor.execute(comando_sql)
                valores = cursor.fetchall()
                try:
                    if valores[0][1] == tel:
                        print('Telefone ja cadastrado. Tente outro telefone.')
                    elif valores[0][2] == mail:
                        print('Email ja cadastrado. Tente outro email.')

                except:
                    codigo = cod()
                    EMAIL_ADDRESS = 'seu email'
                    EMAIL_PASSWORD = 'senha do seu email'

                    msg = EmailMessage()
                    msg['Subject'] = 'Verificação de email'
                    msg['From'] = 'LoginPyTeste@gmail.com'
                    msg['To'] = f'{mail}'
                    msg.set_content(f'Codigo de verificação {codigo}.')

                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                        smtp.send_message(msg)

                    while True:
                        cod_vf = int(input('''\n\nDigite que o codigo enviado para seu email: '''))

                        if cod_vf == codigo:
                            comando_sql = f'insert into pessoas(nome, senha, mail, fone) values ("{name}", "{password}", "{mail}", "{tel}");'
                            cursor.execute(comando_sql)
                            print('Usuário cadastrado com sucesso!\n\n')
                            break
                        else:
                            print('Codigo incorreto. Tente novamente: ')
            else:
                print('As senhas nao coincidem. Tente novamente.')
            break
    else:
        break