#Seleciona login ou cadastro
from distutils.command.install_scripts import install_scripts


opc = int(input('''Selecione uma opção:
[1] Login
[2] Cadastro de novo usuário
'''))
#Tela login
if opc == 1:
    name = str(input('ID: '))
    password = str(input('Password: '))
#Tela cadastro
else:
    name = str(input('ID: '))
    tel = str(input('Telefone: '))
    mail = str(input('Email: '))
    password = str(input('Password: '))
    conf_password = str(input('Confirm password: '))