def addition (a,b):
    return a+b
def soustraction (a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    if b!=0:
        return a/b
    else:
        return"erreur:division par 0"

def calculatrice():
    print("Bienvenue dans la calculatrice simple!")
    print("Sélectionner une opération:")
    print("1.Addition")
    print("2.soustraction")
    print("3.multiplication")
    print("4.division")

    choix= input("Entrer votre choix(1/2/3/4):")

    if choix in ['1','2','3','4']:
        try:
            nombre1 =float(input("Entrer le premier nombre: "))
            nombre2 = float(input("Entrer le deuxiéme nombre: "))
        except ValueError:
            print("Erreur: veiller entrer un nombre valides.")
            return
        if choix =='1':
            print(f"Resultat :{nombre1} +{nombre2}={addition(nombre1,nombre2)}")
        elif choix =='2':
            print(f"Resultat:{nombre1}-{nombre2}={soustraction(nombre1,nombre2)}")
        elif choix =='3':
            print(f"Resultat:{nombre1}*{nombre2}={multiplication(nombre1,nombre2)}")
        elif choix =='4':
            print(f"Resultat:{nombre1}/{nombre2}={division(nombre1,nombre2)}")
    else:
        print("Erreur:choix invalide.Veuller réessayer")
        


