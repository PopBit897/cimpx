import os,time,webbrowser

#downlod ip-tools terminal ,terminal lest version and GUI and other software by RDA2ITA and no
def d_nw():
    os.system('git clone https://github.com/RedAnonymusITA/ip-tools.git')
    print('collegamento server in corso a github.com')
    os.system('clear')
def bw_o():
    url ='https://github.com/RedAnonymusITA/ip-tools/releases/tag/v0.0.1'
    print('Apertura in corso del tuo browser...')
    try:
        webbrowser.open(url)
    except:
        print('errore con webbrowser librery :( ')

def ip_gui():
    os.system('git clone https://github.com/RedAnonymusITA/ip_tools_GUI.git')
    print('collegamento server in corso a github.com')
    os.system('clear')
def GP():
    os.system('git clone https://github.com/RedAnonymusITA/Generatore_Password.git')
    print('collegamento server in corso a github.com')
    os.system('clear')


# def command
def reboot():
    print('Sei sicuro che vuoi riavviare il sistema digita:si o no')
    com=input('>>> ')
    if com=='si':
        os.system('sudo reboot now ')
    if com=='no':
        os.system('clear')
def shutdown ():
    print('Sei sicuro che vuoi spegnere il tuo pc :si o no')
    com = input('>>> ')
    if com =='si':
        os.system('shutdown')
    if com=='no':
        os.system('clear')
def nw_host():
    com0=input('Sei sicuro che voui cambiare il nome locale si o no:')
    if com0=='si':
        com=input('Scrivi qui il nuovo nome locale > ')
        os.system('hostnamectl set-hostname %s'%(com))
        os.system('python3 main.py')
        os.system('clear')
def cls():
    os.system('clear')
def no_cimpx_com():
    print('Linux command ,per uscire dalla modalita digita:cimpx -ex -xc ')
    command2=input('>>> ')
    os.system(command2)
    print('tempo di riavvio app sono 10s')
    tempo=time.sleep(10)
    cimpx_reboot()
    if command2 =='cimpx -ex -xc':
        cls()
def cimpx_reboot():
    os.system('python3 main.py')
    pass
def cv():
    print('versione cimpx e :V0.1_pre-Alpha')
