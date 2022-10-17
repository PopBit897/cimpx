import os,time ,socket
from L_cimpx import *
from info import info1,version
import platform as pl
import inquirer as iq
from rich import *


def cimpx_main():
	cls()

	host_pc=socket.gethostname()
	ip_pc=socket.gethostbyname(host_pc)
	text1="""
									░█████╗░██╗███╗░░░███╗██████╗░██╗░░██╗
									██╔══██╗██║████╗░████║██╔══██╗╚██╗██╔╝
									██║░░╚═╝██║██╔████╔██║██████╔╝░╚███╔╝░
									██║░░██╗██║██║╚██╔╝██║██╔═══╝░░██╔██╗░
									╚█████╔╝██║██║░╚═╝░██║██║░░░░░██╔╝╚██╗
									░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝V 0.2\n """
	print('Copyright (c) 2022 RedAnonymusITA2021')
	print(text1)
	print('hostname del tuo pc :',host_pc)
	print('il tuo ip del pc e :',ip_pc)
	text_info="""\nPer info digita: cimpx -i,per aiuto digita: cimpx -h . per cancellare digita: cls"""

	print(text_info)

	while True:

		command=input('>>> ')
		if command  =='cimpx --version':
			version()
		elif command == 'ping':
			host=input('Nome host://')
			os.system('ping %s'%(host))

		elif command == 'pc -nw -MAC':
			
			cm=input('tu hai scaricato macchanger? /you have macchanger download?[y/n]: ').lower()
			if 'y' in cm:
				com_i=input("interface name://")
				print('avvio MAC Spoofing /Start MAC Spoofing')
				os.system('ifconfig %s down'%(com_i))
				os.system('mecchanger -r %s'%(com_i))
				os.system('ifconfig %s up'%(com_i))
				os.system('service network-manager restart')
			elif 'n' in cm:
				com_i=input("interface name://")
				from store import mac
				mac()
				print('avvio MAC Spoofing /Start MAC Spoofing')
				os.system('ifconfig %s down'%(com_i))
				os.system('mecchanger -r %s'%(com_i))
				os.system('ifconfig %s up'%(com_i))
				os.system('service network-manager restart')

			

		elif command == 'ne -u':
			ne_u()
		elif command == 'ne':
			try:
				ne()
			except:
				print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
		
		elif command == 'tilde':
			try:
				tilde()
			except:
				print('non e stato scaricato vai sul cimpx store(cimpx -st) ')

		elif command  == 'pacman':
			try:
				pacman()
			except:
				print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
		elif command == 'ninvaders':
			try:
				nInvaders()
			except:
				print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
		elif command=='moon':
			try:
				moon()
			except:
				print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
		elif command == 'sudoku':
			try:
				sudoku()
			except:
				print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
		elif command =='cls':
			cls()
		
		elif command =='cimpx -h':
			print('per riavviare il pc linux digita:pc -r')
			print('\nper sapere il nome locale pc digita:pc -h')
			print('\nper cambiare nome locale digita:pc -nw -h')
			print('MAC Spoofing(requisito macchanger) digita:pc -nw -MAC')
			print('\nper spegnere il pc digita:pc -s')
			print('\nin caso che tu voglia digitare un commando non essistentte digita:cimpx -xc')# xc = linux command
			print('\nper installare altri app prodotti da RDA2ITA digita:cimpx -o')
			print('per altri software digita:cimpx -st')
			print('per info su come avviare software dal cimpx store:store -h')
			print('per info su come disinstallare un software che hai scaricato dal cimpx store digita:store -u')
			
		elif command =='store -u':
			print('		Per disinstallare giochi:')
			print('moon -u')
			print('sudoku -u')
			print('ninvaders -u')
			print('\npacman -u')
			print('		Per text editri:')
			print('ne -u')
			print('tilde -u')
		elif command =='moon -u':
			moon_u()
		elif command == 'sudoku -u':
			sudoku_u()
		elif command == 'ninvaders -u':
			nInvaders_u()
		elif command == 'pacman -u':
			pacman_u()
		elif command == 'ne -u':
			ne_u()
		elif command == 'tilde -u':
			tilde_u()
		elif command =='store -h':
			helprun()
		elif command =='cimpx -i':
			info1()
		elif command =='pc -nw -h':
			nw_host()
		elif command =='cimpx -v':
			cv()
		elif command =='pc -h':
			print(host_pc)
		elif command =='pc -r':
			reboot()
		elif command=='cimpx -xc':
			no_cimpx_com()
		elif command =='cimpx -o':
			print('per scaricare ip-tools 0.0.1 digita:ip -v0.0.1')
			print('per scaricare ip-tools sucesiva versione digita:ip -nw')
			print('per scaricare la versione GUI digita:ip -GUI')
			print('per scaricare GeneratorePassword digita:GP ')
			print('invece se vuoi una versione grafica installer digita :auto -i')
			
		elif command == 'cimpx -st':
			store()
		elif command =='ip -v0.0.1':
			bw_o()
		elif command == 'ip -nw':
			d_nw()
		elif command =='ip -GUI':
			ip_gui()
cimpx_main()