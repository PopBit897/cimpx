import os,time

try:
    from platform import python_version
    from tqdm import tqdm
    import inquirer

except :
    print('Not found  librery ')
    os.system('chmod +x setup.sh')
    os.system('./setup.sh')
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
os.system("python3 main.py")