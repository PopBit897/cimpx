import os,time ,socket
from L_cimpx import *
from info import info1
cls()

host_pc=socket.gethostname()
ip_pc=socket.gethostbyname(host_pc)
text1="""
								░█████╗░██╗███╗░░░███╗██████╗░██╗░░██╗
								██╔══██╗██║████╗░████║██╔══██╗╚██╗██╔╝
								██║░░╚═╝██║██╔████╔██║██████╔╝░╚███╔╝░
								██║░░██╗██║██║╚██╔╝██║██╔═══╝░░██╔██╗░
								╚█████╔╝██║██║░╚═╝░██║██║░░░░░██╔╝╚██╗
								░╚════╝░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝░░╚═╝V0.2\n """

print(text1)
print('hostname del tuo pc :',host_pc)
print('il tuo ip del pc e :',ip_pc)
text_info="""\nPer info digita:cimpx -i,per aiuto digita:cimpx -h . per cancellare digita:cls"""

print(text_info)
while True:
	command=input('>>> ')
	if command == 'ne -u':
		ne_u()
	if command == 'ne':
		try:
			ne()
		except:
			print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
	
	if command == 'tilde':
		try:
			tilde()
		except:
			print('non e stato scaricato vai sul cimpx store(cimpx -st) ')

	if command  == 'pacman':
		try:
			pacman()
		except:
			print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
	if command == 'ninvaders':
		try:
			nInvaders()
		except:
			print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
	if command=='moon':
		try:
			moon()
		except:
			print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
	if command == 'sudoku':
		try:
			sudoku()
		except:
			print('non e stato scaricato vai sul cimpx store(cimpx -st) ')
	if command =='cls':
		cls()
	if command =='cimpx -h':
		print('per riavviare il pc linux digita:pc -r')
		print('\nper sapere il nome locale pc digita:pc -h')
		print('\nper cambiare nome locale digita:pc -nw -h')
		print('\nper spegnere il pc digita:pc -s')
		print('\nin caso che tu voglia digitare un commando non essistentte digita:cimpx -xc')# xc = linux command
		print('\nper installare altri app prodotti da RDA2ITA digita:cimpx -o')
		print('per info su come avviare software dal cimpx store:store -h')
		print('per info su come disinstallare un software che hai scaricato dal cimpx store digita:store -u')
	if command =='store -u':
		print('		Per disinstallare giochi:')
		print('moon -u')
		print('sudoku -u')
		print('ninvaders -u')
		print('\npacman -u')
		print('		Per text editri:')
		print('ne -u')
		print('tilde -u')
	if command =='moon -u':
		moon_u()
	if command == 'sudoku -u':
		sudoku_u()
	if command == 'ninvaders -u':
		nInvaders_u()
	if command == 'pacman -u':
		pacman_u()
	if command == 'ne -u':
		ne_u()
	if command == 'tilde -u':
		tilde_u()
	if command =='store -h':
		helprun()
	if command =='cimpx -i':
		info1()
	if command =='pc -nw -h':
		nw_host()
	if command =='cimpx -v':
		cv()
	if command =='pc -h':
		print(host_pc)
	if command =='pc -r':
		reboot()
	if command=='cimpx -xc':
		no_cimpx_com()
	if command =='cimpx -o':
		print('per scaricare ip-tools 0.0.1 digita:ip -v0.0.1')
		print('per scaricare ip-tools sucesiva versione digita:ip -nw')
		print('per scaricare la versione GUI digita:ip -GUI')
		print('per scaricare GeneratorePassword digita:GP ')
		print('invece se vuoi una versione grafica installer digita :auto -i')
		print('per altri software digita:cimpx -st')
	if command == 'cimpx -st':
		store()
	if command =='ip -v0.0.1':
		bw_o()
	if command == 'ip -nw':
		d_nw()
	if command =='ip -GUI':
		ip_gui()
    