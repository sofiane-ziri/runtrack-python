def fruits_et_legumes(type, saison):
  if type == "fruits":
    if saison == "hiver":
      print("orange, mandarine et kiwi")
    elif saison == "été":
      print("Poire, fraise, cassis")
  elif type == "légumes":
    if saison == "hiver":
      print("carotte, topinambour, endive")
    elif saison == "été":
      print("artichaut, aubergine, navet")


fruits_et_legumes("fruits", "hiver")  # affiche "orange, mandarine et kiwi"
fruits_et_legumes("fruits", "été")  # affiche "Poire, fraise, cassis"
fruits_et_legumes("légumes", "hiver")  # affiche "carotte, topinambour, endive"
fruits_et_legumes("légumes", "été")  # affiche "artichaut, aubergine, navet"


