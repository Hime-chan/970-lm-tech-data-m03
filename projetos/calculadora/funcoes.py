def operacoes(a,b,operacao,char):
  try:
    new_a=float(a);
    new_b=float(b);
  except:
    erro=f"O input 'a' e 'b' devem ser números. Recebemos a={a}, {type(a)} e b={b}, {type(b)}";
    raise TypeError(erro);
  else:
    return (a+char+b+'='+str(operacao(new_a,new_b)));
  
def adicao(a,b):
  return operacoes(a,b,lambda x,y: x+y,"+");
    
def subtracao(a,b):
  return operacoes(a,b,lambda x,y: x-y,'-');
  
def divisao_aux(a,b):
  if (b==0):
    raise TypeError("Divisão inválida! O denominador (dividendo) não pode ser zero.");
    return 0;
  else:
    return a/b;
  
def divisao(a,b):
  return operacoes(a,b,divisao_aux,'/');

def multiplicacao(a,b):
  return operacoes(a,b,lambda x,y: x*y,'*');       
  
  