from libs.bottle import *
import mysql.connector
import interactionBD

##################
#    ROUTING     #
##################
@route('/static/<filepath:path>')
def file_stac(filepath):
  return static_file(filepath,root="./static")

@route('/')
@view('index.tpl')
def index():
  context = template('index')
  return (context)

@route('/search',method='POST')
@view('result.tpl')
def search():
	#On recupere le champ ville
	ville = request.forms.get('ville')

  	#On recupere le champ sport
	sport = request.forms.get('sport')

	#Si les deux champs sont renseignes
	if sport != '' and ville != '':
		print('2 champs renseignes')
		requeteFinale = ''.join(["select distinct i.nom, i.adresse FROM Installation i, Activite a, Equipement e, Equipement_Activite ea WHERE a.numero=ea.numero_activite And ea.numero_equipement=e.numero And e.numero_installation=i.numero And i.ville = '",str(ville),"' And a.nom='",str(sport),"'"]) 
		print(requeteFinale)
		result = interactionBD.getRequete(requeteFinale)
		print(result)

	#Sinon si ville renseigne	
	elif ville != '':
		print('ville renseignes')
		requeteFinale = ''.join(["select distinct a.nom from Activite a, Installation i, Equipement e, Equipement_Activite ea WHERE a.numero=ea.numero_activite AND ea.numero_equipement=e.numero AND e.numero_installation=i.numero AND i.ville='",str(ville),"'"])
		print(requeteFinale)
		result = interactionBD.getRequete(requeteFinale)

	#Sinon si sport renseigne	
	elif sport != '':
		print('sport renseignes')
		requeteFinale = ''.join(["select distinct i.ville from Installation i, Equipement e, Equipement_Activite ea, Activite a WHERE i.numero=e.numero_installation and e.numero=ea.numero_equipement and ea.numero_activite=a.numero and a.nom='",str(sport),"'"])
		print(requeteFinale)
		result = interactionBD.getRequete(requeteFinale)

	context = template('result',rows=result,ville=ville,sport=sport)
	return (context)

run(host='localhost', port=8080, reloader=True)