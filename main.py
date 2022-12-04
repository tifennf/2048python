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
    Pre: len(cases) != 0
    Procédure insérant un nombre"""

    i: int = int(random.random()*4)
    j: int = int(random.random()*4)

    while not ((i,j) in empty_cases) :
        i = int(random.random()*4)
        j = int(random.random()*4)

    pla[i][j] = n

def is_case_possible(i: int, j:int) -> bool:
    """Vérifie si la case est valide"""
    return 0<= i < 3 and 0<= j < 3

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

plateau2048: Plateau2048 = init_2048()

print(draw_2048(plateau2048))

