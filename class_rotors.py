import class_fonctions as f
from random import randint

class rotor:
	def __init__(self):
		self.alphabet = ["a","z","e","r","t","y","u","i","o","p","q","s","d","f","g","h","j","k","l","m","w","x","c","v","b","n"]
		self.R1 = {}
		self.R1_ = {}
		self.R2 = {}
		self.R2_ = {}
		self.R3 = {}
		self.R3_ = {}
		self.REF = {}
		self.TC = {}

	def creer_rotor(self):
		rotor = {}
		rotor_ = {}
		alphabet_1 = self.alphabet [:]
		alphabet_2 = self.alphabet [:]
		while alphabet_1 != []:
			if len(alphabet_1) == 1 and alphabet_1 == alphabet_2:
				return self.creer_rotor()
			l1 = "a"
			l2 = "a"
			while l1 == l2:
				r1 = f.chisir_aleatoirement_dans_une_liste (alphabet_1)
				l1 = alphabet_1[r1]
				r2 = f.chisir_aleatoirement_dans_une_liste (alphabet_2)
				l2 = alphabet_2[r2]
			del alphabet_2[r2]
			del alphabet_1[r1]
			rotor[l1] = l2
			rotor_[l2] = l1
		return rotor,rotor_

	def creer_reflecteur (self):
		ref = {}
		alphabet_ = self.alphabet [:]
		while alphabet_ != []:
			r1 = f.chisir_aleatoirement_dans_une_liste (alphabet_)
			l1 = alphabet_[r1]
			del alphabet_[r1]
			r2 = f.chisir_aleatoirement_dans_une_liste (alphabet_)
			l2 = alphabet_[r2]
			del alphabet_[r2]
			ref[l1] = l2
			ref [l2] = l1
		return ref

	def creer_tableau (self): # creation du tableau des connexions (dictionnaire)
		alphabet_ = self.alphabet [:]
		TC = {}
		while len(TC)<20:
			r1 = f.chisir_aleatoirement_dans_une_liste (alphabet_)
			l1 = alphabet_[r1]
			del alphabet_[r1]
			r2 = f.chisir_aleatoirement_dans_une_liste (alphabet_)
			l2 = alphabet_[r2]
			del alphabet_[r2]
			TC[l1] = l2
			TC[l2] = l1
		while alphabet_ != []:
			TC[alphabet_[0]] = alphabet_[0]
			del alphabet_[0]	
		return TC


	def nouveau_processus_rotors(self):
		self.R1,self.R1_ = self.creer_rotor()
		self.R2,self.R2_ = self.creer_rotor()
		self.R3,self.R3_ = self.creer_rotor()
		self.REF = self.creer_reflecteur()
		return self.R1,self.R1_,self.R2,self.R2_,self.R3,self.R3_,self.REF

	def nouveau_processus_tableau (self):
		self.TC = self.creer_tableau()
		return self.TC

	def afficher_parametres(self):
		print ("R1 :")
		print (self.R1)
		print ()
		print ("R2 :")
		print (self.R2)
		print ()
		print ("R3 :")
		print (self.R3)
		print ()
		print ("REF :")
		print (self.REF)
		print ()
		print ("TC :")
		print (self.TC)
		print ()

def passage_rotor (rotor,reglage_rotor,lettre):
	lettre = f.addition_des_lettres (lettre,reglage_rotor)
	lettre = rotor[lettre]
	lettre = f.soustraction_des_lettres (lettre,reglage_rotor)
	return lettre





