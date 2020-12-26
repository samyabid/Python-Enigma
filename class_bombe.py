# ici on connait la configuration, on cherche le reglage

import class_enigma0 as e0 # note: on n'a acces qu'a enigma0 qui ne connait rien appart la configuration des rotors
import class_fonctions as f

class identifier_cycles_4:
	def __init__(self,MESSAGE,MESSAGE_): # MESSAGE et MESSAGE_ doivent correspondre
		self.MESSAGE = MESSAGE # message suppose
		self.MESSAGE_ = MESSAGE_ # message recu
		self.arbre_des_cycles_0 = []
		self.arbre_des_cycles_1 = []
		self.arbre_des_cycles_2 = []
		self.arbre_des_cycles_3 = []
		self.arbre_des_cycles_4 = []
		self.arbre_des_cycles_final = []

	def generation_de_l_arbre_des_cycles(self):
		for i in range (0,len(self.MESSAGE)):
			self.arbre_des_cycles_0 += [i]

	def premier_passage(self):
		for i in range (0,len(self.arbre_des_cycles_0)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_0[i]] == self.MESSAGE[j]:
					self.arbre_des_cycles_1 += [[self.arbre_des_cycles_0[i],j]]

	def deuxieme_passage(self):
		for i in range (0,len(self.arbre_des_cycles_1)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_1[i][1]] == self.MESSAGE[j]:
					self.arbre_des_cycles_2 += [self.arbre_des_cycles_1[i]+[j]]

	def troisieme_passage(self):
		for i in range (0,len(self.arbre_des_cycles_2)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_2[i][2]] == self.MESSAGE[j]:
					self.arbre_des_cycles_3 += [self.arbre_des_cycles_2[i]+[j]]

	def quatrieme_passage(self):
		for i in range (0,len(self.arbre_des_cycles_3)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_3[i][3]] == self.MESSAGE[j]:
					self.arbre_des_cycles_4 += [self.arbre_des_cycles_3[i]+[j]]

	def selection_des_cycles(self):
		for i in self.arbre_des_cycles_4:
			if i[0] == i[-1]:
				self.arbre_des_cycles_final += [i]

	def processus(self): # return un cycle sous forme de liste
		self.generation_de_l_arbre_des_cycles()
		self.premier_passage()
		self.deuxieme_passage()
		self.troisieme_passage()
		self.quatrieme_passage()
		self.selection_des_cycles()
		if self.arbre_des_cycles_final != []:
			return self.arbre_des_cycles_final
		else:
			return "il n'y a pas de cycles"

class identifier_cycles_3:
	def __init__(self,MESSAGE,MESSAGE_): # MESSAGE et MESSAGE_ doivent correspondre
		self.MESSAGE = MESSAGE # message suppose
		self.MESSAGE_ = MESSAGE_ # message recu
		self.arbre_des_cycles_0 = []
		self.arbre_des_cycles_1 = []
		self.arbre_des_cycles_2 = []
		self.arbre_des_cycles_3 = []
		self.arbre_des_cycles_final = []

	def generation_de_l_arbre_des_cycles(self):
		for i in range (0,len(self.MESSAGE)):
			self.arbre_des_cycles_0 += [i]

	def premier_passage(self):
		for i in range (0,len(self.arbre_des_cycles_0)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_0[i]] == self.MESSAGE[j]:
					self.arbre_des_cycles_1 += [[self.arbre_des_cycles_0[i],j]]

	def deuxieme_passage(self):
		for i in range (0,len(self.arbre_des_cycles_1)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_1[i][1]] == self.MESSAGE[j]:
					self.arbre_des_cycles_2 += [self.arbre_des_cycles_1[i]+[j]]

	def troisieme_passage(self):
		for i in range (0,len(self.arbre_des_cycles_2)):
			for j in range (0,len(self.MESSAGE)):
				if self.MESSAGE_[self.arbre_des_cycles_2[i][2]] == self.MESSAGE[j]:
					self.arbre_des_cycles_3 += [self.arbre_des_cycles_2[i]+[j]]

	def selection_des_cycles(self):
		for i in self.arbre_des_cycles_3:
			if i[0] == i[-1]:
				self.arbre_des_cycles_final += [i]

	def processus(self): # return un cycle sous forme de liste
		self.generation_de_l_arbre_des_cycles()
		self.premier_passage()
		self.deuxieme_passage()
		self.troisieme_passage()
		self.selection_des_cycles()
		if self.arbre_des_cycles_final != []:
			return self.arbre_des_cycles_final
		else:
			return "il n'y a pas de cycles "

class identifier_reglage: # ici on veut trouver le reglage en ayant identifie un cycle
	def __init__(self,D1,D2,D3,D4,configuration): # D1,D2 et D3 sont les decalage de reglage entre les machines
		self.RR1 = "a" # reglage initiale de la machine
		self.RR2 = "a"
		self.RR3 = "a"

		self.RM1_R1 = "a" # reglage de la premiere machine
		self.RM1_R2 = "a"
		self.RM1_R3 = "a"

		self.RM2_R1 = "a" # reglage de la deuxieme machine
		self.RM2_R2 = "a"
		self.RM2_R3 = "a"

		self.RM3_R1 = "a" # reglage de la troisieme machine
		self.RM3_R2 = "a"
		self.RM3_R3 = "a"

		self.RM4_R1 = "a" # reglage de la quatrieme machine
		self.RM4_R2 = "a"
		self.RM4_R3 = "a"

		self.D1 = D1 # positions du cycle
		self.D2 = D2
		self.D3 = D3
		self.D4 = D4
		self.configuration = configuration
		self.reglages_convenables = []

