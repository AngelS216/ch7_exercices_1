#!/usr/bin/env python
# -*- coding: utf-8 -*-

#From chap 6:
def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres
    frequency = dict()
    for letter in sentence:
        frequency[letter] = sentence.count(letter)

    sorted_keys = sorted(frequency, key=frequency.__getitem__, reverse=True)
    for key in sorted_keys:
        if frequency[key] > 5:
            print(f"Le caractère {key} revient {frequency[key]} fois.")

    return frequency

# TODO: Importez vos modules ici
import math

# TODO: Définissez vos fonction ici
def volume_masse(a,b,c,masse_volumique):
    volume = abs((4/3)*(math.pi)*a*b*c)
    masse = volume* abs(masse_volumique)
    return volume, masse
    '''Quand on retourne plusieurs variables à partir d'une fonction, ces variables sont assemblées dans un tuple, 
    donc pas de besoin de mettre volume et masse dans un tuple'''

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    print("Voici la masse et le volume de l'ellipsoïde:")
    print(volume_masse(-1,-2,-3,-10))
    pass
