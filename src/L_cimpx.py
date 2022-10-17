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
# def  command game and app start  use cimpx software
def moon():
    os.system('moon-buggy')
def sudoku():
    os.system('sudoku')
def nInvaders():
    os.system('ninvaders')
def pacman():
    os.system('pacman4console')
def tilde():
    os.system('tilde')
def ne():
    os.system('ne')
# remove app form cimpx store 
def moon_u():
    os.system('sudo apt remove moon-buggy')
def sudoku_u():
    os.system('sudo apt remove sudoku')
def nInvaders_u():
    os.system('sudo apt remove ninvaders')
def pacman_u():
    os.system('sudo apt remove pacman4console')
def tilde_u():
    os.system('sudo apt remove tilde')
def ne_u():
    os.system('sudo apt remove ne')
    
# help run software download to cimpx store(info baner )
def helprun():
    cls()
    print('Avviare software scaricati da cimpx store.')
    print('\nAvvio giochi :')
    print('per avviare moon-buggy su cimpx digita:moon')
    print('per avviare sudoku su cimpx digita:sudoku')
    print('per avviare nInvaders su cimpx digita:ninvaders')
    print('per avviare pacman4console(pac-man) su cimpx digita:pacman')
    print('Avvio text editor:')
    print('per avviare tilde su cimpx digita:tilde')
    print('per avviare The nice editor su cimpx digita:ne')
    print('\nAvvia software con linux .')
    print('Aviare giochi:')
    print('per avviare moon-buggy su linux digita:moon-buggy')
    print('per avviare sudoku su linux digita:sodoku')
    print('per avviare nInvaders su linux digita:ninvaders')
    print('per avviare pacman4console(pac-man) su linux digita:pacman4console')
    print('\nAvvio text editor')
    print('Prima cosa avviare la funzione cimpx -xc o pure uscire da cimpx')
    print('per avviare tilde su linux digita:tilde')
    print('per avviare the nice editor su linux digita:ne')

# software other brand open source software ,cimpx store v0.1Pre-Alpha move to store.py file 

def store():
   from store import store_list
   store_list()













































































































            
