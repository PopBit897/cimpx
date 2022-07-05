from L_cimpx import cls
import time,os
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
                                                            ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝ V0.1(building 0.0.1)"""
    print(text_ascii)
    print('\n emulator :1'), print('server:2')
    print('desktop:3')     ,print('game(terminal):4')
    print('text editor:5')
    print('Per tornare indietro clicca invia ,se vui tornare su cimpx  clicca invia in questa finestra')
    print('ATTENZIONE store pre-relese build 0.0.1 version =0.1_Pre-alpha')
    try:
        command_st=input('>>> ')
    except:
        command_st=input('>>> ')

    if command_st =='1':
        print('sorry is pre-alpha store,mi dispiace e un store pre-alpha')
        store()
    if command_st =='3':
        cls()
        print('MATE:1')      ,print('Enlightenment:2'),print('Cinnamon:3')
        print('GNOME:4')     ,print('LXDE:5')          ,print('Deepin:6')
        print('KDE Plasma:7') ,print('LXQT:8')
        try:
         c_st=input('>>')
        except:
             c_st=input('>>')
        if c_st == 'exit':
            os.system('python3 main.py')
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
        else : 
            store()
        if c_st=='6':
            print('faill install sorry ppa leaeasy/dde not working (for your self code pythone is desable)')
         #   time.sleep(0.5)
         #   os.system('sudo add-apt-repository ppa:leaeasy/dde')
          #  print('aggiornamento in corso..')
          #  time.sleep(0.5)
          #  os.system('sudo apt update')
            #print('installazione in corso..')
          #  time.sleep(0.5)
           # os.system('sudo apt install dde')
            
            #print(' installazione di deepin file maneger')
           # time.sleep(0.5)
            #os.system('sudo apt-get install dde-file-manager')
            #print('install theme')
            #time.sleep(0.5)
          #  os.system('sudo apt install deepin-gtk-theme')
           # os.system('sudo reboot now')
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
            store()
           
        if c_game =='2':
            print('installa sudoko')
            os.system('sudo apt-get install sudoku')
            store()
        if c_game =='3':
            print('installa nInvaders')
            os.system('sudo apt-get install  ninvaders')
            store()
        if c_game =='4':
            print('installa pac-man')
            os.system('sudo apt-get install pacman4console')
            store()
        else:
            store()
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
            store()
        if c_ed=='2':
            print('Sto installando The nice editor')
            time.sleep(0.5)
            os.system('sudo apt install ne')
            store()
        else:
            store()

    else:
        import main 










