def sum_evens(lst):
  sum = 0
  for x in lst:
    if x % 2 == 0:
      sum += x
  return sum

# Exemple d'utilisation
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
print(sum_evens(L)) # affiche 168
