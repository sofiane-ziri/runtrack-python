def est_premier(n):
  # On vérifie si n est égal à 2, auquel cas on le considère comme premier
  if n == 2:
    return True
  # On vérifie si n est inférieur à 2, auquel cas on le considère comme non premier
  if n < 2:
    return False

  # On commence à 2 et on teste tous les nombres entiers jusqu'à la racine carrée de n
  for i in range(2, int(n ** 0.5) + 1):
    # Si n est divisible par i, alors il n'est pas premier
    if n % i == 0:
      return False
  # Si aucun nombre jusqu'à la racine carrée de n ne divise n, alors n est premier
  return True

# On parcourt tous les nombres entiers de 2 à 1000
for n in range(2, 1001):
  # Si n est premier, on l'affiche
  if est_premier(n):
    print(n)
