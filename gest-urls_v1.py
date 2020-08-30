#---------------------------------gest-urls_v1.py----------------------------------
# -*- coding:Utf8 -*-

###############################################################################
# Programme Python type                                                       #
# auteur : Daniel Bovay, Le Mont sur Lausanne, 2020-08-24                     #
# licence : GPL                                                               #
# Projet : GEST-URLs                                                          #
# Version Python: 3.8.2                                                       #
# Version du programme: 1.05                                                  #
#                                                                             #
###############################################################################

# remarques:
# création d'une version fonctionnelle basic pour la saisie
# de l'URL, de TAGS, d'une DESCRIPTION
# les NO_ID, DATE_DE_SAISIE, STATUS seront intégrés ultérieurement
#
# a voir comment gérer les TAGS

###############################################################################
# Importation de fonctions externes :
import datetime
import os
import sys

###############################################################################
# Définition de fonctions locales :

def saisie_record():
    url = str(input("Url / min 7 car. max 2000 car: "))
    valide_url(url)
    tags = str(input("TAGS séparé par virgule / min 3 car. max 150 car.: "))
    valide_tags(tags)
    description = str(input("Description / min 10 car. max 2500 car.: "))
    return url, tags, description

def valide_url(my_url):
    if len(my_url) <= 6:
        print("URL is too short")
    elif len(my_url) > 12: #valeur pour test, pour prod remplacer par 2000
        print("URL is too long")
    else:
        print("URL is is ok")
        pass
    
def valide_tags(my_tag):
    if len(my_tag) <= 3:
        print("TAG is to shoort")
    elif len(my_tag) > 12:  #valeur pour test, pour prod remplacer par 150
        print("TAG is to long")
    else:
        print("TAG is ok")
        pass

def valide_description(my_description):
    if len(my_description) < 10
        print("DESCRIPTION IS TOO SHORT")
    elif len(my_description) > 12  #valeur pour test, pour prod remplacer par 2000
        print("DESCRIPTION is too long")
    else:
        print("DESCRIPTION is ok")
        pass
    





###############################################################################
# Corps principal :

now = datetime.datetime.now()
nom_pgm = "GEST-URLs"
version_pgm = "1.0.5"
#------------------DEBUT
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
print("Début du programme : ", nom_pgm, "  ", version_pgm)
#---ajouter date et heure
#---src: http://apcpedagogie.com/les-date-et-lheure-actuelles-en-python/
print ("La date courante est : ", now.strftime("%d.%m.%Y %H:%M:%S "))
print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

# main

aa = saisie_record()

print(aa)