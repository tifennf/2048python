from typing import *
import random

Plateau2048 = List[List[int]]
EmptyCases = Set[Tuple[int,int]]

def is_empty(pla: Plateau2048, i:int, j:int) -> bool:
    """Vérifie si la case est vide"""
    return pla[i][j] == 0

def get_empty_cases(pla: Plateau2048) -> EmptyCases:
    """Renvoi l'ensemble des cases vides du plateau"""
    return {(i,j) for i in range(4) for j in range(4) if is_empty(pla,i,j)}

def insert_number(pla: Plateau2048, empty_cases: EmptyCases, n:int) -> None:
    """
    Pre: len(empty_cases) != 0
    Procédure insérant un nombre"""

    i: int = int(random.random()*4)
    j: int = int(random.random()*4)

    while not ((i,j) in empty_cases) :
        i = int(random.random()*4)
        j = int(random.random()*4)

    pla[i][j] = n

def is_inboard(i: int, j:int) -> bool:
    """Vérifie si la case est valide"""
    return 0<= i <= 3 and 0<= j <= 3

def init_2048() -> Plateau2048:
    """Créer un plateau vide pour le jeu 2048"""
    pla: Plateau2048 = [ [0 for _ in range(4)] for _ in range(4)]

    empty_cases: EmptyCases = get_empty_cases(pla)

    ### marche forcément
    insert_number(pla, empty_cases,2)
    insert_number(pla, empty_cases,4)

    return pla

def draw_2048(pla: Plateau2048) -> str:
    """Renvoi une string contenant le plateau"""

    sep: str = "-----------------"
    draw: str = sep + "\n"
    
    i:int
    for i in range(4):
        for j in range(4):
            draw = draw + "|"
            if pla[i][j] == 0:
                draw = draw + "   "
            else:
                draw = draw + " " + str(pla[i][j])+ " "
        if i == 3:
            draw = draw +"|\n" + sep
        else:
            draw = draw +"|\n" + sep + "\n"
            

    return draw


def translate_haut(pla: Plateau2048) -> None:
    """Translate le nombre d'une case vers le haut"""
    i: int
    for i in range(4):
        j:int
        for j in range(4):
            x: int = i-1
            y: int = j
            if is_inboard(x,y):
                if is_empty(pla,x,y):
                    pla[x][y] = pla[i][j]
                    pla[i][j] = 0
                elif pla[x][y] == pla[i][j]:
                    pla[x][y] = pla[x][y] * pla[i][j]
                    
def translate_gauche(pla: Plateau2048) -> None:
    """Translate le nombre d'une case vers la gauche"""
    i: int
    for i in range(4):
        j:int
        for j in range(4):
            x: int = i - 1
            y: int = j
            if is_inboard(y,x):
                if is_empty(pla,y,x):
                    pla[y][x] = pla[j][i]
                    pla[j][i] = 0
                elif pla[y][x] == pla[y][x]:
                    pla[y][x] = pla[y][x] * pla[j][i]
                    
def translate_bas(pla: Plateau2048) -> None:
    """Translate le nombre d'une case vers le bas"""
    n: int = 3
    i: int
    for i in range(n+1):
        j:int
        for j in range(n+1):
            x: int = n-i+1
            y: int = n-j
            if is_inboard(x,y):
                if is_empty(pla,x,y):
                    pla[x][y] = pla[n-i][n-j]
                    pla[n-i][n-j] = 0
                elif pla[x][y] == pla[n-i][n-j]:
                    pla[x][y] = pla[x][y] * pla[n-i][n-j]

def translate_droite(pla: Plateau2048) -> None:
    """Translate le nombre d'une case vers la droite"""
    n: int = 3
    i: int
    for i in range(n+1):
        j:int
        for j in range(n+1):
            x: int = n-i+1
            y: int = n-j
            if is_inboard(y,x):
                if is_empty(pla,y,x):
                    pla[y][x] = pla[n-j][n-i]
                    pla[n-j][n-i] = 0
                elif pla[y][x] == pla[n-j][n-i]:
                    pla[y][x] = pla[y][x] * pla[n-j][n-i]


def is_over(pla: Plateau2048, empty: EmptyCases) -> bool:
    """Vérifie si la partie est terminée"""

    if len(empty) != 0:
        return False

    

def push(pla: Plateau2048, sens: str) -> None:
    """
    Pre: len(sens) == 1 and sens in {'h','b','g','d'}
    Procédure qui pousse tout le plateau dans un sens"""
    if sens == "h":
        translate_haut(pla)
        translate_haut(pla)
        translate_haut(pla)

        empty: EmptyCases = get_empty_cases(pla)
        if len(empty!= 0):
            insert_number(pla,empty,2)
            insert_number(pla,empty,4)
    elif sens == "g":
        translate_gauche(pla)
        translate_gauche(pla)
        translate_gauche(pla)
    elif sens == "b":
        translate_bas(pla)
        translate_bas(pla)
        translate_bas(pla)
    elif sens == "d":
        translate_droite(pla)
        translate_droite(pla)
        translate_droite(pla)






plateau2048: Plateau2048 = init_2048()

print(draw_2048(plateau2048))

translate_droite(plateau2048)

print(draw_2048(plateau2048))


