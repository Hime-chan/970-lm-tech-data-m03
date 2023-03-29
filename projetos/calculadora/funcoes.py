def adicao(a,b):
  try:
    new_a=float(a);
    new_b=float(b);
  except:
    erro=f"O input 'a' e 'b' devem ser números. Recebemos a={a}, {type(a)} e b={b}, {type(b)}";
    raise TypeError(erro);
  else:
    print(new_a+new_b);