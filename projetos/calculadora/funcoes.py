def operacoes(a,b,operacao,char):
  try:
    new_a=float(a);
    new_b=float(b);
  except:
    erro=f"O input 'a' e 'b' devem ser números. Recebemos a={a}, {type(a)} e b={b}, {type(b)}";
    raise TypeError(erro);
  else:
    print(a,char,b,'=',operacao(new_a,new_b));
  

def adicao(a,b):
  operacoes(a,b,lambda x,y: x+y,"+");
    

def subtracao(a,b):
  operacoes(a,b,lambda x,y: x-y,'-');
  