# class epurer_liste_des_cycles3:
# 	def __init__(self,liste_des_cycles):
# 		self.nouvelle_liste_des_cycles = []
# 		self.liste_des_cycles = liste_des_cycles

# 	def cycle_present_dans_nouvelle_liste (self,cycle):
# 		for i in self.nouvelle_liste_des_cycles:
# 			for j in range (0,3):
# 				if i[j] != cycle[j]


	def regler_les_machines(self): # on regle les machines avec le bon decalage
		for i in range (0,self.D1):
			self.RM1_R1,self.RM1_R2,self.RM1_R3 = f.actualisation_des_reglages(self.RM1_R1,self.RM1_R2,self.RM1_R3)

		for i in range (0,self.D2):
			self.RM2_R1,self.RM2_R2,self.RM2_R3 = f.actualisation_des_reglages(self.RM2_R1,self.RM2_R2,self.RM2_R3)

		for i in range (0,self.D3):
			self.RM3_R1,self.RM3_R2,self.RM3_R3 = f.actualisation_des_reglages(self.RM3_R1,self.RM3_R2,self.RM3_R3)

		for i in range (0,self.D4):
			self.RM4_R1,self.RM4_R2,self.RM4_R3 = f.actualisation_des_reglages(self.RM4_R1,self.RM4_R2,self.RM4_R3)

	def actualisation_de_tout_les_reglages(self): # ici on agmente le reglage de tout le monde de une lettre
		self.RR1,self.RR2,self.RR3 = f.actualisation_des_reglages(self.RR1,self.RR2,self.RR3)
		self.RM1_R1,self.RM1_R2,self.RM1_R3 = f.actualisation_des_reglages(self.RM1_R1,self.RM1_R2,self.RM1_R3)
		self.RM2_R1,self.RM2_R2,self.RM2_R3 = f.actualisation_des_reglages(self.RM2_R1,self.RM2_R2,self.RM2_R3)
		self.RM3_R1,self.RM3_R2,self.RM3_R3 = f.actualisation_des_reglages(self.RM3_R1,self.RM3_R2,self.RM3_R3)
		self.RM4_R1,self.RM4_R2,self.RM4_R3 = f.actualisation_des_reglages(self.RM4_R1,self.RM4_R2,self.RM4_R3)

	def afficher_tout_les_reglages(self):
		print("reglages suppose de la machine :")
		print (self.RR1,self.RR2,self.RR3)
		print ("reglage machine 1 :")
		print (self.RM1_R1,self.RM1_R2,self.RM1_R3)
		print ("reglage machine 2 :")
		print (self.RM2_R1,self.RM2_R2,self.RM2_R3)
		print ("reglage machine 3")
		print (self.RM3_R1,self.RM3_R2,self.RM3_R3)
		print ("reglage machine 4")
		print (self.RM4_R1,self.RM4_R2,self.RM4_R3)

	def boucler_une_lettre (self,LETTRE):
		aa = LETTRE

		M1 = e0.enigma0(self.configuration,(self.RM1_R1,self.RM1_R2,self.RM1_R3),LETTRE)
		M1.coder_MESSAGE()
		a = LETTRE = M1.MESSAGE_

		M2 = e0.enigma0(self.configuration,(self.RM2_R1,self.RM2_R2,self.RM2_R3),LETTRE)
		M2.coder_MESSAGE()
		b =LETTRE = M2.MESSAGE_

		M3 = e0.enigma0(self.configuration,(self.RM3_R1,self.RM3_R2,self.RM3_R3),LETTRE)
		M3.coder_MESSAGE()
		c = LETTRE = M3.MESSAGE_

		M4 = e0.enigma0(self.configuration,(self.RM4_R1,self.RM4_R2,self.RM4_R3),LETTRE)
		M4.coder_MESSAGE()
		d = LETTRE = M4.MESSAGE_

		# print (aa,a,b,c,d)

		return LETTRE

	def tester_lettre(self,LETTRE): # la lettre est sous forme d'une liste ici
		LETTRE_bis = self.boucler_une_lettre(LETTRE)
		if LETTRE == LETTRE_bis:
			return True
		else:
			return False

	def tester_alphabet(self): # ici, pour un reglage donne on teste toutes les lettres de l'alphabet
		for i in "azertyuiopqsdfghjklmwxcvbn":
			if self.tester_lettre([i]) == True:
				self.reglages_convenables += [[self.RR1,self.RR2,self.RR3]]
				return
		return

	def processus(self):
		a = self.RR3
		for i in range (0,26*26):
			if self.RR3 != a:
				print (a)
				a = self.RR3
			self.tester_alphabet()
			self.actualisation_de_tout_les_reglages()



































