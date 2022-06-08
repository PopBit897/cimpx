import os,time ,socket
from L_cimpx import *
from info import info1
cls()

host_pc=socket.gethostname()
ip_pc=socket.gethostbyname(host_pc)
text1='Benvenuto/a nel controllo il mio pc linux (cimpx)\n'

print(text1)
print('hostname del tuo pc :',host_pc)
print('il tuo ip del pc e :',ip_pc)


text_info="""\nPer info digita:cimpx -i,per aiuto digita:cimpx -h . per cancellare digita:cls"""

print(text_info)
while True:

	command=input('>>> ')

	if command =='cls':
		cls()
	if command =='cimpx -h':
		print('per riavviare il pc linux digita:pc -r')
		print('per sapere il nome locale pc digita:pc -h')
		print('per cambiare nome locale digita:pc -nw -h')
		print('per spegnere il pc digita:pc -s')
		print('in caso che tu voglia digitare un commando non essistentte digita:cimpx -xc')# xc = linux command
		print('per installare altri app prodatti da RDA2ITA digita:cimpx -o')
		print('per usare un editore testo digita:cimpx -txt(non e disponibile nella versione pre-alpha)')

		pass
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
