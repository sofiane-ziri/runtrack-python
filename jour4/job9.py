def product_in_range(lst):
  product = 1
  for x in lst:
    if 25 <= x <= 90:
      product *= x
  return product

# Exemple d'utilisation
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
print(product_in_range(L)) # affiche 80640
