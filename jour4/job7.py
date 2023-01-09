def count_multiples_of_3(lst):
  count = 0
  for x in lst:
    if x % 3 == 0:
      count += 1
  return count

# Exemple d'utilisation
L = [8, 24, 48, 2, 16]
print(count_multiples_of_3(L)) # affiche 2
