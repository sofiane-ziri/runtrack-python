# On crée la chaîne à partir de "abcdefghijklmnopqrstuvwxyz" multipliée par 10
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# On définit un compteur qui représente le nombre de lignes de la pyramide
compteur = 0

# On parcourt la chaîne par tranches de 26 caractères (une lettre par ligne)
# jusqu'à ce qu'il n'y ait plus assez de caractères pour remplir une ligne
while len(chaine[compteur * 26: (compteur + 1) * 26]) == 26:
  # On récupère la tranche de 26 caractères correspondant à la ligne courante
  ligne = chaine[compteur * 26: (compteur + 1) * 26]
  # On affiche la ligne
  print(ligne)
  # On incrémente le compteur
  compteur += 1

# Si il reste des caractères, on récupère la tranche restante et on l'affiche
reste = chaine[compteur * 26:]
print(reste)
