import class_rotors as r
import class_fonctions as f
import class_enigma as e
import class_bombe as b

""" CONFIGURATION"""
c = r.rotor()
configuration = c.nouveau_processus_rotors()
# c.afficher_parametres()

"""REGLAGE"""
RR1 = "y" # lettre en face de la bague
RR2 = "t"
RR3 = "a"
TC = c.nouveau_processus_tableau ()
reglage = RR1,RR2,RR3,TC
c.afficher_parametres()

""" MESSAGE"""
message = "hdjkabdkjdjkzehdhdjskhazertyuiopqsdfghjklwxcvbndkjhdkjhdjkhdkjhzefhzefhezhfkjhfzkjehfkjkjezhjdhkjzehdkjhdfkjhezkdhzjkfhezhfjkzhfdkjze"
MESSAGE = f.chaine_vers_liste(message) # transforme le message chaine en liste

""" CODAGE DU MESSAGE """
machine1 = e.enigma(configuration,reglage,MESSAGE)
machine1.coder_MESSAGE()
MESSAGE_ = machine1.MESSAGE_ # liste
message_ = f.liste_vers_chaine (MESSAGE_) # chaine


print ("affichage des messages recu et interceptes")
f.afficher_message_recu_intercepte(message,message_)

""" codage dune lettre _ exemple tipe """
# machine2 = e.enigma(configuration,reglage,MESSAGE)
# machine2.coder_une_lettre_exemple("a")z = b.identifier_reglage (cycle4[i][0],cycle4[i][1],cycle4[i][2],cycle4[i][3],configuration)

""" DECODAGE RECEPTEUR """
# machine2 = e.enigma(configuration,reglage,MESSAGE_)
# machine2.coder_MESSAGE()
# MESSAGE__ = machine2.MESSAGE_ # liste
# message__ = f.liste_vers_chaine (MESSAGE__) # chaine
# print (message__)

""" DECODAGE INTERCEPTEUR """
# suppose = ["a","a","b","s","c","c"]
# intercepte = ["z","b","c","c","a","e"]
suppose = MESSAGE
intercepte = MESSAGE_

d = b.identifier_cycles_4(suppose,intercepte)
cycle4 = d.processus() [:-1]
print ("cycle4",cycle4)

z = b.identifier_reglage (cycle4[0][0],cycle4[0][1],cycle4[0][2],cycle4[0][3],configuration)
z.regler_les_machines()
z.afficher_tout_les_reglages()
z.processus()

resultat = z.reglages_convenables

for i in range (1,30):
	z = b.identifier_reglage (cycle4[i][0],cycle4[i][1],cycle4[i][2],cycle4[i][3],configuration)
	z.regler_les_machines()
	z.afficher_tout_les_reglages()
	z.processus()

	resultat = f.intersection_de_listes (resultat,z.reglages_convenables)

print ("\nresultat : ",resultat,"\nnombre de combinaisons trouvees : ",len(resultat))

# f.tout_stocker_dans_un_fichier(suppose,intercepte,cycle,d.reglages_convenables)
