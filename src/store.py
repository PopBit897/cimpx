from L_cimpx import cls
import time,os
try:
    import inquirer as iq
except:
    os.system('pip3 install inquirer')
from rich import * 
def mac():
        print('installazione in corso ... /install wait ...')
        try:
            os.system('sudo apt-get install macchanger')
        except:
            try:
                os.system('pacman -S macchanger')
            except:
                try:
                    os.system('yum install macchanger')
                except:
                    print('errore ?/error ?')
def store_list():
    

    question=[iq.List("select1",message="Seleziona cosa vuoi scaricare?:",choices=["Emulator","Desktop Enviromrnt","text editor","Game Console","MAC-Spoofing","Home"])]   
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
                                                     ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝ V0.1(building 0.0.2)"""
    while True:
        cls()
        
        print(text_ascii)
        
        answer=iq.prompt(question)['select1']
        
        if "Emulator" in answer:
            cls()
            print('non ce ancora nessuna lista')
            time.sleep(10)
            store_list()
        elif "MAC-Spoofing" in answer:
            mac()
            
        elif 'Home' in answer:
           
            from main import cimpx_main
            cimpx_main()
        elif "Desktop Enviromrnt" in answer:
            cls()
            print(text_ascii)
            question1=[iq.List("select2",message="Seleziona cosa vuoi scaricare?:",choices=["Mate","GNOME","Kde_full","LXDE","Back"])] 
            answer1=iq.prompt(question1)["select2"]
            if 'GNOME' in answer1:
                print('Server ...')
                print('install Gnome ...')
                try:
                    os.system('sudo apt -y gnome-desktop-environment')
                except:
                    try:
                        os.system('pacman -S -y gnome-desktop-environment ')
                    except:
                        os.system('yum install -y gnome-desktop-environment ')
            elif 'Mate' in answer1:
                print('Server ...')
                print('install Mate ...')
                try:
                    os.system('sudo apt mate-desktop-environment')
                except:
                    try:
                        os.system('pacman -S mate-desktop-environment')
                    except:
                        os.system('yum install mate-desktop-environment')
            elif 'KDE' in answer1:
                print('Server ...')
                print('install kde ...')
                try:
                    os.system('sudo  apt install  kde-full')
                except:
                    try:
                        os.system('pacman -S   kde-full')
                    except:
                        os.system('yum  install  kde-full')
            elif 'LXDE' in answer1:
                print('Server ...')
                print('install LXDE ...')
                try:
                    os.system('sudo  apt install lxde')
                except:
                    try:
                        os.system('pacman -S  lxde')
                    except:
                        os.system('yum  install lxde')
        elif 'text editor' in answer:
            question1=[iq.List("select2",message="Seleziona cosa vuoi scaricare?:",choices=["NE","Tilde","Back"])] 
            answer1=iq.prompt(question1)["select2"]
            if 'NE' in answer1:
                print('Server ...')
                print('install nice editor ...')
                try:
                    os.system('sudo apt install ne')
                except:
                    try:
                        os.system('pacman -S ne')
                    except:
                        os.system('yum install ne')
        elif 'Tilde' in answer1:
                print('Server ...')
                print('install tilde editor ...')
                try:
                    os.system('sudo apt install tilde')
                except:
                    try:
                        os.system('pacman -S tilde')
                    except:
                        os.system('yum install tilde')

            

            
store_list()




