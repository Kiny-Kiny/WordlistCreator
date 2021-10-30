# Recomendação : Use apenas se seu computador/celular for bom.
# Autor        : Kiny
# Pix          : (61) 9603-5417
# Github       : https://github.com/Kiny-Kiny
# WhatsApp     : http://wa.me/552179180533
# Telegram     : @K_iny
# Instagram    : @parziovanni
# Twitter      : @KinyBruno
############################################
'''Módulos'''
from itertools import product;
from sys import argv,stdout;
from time import sleep;
from os import system;
############################################
'''Cores'''
global R,B,C,G
R='\033[1;31m';
B='\033[1;34m';
C='\033[1;37m';
G='\033[1;32m';
############################################
'''Funções'''
def slow(msg):
	for i in msg: stdout.write(i);sleep(0.007);stdout.flush();

def clear(): system('cls||clear');
############################################
'''Banner'''
logo=B+'''  __  __     __     __   __     __  __    
 /\ \/ /    /\ \   /\ "-.\ \   /\ \_\ \   
 \ \  _"-.  \ \ \  \ \ \-.  \  \ \____ \  
  \ \_\ \_\  \ \_\  \ \_\\"\_\   \/\_____\ 
   \/_/\/_/   \/_/   \/_/ \/_/   \/_____/ \n'''+C

############################################
'''Parte de criação da Wordlist'''
def wordlist(i):
	msg='';res = product('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890', repeat=i);
	for g in res:
		senha=''
		for i in g: senha+=i
		msg+=f'{senha}\n'
	return msg

def main(min,max):
	lis=[]
	slow(
	f'[{G}!{C}] Criando a WordList...\n'
	)
	for i in range(int(min),int(max)): lis.append(str(wordlist(i)));
	msg='';
	for i in lis: msg+=i
	file=open('KingCrimson.txt','w+');
	file.write(msg);
	file.close();
	clear();
	slow(
	f'{logo}\n[{G}Wordilist Criada!{C}] A worlist foi criada e salva no arquivo KingCrimson.txt\n'
	);	

############################################
if int(len(argv)) < 3:
	slow(
	str(logo) + f'\n{G}- {C}Modo de Uso{G} : {C}python3 '+ str(argv[0]) + G+' {'+C+'Quantidade mínima'+G+'} {' +C+'Quantidade Máxima'+G+'}\n'+C
	);exit();

try: int(argv[1]);int(argv[2]);
except: slow(
f'{logo}\n[{R}Error{C}] Use apenas números inteiros! (ex: 7)\n'
);exit();

if __name__=='__main__':
	clear()
	if int(argv[1]) == int(argv[2]):
		slow(
		f'{logo}\n[{R}Error{C}] A quantidade mínima não pode ser igual a quantidade máxima.\n'
		
		);
	elif int(argv[1]) > int(argv[2]):
		slow(
		f'{logo}\n[{R}Error{C}] A quantidade mínima não pode ser maior que a quantidade máxima.\n'
		);
	else:
		try:
			main(int(argv[1]),int(argv[2]));
		except:
			clear();
			slow(
			f'{logo}[{R}Error{C}] Erro Desconhecido.\n'
			);
