import mysql.connector
import csv

def connexion():
	try :
		global cursor,db
		db = mysql.connector.connect(host="infoweb",user="E134918A",password="E134918A",database="E134918A")
		cursor = db.cursor()
	except Exception as e:
		print(e)

def deconnexion():
	try :
		db.close()
	except Exception as e:
		print(e)

def affichageMessage(msg):
	print('-------------------------------------------------')
	print(msg)
	print('-------------------------------------------------')

def remplissageTableInstallation(nomFichier) :
	affichageMessage("remplissageTableInstallation start")

	connexion()

	try :
		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		for row in lecteurCsv:
			if(row[0]!="Nom usuel de l'installation"):
				if(row[1]!=""): 	numero						= row[1]
				else: 				numero						= 'null'
				if(row[0]!=""):		nom 						= "'" + row[0].replace("'","") + "'"
				else: 				nom							= 'null'
				if(row[2]!=""): 	ville						= "'" + row[2].replace("'","") + "'"
				else: 				ville						= 'null'
				if(row[6]!=""):		numVoie						= row[6].replace("'","")
				else:				numVoie						= 'null'
				if(row[7]!=""):		nomVoie						= row[7].replace("'","")
				else:				nomVoie						= 'null'
				if(row[4]!=""):		codePostal					= "'" + row[4].replace("'"," ") + "'"
				else:				codePostal					= 'null'
				if(row[10]!=""):	latitude					= row[10] 
				else:				latitude 					= 'null'
				if(row[9]!=""):		longitude 					= row[9] 
				else:				longitude 					= 'null'

				if(numVoie!='null'): adresse = "'" + numVoie + " "
				else : adresse = "'"
				if(nomVoie!='null'):adresse = adresse + nomVoie + "'"
				else : adresse = 'null'
					
				requete="INSERT INTO `Installation`  VALUES (" + numero + "," + nom + "," + adresse + "," + codePostal + ", " + ville + ", " + latitude + ", " + longitude +")"
				cursor.execute(requete)

		db.commit()
		deconnexion()

	except Exception as e:
		print(e)

	affichageMessage("remplissageTableInstallation fini")



def remplissageTableActivite(nomFichier) :
	affichageMessage("remplissageTableActivite start")

	connexion()

	try :
		liste = []

		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		for row in lecteurCsv:
			if(row[0]!="Code INSEE"):
				if(row[4]!=""): 	numero						= row[4]
				else: 				numero						= 'null'
				if(row[5]!=""):		nom 						= "'" + row[5].replace("'"," ") + "'"
				else: 				nom							= 'null'
				
				if(numero not in liste and numero != 'null'):
					requete="INSERT INTO `Activite`  VALUES (" + numero + "," + nom +")"
					liste.append(numero)
					cursor.execute(requete)

		db.commit()
		deconnexion()
	except Exception as e:
		print(e)

	affichageMessage("remplissageTableActivite fini")




def remplissageTableEquipementActivite(nomFichier) :
	affichageMessage("remplissageTableEquipementActivite start")

	connexion()

	try :
		liste = []

		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		listeCodes = list()

		for row in lecteurCsv:
			if(row[0]!="Code INSEE"):
				if(row[2]!=""): 	numequip	 			= row[2]
				else: 				numequip	 			= 'null'
				if(row[4]!=""): 	numact	 				= row[4]
				else: 				numact					= 'null'

				if(numequip not in liste and numequip != 'null' and numact != 'null'):
					requete="INSERT INTO `Equipement_Activite`  VALUES (" + numequip + "," + numact + ")"
					liste.append(numequip)
					cursor.execute(requete)

		db.commit()
		deconnexion()
	except Exception as e:
		print(e)
	affichageMessage("remplissageTableEquipementActivite fin")





def remplissageTableEquipement(nomFichier) :
	affichageMessage("remplissageTableEquipement start")
	
	connexion()

	try :
		fichier = open(nomFichier,'r')

		lecteurCsv = csv.reader(fichier, delimiter=',', quotechar='"')

		liste = []

		for row in lecteurCsv:
			if(row[0]!="ComInsee"):
				if(row[4]!=""): 	numero	 			= row[4]
				else: 				numero	 			= 'null'
				if(row[5]!=""): 	nom	 				= "'"+row[5].replace("'"," ")+"'"
				else: 				nom	 				= 'null'
				if(row[0]!=""): 	numinst	 			= row[2]
				else: 				numinst		 		= 'null'

				if(numero not in liste and numero != 'null'):
					requete="INSERT INTO `Equipement`  VALUES (" + numero + "," + nom + "," + numinst + ")"
					liste.append(numero)
					cursor.execute(requete)

		db.commit()
		deconnexion()
	except Exception as e:
		print(e)
	affichageMessage("remplissageTableEquipement fini")

def getRequete(requete):
	try:
		connexion()

		cursor.execute(requete)

		data = cursor.fetchall()

		deconnexion()

		return data

	except Exception as e:
		print(e)