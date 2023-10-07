def aprov (media,menor_nota):
  if media >= 7 and menor_nota > 5.1:
    return 'Aprovado'
  else:
    return 'Reprovado'

print(aprov(10,8))