import os,time
from tqdm import tqdm
text_ascii="""
            ░█████╗░██╗███╗░░░███╗██████╗░██╗░░██╗
            ██╔══██╗██║████╗░████║██╔══██╗╚██╗██╔╝
            ██║░░╚═╝██║██╔████╔██║██████╔╝░╚███╔╝░
            ██║░░██╗██║██║╚██╔╝██║██╔═══╝░░██╔██╗░
            ╚█████╔╝██║██║░╚═╝░██║██║░░░░░██╔╝╚██╗
            ░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝V.0.2\n  """
py = os.system('python -version') 
py3=os.system('python3 -version')
text1='bootloader ...\n'
text2='ricerca python versione:python2%s ,python3%s'%(py,py3)
text3='attendere perfavore...'

print(                   text_ascii                       )


for i in tqdm(range(100)):
    time.sleep(0.1)
    t=print(text1)
time.sleep(0.5)
t=print(text2)
for i in tqdm(range(100)):
    time.sleep(0.1)
    t=print(text3)
time.sleep(0.2)





try:    
    os.system('python3 main.py ')
except:
    print('not found python3 ')
    try:
        os.system('python main.py')
    except:
        print('not found python')
        print('sto aggiornado la reposetery..')
        os.system('sudo apt update -y && sudo apt update -y')
        print('sto scaricando python ultima versione')
        os.system('sudo apt install python3')
