lettre_a_chercher = "e"
phrase = str(input('entrer un mot :'))

resultat = phrase.lower().count(lettre_a_chercher)

if resultat >=1 :
    print('il i a ya',(resultat) ,'de e dans ce mot')

   
else :

    print("rien")