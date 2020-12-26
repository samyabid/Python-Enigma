import time
from random import randint
alphabet = "abcdefghijklmnopqrstuvwxyz"

def dictionnaire_chiffres_lettres():
	dico = {}

	for i in range (1,27):
		dico[i] = alphabet [i-1]
		dico[alphabet[i-1]] = i
	return dico
dictionnaire_chiffres_lettres_variable = dictionnaire_chiffres_lettres()

def chaine_vers_liste (chaine):
	liste = []
	for i in chaine:
		liste += [i]
	return liste

def liste_vers_chaine (liste):
	chaine = ""
	for i in liste:
		chaine += i
	return chaine
def modulo26 (N):
	while N < 1:
		N += 26
	while N > 26:
		N -= 26
	return N

def addition_des_lettres (A,B): # maj = lettre, min = chiffre
	a = dictionnaire_chiffres_lettres_variable [A]
	b = dictionnaire_chiffres_lettres_variable [B]
	c = a+b
	c = modulo26 (c)
	C = dictionnaire_chiffres_lettres_variable [c]
	return C

def soustraction_des_lettres (A,B):
	a = dictionnaire_chiffres_lettres_variable [A]
	b = dictionnaire_chiffres_lettres_variable [B]
	c = a-b
	c = modulo26 (c)
	C = dictionnaire_chiffres_lettres_variable [c]
	return C

def chisir_aleatoirement_dans_une_liste (L): # return un indice
	if len(L) == 0:
		return "erreur"
	if len(L) == 1:
		return 0
	else:
		return randint(0,len(L)-1)

def actualisation_des_reglages (RR1,RR2,RR3):
	if RR1 != "z":
		RR1 = addition_des_lettres (RR1,"a")
	else:
		RR1 = "a"
		if RR2 != "z":
			RR2 = addition_des_lettres (RR2,"a")
		else:
			RR2 = "a"
			if RR3 != "z":
				RR3 = addition_des_lettres (RR3,"a")
			else:
				RR3 = "a"
	return RR1,RR2,RR3

def tout_stocker_dans_un_fichier(message,message_code,cycles_trouves,liste_des_combinaisons):
    t = time.time()
    t_ = str(t)
    t_ = "Donnees/"+ t_[:10]
    num = ""
    for i in range (0,len(message)):
        num += str(i)[-1]
    fichier = open(t_,"w")
    fichier.write(num)
    fichier.write ("\n")
    fichier.write(liste_vers_chaine(message))
    fichier.write ("\n")
    fichier.write(liste_vers_chaine(message_code))
    fichier.write ("\n")
    fichier.write(str(cycles_trouves))
    fichier.write ("\n")
    fichier.write("Liste des combinaisons")
    fichier.write("\n")
    for i in (liste_des_combinaisons):
        fichier.write(str(i))
        fichier.write ("\n")

    fichier.close()

def afficher_message_recu_intercepte(message_recu,message_intercepte):
	L1 = ""
	L2 = ""
	L3 = ""
	for i in range (0,max(len(message_recu),len(message_intercepte))):
		i_ = str(i)
		if len(i_) == 1:
			i_ = "  " + i_
		if len(i_) == 2:
			i_ = " " + i_
		if len(i_) == 3:
			i_ = i_
		L1 += i_
		L2 += "  " + message_recu[i]
		L3 += "  " + message_intercepte[i]

	print (L1)
	print (L2)
	print (L3)

def intersection_de_listes (L1,L2):
	listebis = []
	for i in L1:
		if i in L2:
			listebis += [i]
	return listebis


























