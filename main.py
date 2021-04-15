import os
import subprocess
from sys import platform,executable
from subprocess import call
from random import choice
from time import sleep

def restart():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def clear():
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    call(command, shell=True)
    
vermelho = '\033[1;31m'
verde = '\033[1;32m'
a = '\033[m[\033[1;33m+\033[m]'

print('{} Verificando atualizações...'.format(a))
update = subprocess.check_output('git pull', shell=True)
if 'Already up to date' not in update.decode():
    print('{} Atualizado com sucesso,iniciando...\n'.format(a))
    sleep(3)
    subprocess.run('clear')
    restart()
else:
    print('{} Nenhuma atualização disponível.'.format(a))
    sleep(3)
    
clear()

nome = input('{} Me diga como quer ser chamado: '.format(a))

while True:
    tema = input('''{} Qual tema você quer usar na ferramenta?
    
[\033[1;33m1\033[m] - Vermelho
[\033[1;33m2\033[m] - Verde
    
>>> '''.format(a))
    if tema == '1':
        print('\nTema definido para {}vermelho!\n'.format(vermelho))
        sleep(2)
        b = '\033[1;31m'
        c = '\033[m'
        break
    elif tema == '2':
        print('\nTema definido para {}verde!\n'.format(verde))
        sleep(2)
        b = '\033[1;32m'
        c = '\033[m'
        break
    else:
        print('\nOpção inválida\n')

welcome = ['Bem vindo','Use com moderação','Use com consiência','Você é foda','Você é o mais brabo']
kkk = choice(welcome)
erro = '{} Ops! Parece que você escolheu uma opção não definida'.format(a)
while True:
    clear()
    menu = input('''
{0}  ____ _     _____   _____ ___   ___  _
 / ___| |   |___ /  |_   _/ _ \ / _ \| |
| |   | |     |_ \    | || | | | | | | |
| |___| |___ ___) |   | || |_| | |_| | |___
 \____|_____|____/    |_| \___/ \___/|_____|{1}
    
    
{2} {0}{3}!{1}

{0}[{1}1{0}]{1} - Spam
{0}[{1}2{0}]{1} - Ataque DDoS
{0}[{1}3{0}]{1} - Puxar dados
{0}[{1}4{0}]{1} - Ferramentas hacker
{0}[{1}5{0}]{1} - Mùsicas
{0}[{1}6{0}]{1} - Gerar câmeras de segueança
{0}[{1}7{0}]{1} - Criar um vírus
{0}[{1}8{0}]{1} - BOTs para WhatsApp

{0}[{1}111{0}]{1} - Chat do lost
{0}[{1}222{0}]{1} - Chat do Causs
{0}[{1}333{0}]{1} - Canal do lost
{0}[{1}444{0}]{1} - Canal do causs
{0}[{1}555{0}]{1} - IG do lost
{0}[{1}666{0}]{1} - IG do causs

{0}[{1}777{0}]{1} - Reportar/Pedidos

{0}[{1}0{0}]{1} - Sair

{0}>>>{1} '''.format(b,c,kkk,nome))

    if menu == '1':
        clear()
        spam = input('''

{0} ____  ____   _    __  __
/ ___||  _ \ / \  |  \/  |
\___ \| |_) / _ \ | |\/| |
 ___) |  __/ ___ \| |  | |
|____/|_| /_/   \_\_|  |_|
{1}
{0}[{1}1{0}]{1} - Spam SMS
{0}[{1}2{0}]{1} - Voltar

{0}>>>{1} '''.format(b,c))

        if spam == '1':
            if platform not in ('win32', 'cygwin'):
                command = 'node tools/spam.js'
            call(command, shell=True)
            break
        elif spam == '2':
            print(menu)
    elif menu == '2':
        ddos = input('''
{0}
 ____  ____       ____
|  _ \|  _ \  ___/ ___|         
| | | | | | |/ _ \___ \
| |_| | |_| | (_) |__) |
|____/|____/ \___/____/{1}

{0}[{1}1{0}]{1} - Iniciar ataque DDoS
{0}[{1}2{0}]{1} - Voltar

{0}>>>{1}'''.format(b,c))

        if ddos == '1':
            ip = input('\n\n\033[mDigite o IP da vítima: \033[1;31m\n\n')
            if platform not in ('win32', 'cygwin'):
                command = 'python tools/hammer.py -s {} -p80 -t135'.format(ip)
            call(command, shell=True)
            break
        else:
            print(menu)
            
    elif menu == '3':
        if platform not in ('win32', 'cygwin'):
            command = 'sh tools/painel.sh'
        call(command, shell=True)
    elif menu == '0':
        print(erro)
        sleep(2)
        print(menu)
    else:
        print('\nSaindo em 2 segundos...\n')
        sleep(2)
        break
