from __future__ import print_function
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

# software other brand open source software ,cimpx store v0.1Pre-Alpha
def store():
    cls()
    text_ascii="""
            ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗███╗░░░███╗██████╗░██╗░░██╗
            ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║████╗░████║██╔══██╗╚██╗██╔╝
            ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ██║░░╚═╝██║██╔████╔██║██████╔╝░╚███╔╝░
            ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ██║░░██╗██║██║╚██╔╝██║██╔═══╝░░██╔██╗░
            ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ╚█████╔╝██║██║░╚═╝░██║██║░░░░░██╔╝╚██╗
            ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝

                                                            ░██████╗████████╗░█████╗░██████╗░███████╗
                                                            ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██╔════╝
                                                            ╚█████╗░░░░██║░░░██║░░██║██████╔╝█████╗░░
                                                            ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██╔══╝░░
                                                            ██████╔╝░░░██║░░░╚█████╔╝██║░░██║███████╗
                                                            ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝ V0.1(store versione)"""
    print(text_ascii)
    print('\n emulator :1'), print('server:2')
    print('desktop:3')     ,print('game(terminal):4')
    print('text editor:5')
    try:
        command_st=input('>>> ')
    except:
        command_st=input('>>> ')

    if command_st =='1':
        print('sorry is pre-alpha store,mi dispiace e un store pre-alpha')
    if command_st =='3':
        cls()
        print('MATE:1')      ,print('Enlightenment:2'),print('Cinnamon:3')
        print('GNOME:4')     ,print('LXDE:5')          ,print('Deepin:6')
        print('KDE Plasma:7') ,print('LXQT:8')
        try:
         c_st=input('>>')
        except:
             c_st=input('>>')
        if c_st =='1':
            print('aggiornamento in corso ..')
            time.sleep(0.5)
            os.system('sudo apt update ')

            print('sto scaricando MATE')
            time.sleep(0.5)
            os.system('sudo apt install mate-desktop-environment')
            os.system('sudo reboot now')
        if c_st=='2':
            print('aggirnamento in corso..')
            os.system('sudo apt update')
            print('sto scaricando  enlightenmemt')
            time.sleep(0.5)
            os.system('sudo apt -y install enlightenment')
            os.system('sudo reboot now')
        if c_st =='3':
            print('sto aggungendo PPA reposetery')
            time.sleep(0.5)
            os.system('sudo add-apt-repository ppa:embrosyn/cinnamon')
            print('aggiornamento in corso ..')
            os.system('sudo apt update')
            print('sto scaricando cinnamon')
            time.sleep('sudo apt install cinnamon')
            os.system('sudo reboot now')
        if c_st=='4':
            print('aggiornamento in corso..')
            time.sleep(0.5)
            os.system('sudo apt update')
            print('sto scaricando  GNOME')
            time.sleep(0.5)
            os.system('sudo apt-get install -y gnome-desktop-environment')
            os.system('sudo reboot now')
        if c_st=='5':
            print('aggiornamento in corso..')
            time.sleep(0.5)
            print('sto scaricando LXDE')
            time.sleep(0.5)
            os.system('sudo apt install lxde')
            os.system('sudo reboot now')
            
        if c_st=='6':
            print('aggiunta della repo deepi')
            time.sleep(0.5)
            os.system('sudo add-apt-repository ppa:leaeasy/dde')
            print('aggiornamento in corso..')
            time.sleep(0.5)
            os.system('sudo apt update')
            print('installazione in corso..')
            time.sleep(0.5)
            os.system('sudo apt install dde')
            
            print(' installazione di deepin file maneger')
            time.sleep(0.5)
            os.system('sudo apt-get install dde-file-manager')
            print('install theme')
            time.sleep(0.5)
            os.system('sudo apt install deepin-gtk-theme')
            os.system('sudo reboot now')
        if c_st=='7':
            print('aggirnamento in corso..')
            os.system('sudo apt update')
            time.sleep(0.5)
            print('KDE plasma full version install(1GB)')
            time.sleep(0.5)
            os.system('sudo apt install kde-full')
            os.system('sudo reboot now')

        if c_st=='8':
            print('aggiornamento in corso..')
            os.system('sudo apt update')
            time.sleep(0.5)
            os.system('sudo apt install lxqt sddm')
            os.system('sudo reboot now')

    if command_st=='4':
        cls()
        print('Moon-buggy:1'),print('sudoku:2')
        print('nInvaders:3'),print('Pac-Man:4')
        try:
            c_game=input('>>')
        except:
            c_game=input('>>')
        if c_game =='1':
            print('installa moon-buggy')
            os.system('sudo apt-get install moon-buggy')
           
        if c_game =='2':
            print('installa sudoko')
            os.system('sudo apt-get install sudoku')
        if c_game =='3':
            print('installa nInvaders')
            os.system('sudo apt-get install  ninvaders')
        if c_game =='4':
            print('installa pac-man')
            os.system('sudo apt-get install pacman4console')
    if command_st=='5':

        print('tilde:1'),print('The nice editor:2')
        try:
            c_ed=input('>>')
        except:
            c_ed=input('>>')
        if c_ed=='1':
            print('Sto installando tilde')
            time.sleep(0.5)
            os.system('sudo apt install tilde')
        if c_ed=='2':
            print('Sto installando The nice editor')
            time.sleep(0.5)
            os.system('sudo apt install ne')




























































































































































            
