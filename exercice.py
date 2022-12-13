#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import turtle


# TODO: Définissez vos fonction ici
def masse_et_volume_ellipsoide (a,b,c,mv) -> tuple:
    V = (4/3)*(math.pi)*(a*b*c)
    m = mv*V
    return (V,m)

def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    dict_lettres = dict()
    dict_sorted = dict()
    for lettre in sentence:
        if lettre.isalpha():
            nb_occurences = sentence.count(lettre)
            dict_lettres[lettre] = nb_occurences                
    list_sorted = sorted(dict_lettres.items(),key=lambda x:x[1], reverse=True)
    for i in range(len(list_sorted)):
        dict_sorted[list_sorted[i][0]] = list_sorted[i][1]
    return dict_sorted

def dessine_branches(pen_size, longueur_branches, angle):
    if pen_size > 0 and longueur_branches > 0:
        turtle.pensize(pen_size)
        turtle.forward(longueur_branches)
        turtle.right(angle)
        dessine_branches(pen_size-1, longueur_branches-1, angle-5)
        turtle.left(angle*2)
        dessine_branches(pen_size-1, longueur_branches-1, angle-5)
        turtle.right(angle)
        turtle.backward(longueur_branches)


def dessine_arbre():
    turtle.setheading(90)
    turtle.color("green")
    dessine_branches(5, 50, 35)
    turtle.done()       

def saisie_valide_ADN(string_ADN) -> bool:
    lettres_ADN= ['a', 't', 'g', 'c']
    if len(string_ADN)!=0:
        for i in range(len(string_ADN)):
           if i not in lettres_ADN:
                return False
           else:
                return True

def saisie_valide_renvoie_ADN() -> str:
    condition = True
    while (condition):
        chaine_ADN = input("Veuillez saisir une chaîne d'ADN: ")
        condition = saisie_valide_ADN(chaine_ADN)
    return chaine_ADN

def proportion_ADN(ADN, sequence_ADN) -> float:
    result = round(ADN.count(sequence_ADN)/len(ADN), 2)
    return result

def saisie_ADN():
    str_ADN = saisie_valide_renvoie_ADN()
    sequenceADN = saisie_valide_renvoie_ADN()
    proportion = proportion_ADN(str_ADN,sequenceADN)
    print(f"Il a {proportion} % de {sequenceADN}")

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print(masse_et_volume_ellipsoide(1,2,3,4))
    print(masse_et_volume_ellipsoide(100,5,60,80))
    print((lambda sentence: list(frequence(sentence).keys())[0])("Good Gudetama have gggggggdnight"))
    dessine_arbre()
    saisie_ADN()