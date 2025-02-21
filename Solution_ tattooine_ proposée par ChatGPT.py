# Définition des fonctions

def panne_moteur(course):
    """Le premier concurrent passe à la dernière position."""
    if course:
        course.append(course.pop(0))

def passe_en_tete(course):
    """Le deuxième concurrent prend la tête de la course."""
    if len(course) > 1:
        course[0], course[1] = course[1], course[0]

def sauve_honneur(course):
    """Le dernier concurrent dépasse l'avant-dernier."""
    if len(course) > 1:
        course[-1], course[-2] = course[-2], course[-1]

def tir_blaster(course):
    """Le premier concurrent est éliminé."""
    if course:
        course.pop(0)

def retour_inattendu(course, concurrent):
    """Un concurrent éliminé revient en course à la dernière position."""
    course.append(concurrent)

# Liste des concurrents de départ
course_modules = ["Anakin", "Sebulba", "Ben Quadinaros", "Gasgano", "Ratts Tyerell"]

# Affichage de la situation initiale
print("Départ de la course :", course_modules)

# Exécution des événements
panne_moteur(course_modules)
print("Après une panne moteur :", course_modules)

passe_en_tete(course_modules)
print("Après un dépassement en tête :", course_modules)

sauve_honneur(course_modules)
print("Après un dépassement de dernière minute :", course_modules)

tir_blaster(course_modules)
print("Après un tir de blaster :", course_modules)

retour_inattendu(course_modules, "Anakin")
print("Après un retour inattendu :", course_modules)