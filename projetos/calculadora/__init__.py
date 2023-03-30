from funcoes import *;
import sys;

funcoes_menu={'adicao':adicao, '+':adicao,'subtracao':subtracao,'-':subtracao, 'divisao':divisao,'/':divisao,'multiplicacao':multiplicacao,'*':multiplicacao,'sair':sair};

def calcule():
  x='';
  while (x!='sair'):
    try:
      print(funcoes_menu[x:=input('Digite sua operação:')]((x=='sair' or input('Digite um número a:')),(x=='sair' or input('Digite um número b:'))));
    except TypeError:
      print("Ocorreu um erro:");
      print(sys.exc_info()[1]);
    except KeyError:  
      print(f"Opção inválida. \n Nossas opções são: {','.join(list(funcoes_menu.keys()))}");
      
      
