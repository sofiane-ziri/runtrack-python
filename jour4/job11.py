def increment_list(lst):
  for i in range(len(lst)):
    lst[i] += 1
  return lst

# Exemple d'utilisation
L = [7, 11, 42, 39, 2]
L_incremented = list(map(lambda x: x+1, L))
print(increment_list(L)) # affiche [8, 12, 43, 40, 3]
