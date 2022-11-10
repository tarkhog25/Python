import csv
from math import *
f = open('texte.csv','r')
contenu = csv.reader(f, delimiter=";")
tab_contenu = list(contenu)
master_key = "27,17,19,0,12,1,24,15.562305898749054,9.090169943749475,2.618033988749895,9.090169943749475,1.0,26," 
#Comme son nom l'indique, c'est tout simplement la clé maitre qui permet d'accèder au mdp sinon tout le programme ne serait
#qu'un vulgaire crypteur/décrypteur. 
#Evidemment la clé maitre est cryptée. 

def numero_alpha(n):
    """fonction qui renvoie le numero de l'alphabet """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','!','M']
    if str(n).isnumeric() == True :
        return alphabet[int(n)]
    else :
        for i in range(len(alphabet)) :
            if alphabet[i] == n : #Bon, apres quelques mintues recherche je pense que le probleme de mon code se trouve ici, je vais essayer de regler ça
                #Ok la fonction ne renvoie rien, c'est bizarre, je me dois d'enqueter. 
                return str(i)

def lettre_ou_chiffre_dans_crypt(m) :
    """Je sais pas trop comment la décrire et j'ai la flm mais en gros trouve chaque mots  du mot de passe crypté, 
    bon c'est vraiment pas clair mdrr, de toute facon je me comprends donc pas grave, si un jour quelqu'un lit ça 
    bah bonne chance pour comprendre ce que fais la fonction uniquement avec ce que j'ai expliqué enfin essayer d"expliquer,
    en écrivant ça je me rends compte que j'aurai du juste regarder une façon simple de cryptage et décryptage sur internet
    au lieu de vouloir faire mon propre cryptage, mais bon au moins ça me fait coder un peu sachant que par la faute de mr tamby
    je ne fais plus NSI ;'(, si vous lisez ça mr Tamby sachez que je me sens trahit mdrr, bon aller je me tais et au travail. 
    Ps : si quelqu'un lit ça, soyer gentil avec mon code qui ne doit surement pas etre très optimiser mais c'est surtout du 
    au fait que je l'ai finit en étant fatiguer donc bon xD, alors que j'ai un DS de math bien gros demain, bon cette fois j'arrete de parler. """
    indice = 0
    indice2 = 0 #je fais plus d'effort pour le noms des variables 
    l_ou_c = []
    while indice < len(m) : # si ya un probleme sans être une erreur ça peut etre du ici enfin j'espere. 
        var_poubelle = "" #j'ai pas trouvé mieux comme nom mdr 
        for i in range(len(m)):
            if m[i] == ',' and i != len(m)  :
                for a in range(indice2,i):
                    var_poubelle = var_poubelle + m[a]
                l_ou_c.append(var_poubelle)
                var_poubelle = ""
                indice2 = i + 1
        indice = indice + 1
        return l_ou_c 

def decryptage_mdp(n,c):
    """fonction qui soit crypte un mdp soit le décrypte, prends en parametre le mdp à crypter
    ou à decrypter et le choix, c pour crypter ou d pour decrypter"""
    if c == "c" :
        mdp_cryp = ""      
        for i in n :
            if True == i.isnumeric() :
                mdp_cryp = mdp_cryp + str(int(i)*((1+sqrt(5))/2)+1) + ","
            else :
                mdp_cryp = mdp_cryp + numero_alpha(i) + "," #Bon bah j'ai un probleme ici, apparement none type ne pas concatanate avec str, ça doit donc venir de la fonction. 
        return mdp_cryp 
    else : 
        mdp_decryp = ""
        for i in lettre_ou_chiffre_dans_crypt(n) :
            if len(i) == 1 :#donc c'est une lettre qu'est codé car vu que j'avais la flemme 
                #de faire un cryptage pousser pour les lettres, j'ai juste prit leurs numéro dans l'alphabet
                mdp_decryp = mdp_decryp + numero_alpha(i[0])  
            elif len(i) == 2 :
                mdp_decryp = mdp_decryp + numero_alpha(i[0]+i[1])
            else :
                mdp_decryp = mdp_decryp + str(int((float(i)-1)/((1+sqrt(5))/2)))
        return mdp_decryp

def nom_site():
    """renvoie tous les noms des sites dans le gestionnaire de mot de passe"""
    if len(tab_contenu) == 0 :
        return "Il n'y a rien d'enrengristrer. "
    for i in range(len(tab_contenu)):
        print(tab_contenu[i][0])

def mdp_site(n):
    for i in range(len(tab_contenu)):
        if tab_contenu[i][0] == n :
            return decryptage_mdp(tab_contenu[i][1],"d")
    return n + " n'est pas présent !"

def ecrire(): 
    nom = input("quel nom désirez-vous ? : ")
    mdp = decryptage_mdp(input("quel mot de passe ? (il ne doit contenir que des lettres minuscules et chiffre, hors ! et M qui sont accepté"),'c')
    files = open("C:\\Users\\Mohammed\\Desktop\\test2.csv","a",encoding="utf-8")#le a permet de mettre en mode rajout
    ligne = nom + ";" + mdp + '\n' 
    contenu2 = files.write(ligne)
    files.close()

#Ok parfait probleme corrigé. 
#Bah super j'ai fait quasi tous ce qui était important, reste plus qu'une ou deux fonctions à faire. 

def gestionnaire_mdp():
    """Nous voilà à la fin, bon la fonction s'occupe de faire ce dont tout l'ensemble du code a été écrit, ainsi 
    faire un gestionnaire de mdp avec en choix rajouter un mdp avec un nom ou récupérer le mdp avec une clé maitre"""
    test = input("Entrez le mots de passe maître : ") #Faut bien vérifier si l'utilisateur a le droit d'accès. 
    if test != decryptage_mdp(master_key,'') :
        return print("NON NON NON C'EST LE MAUVAIS LE MOT DE PASSE, J'espere que tu n'es pas un vilain hackeur car sinon tu ne passera pas")
    test_1 = input("Que veux tu faire ? (lire pour lire tous les noms, ecrire pour rajouter un mdp et mdp pour avoir accès à un mdp) : ")
    if test_1 == 'lire' : 
        return print(nom_site())
    elif test_1 == 'mdp' : 
        return print(mdp_site(input("le nom du mot de passe : ")))
    elif test_1 == 'ecrire' :
        ecrire()
        return print("c'est bon c'est fait")
    else :
        return print("Soit vous ne savez pas écrire, soit vous essayer de tester mon code, peu import arrêter s'il vous plaît !!!!!")

#J'ai finis super
# 
# Conclusion : c'était cool ça m'a prit au total 1jours, dont un peu moins de 4h, j'ai eu des être un peu inventif et c'était cool
# sachant qu'en plus le programme en soit n'est pas vraiment complexe mais vu que j'ai fait mon propre cryptage bah c'était encore
# plus cool qu'en utiliser un déjà fait meme si il n'est pas vraiment fou fou le mien.
# J'ai découvert Visual Studio Code est vraiment, heureusement que je l'ai trouvé j'adore c'est trop bien et super utile pour coder. 
# Je pense pas que le code soit parfait il doit surement avoir plein d'amélioratation à faire mais il marche donc voilà ça suffit mdr, 
# Si j'ai le temps, j'essaierais de l'ameliorer pour que ça soit plus optimiser et autres, j'y rajouterais surement quelques
# fonctionnalités. 

gestionnaire_mdp()