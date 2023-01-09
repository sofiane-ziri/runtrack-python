def triangle(a, b, c):
  if a + b > c and a + c > b and b + c > a:
    print("Il est possible de construire un triangle avec ces longueurs.")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
      print("Ce triangle est rectangle.")
    elif a == b or a == c or b == c:
      print("Ce triangle est isocèle.")
    elif a == b and b == c:
      print("Ce triangle est équilatéral.")
    else:
      print("Ce triangle est quelconque.")
  else:
    print("Il n'est pas possible de construire un triangle avec ces longueurs.")


triangle(3, 4, 5)  # affiche "Il est possible de construire un triangle avec ces longueurs. Ce triangle est rectangle."
triangle(3, 3, 3)  # affiche "Il est possible de construire un triangle avec ces longueurs. Ce triangle est équilatéral."
triangle(3, 3, 4)  # affiche "Il est possible de construire un triangle avec ces longueurs. Ce triangle est isocèle."
triangle(1, 2, 3)  # affiche "Il n'est pas possible de construire un triangle avec ces longueurs."