from funcoes import *;
import sys;

funcoes_menu={'adicao':adicao, '+':adicao};

def calcule():
  while (True):
    try:
      funcoes_menu[input('Digite sua operação:')](input('Digite um número a:'),input('Digite um número b:'));
    except TypeError:
      print("Ocorreu um erro:");
      print(sys.exc_info()[1]);
    except KeyError:  
      print(f"Opção inválida. \n Nossas opções são: {','.join(list(funcoes_menu.keys()))}");