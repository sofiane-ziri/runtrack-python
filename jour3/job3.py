def affiche_sauf_certains_nombres():
  for i in range(101):
    if i in [26, 37, 88]:
      continue
    print(i)

affiche_sauf_certains_nombres()