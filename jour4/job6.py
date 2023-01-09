def swap_first_last(lst):
  # On vérifie que la liste contient au moins deux éléments
  if len(lst) < 2:
    return lst
  
  # On échange les valeurs des deux premiers éléments
  lst[0], lst[-1] = lst[-1], lst[0]
  return lst

# Exemple d'utilisation
print(swap_first_last([1, 2, 3, 4])) # affiche [4, 2, 3, 1]
print(swap_first_last([1])) # affiche [1]
