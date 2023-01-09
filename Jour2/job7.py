

def categorize_developer(langage: str) -> None:
    if langage == "javascript":
        print("tu es un developpeur web")
    elif langage == "python":
        print("tu es un developpeur IA")
    elif langage == "java":
        print("tu es un developpeur logiciel")
    elif langage == "reactjs":
        print("tu es un developpeur mobile")
    else:
        print("un jour, je serai le meilleur developpeur...")

categorize_developer("javascript")  # affiche "tu es un developpeur web"
categorize_developer("python")  # affiche "tu es un developpeur IA"
categorize_developer("java")  # affiche "tu es un developpeur logiciel"
categorize_developer("reactjs")  # affiche "tu es un developpeur mobile"
categorize_developer("c++")  # affiche "un jour, je serai le meilleur developpeur..."



