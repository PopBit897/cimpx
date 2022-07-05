import os,time
from platform import python_version
from tqdm import tqdm
text_ascii="""
            ░█████╗░██╗███╗░░░███╗██████╗░██╗░░██╗
            ██╔══██╗██║████╗░████║██╔══██╗╚██╗██╔╝
            ██║░░╚═╝██║██╔████╔██║██████╔╝░╚███╔╝░
            ██║░░██╗██║██║╚██╔╝██║██╔═══╝░░██╔██╗░
            ╚█████╔╝██║██║░╚═╝░██║██║░░░░░██╔╝╚██╗
            ░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝V.0.2\n  """

text1='bootloader ...\n'

print(                   text_ascii                       )


for i in tqdm(range(100)):
    time.sleep(0.1)

try:
    os.system('python3 main.py ')
except :
    print('not found python3 or tqdm librery ')
    os.system('setup.py')