#Pass permet de passer la ligne de code sans rien faire de particulier.
var = None

match var : 
    case "Bleu":
        print("couleur primaire bleu") 
    case "Rouge":
        print("couleur primaire rouge")
    case "jaune":
        print("couleur primaire jaune")
    case "vert":
        pass
    case "Noir" "blanc":
        pass
    case _ : 
        print("Ce n'est pas une couleur")
