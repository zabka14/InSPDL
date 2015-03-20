<!DOCTYPE html>
<html>
	<head>
		<title>Sport / Ville - Pays de la Loire</title>
		<!-- <meta name="viewport" content="width=device-width, initial-scale=1.0"> -->
		<!-- Bootstrap -->
		<meta http-equiv="content-type" content="text/html; charset=utf-8" />
		<script src="http://code.jquery.com/jquery.js"></script>
		<script src="/static/bootstrap/js/bootstrap.min.js"></script>
		<link href="/static/bootstrap/css/bootstrap.min.css" rel="stylesheet">
		<link href="/static/perso.css" rel="stylesheet">
		<script src="/static/perso.js"></script>

	</head>
	<body style="padding-top:70px">

		<nav class="navbar navbar-inverse navbar-fixed-top">
	      <div class="container">
	        <div class="navbar-header">
	          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
	            <span class="sr-only">Navigation</span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	            <span class="icon-bar"></span>
	          </button>
	          <a class="navbar-brand" href="/">Sport / Ville - PDL</a>
	        </div>
	        <div id="navbar" class="navbar-collapse collapse">
	          <ul class="nav navbar-nav">
	            <li class="active"><a href="/">Chercher</a></li>
	            <li><a href="#">Resultat</a></li>
	            <li><a href="/map">Carte</a></li>
	            <li><a data-toggle="modal" data-target="#myModal">A propos</a></li>
	          </ul>
	        </div><!--/.nav-collapse -->
	      </div>
	    </nav>

	    <div class="container">
			<h1>Cherche un sport et une ville</h1>
			</br>


			<!-- Formulaire de recherche -->
			<form class="form-horizontal" action='/search' method='POST'>
				<div class="row">
					<!-- Main -->
					<div class="col-md-6">
						<div class="form-group">
							<label for="ville" class="col-sm-1 control-label">Ville</label>
							<div class="col-sm-6">
								<input type="text" class="form-control" id="ville" placeholder="Ville" name="ville">
							</div>
						</div>
						<div class="form-group">
							<label for="sport" class="col-sm-1 control-label">Sport</label>
							<div class="col-sm-6">
							    <input type="text" class="form-control" id="sport" placeholder="Sport" name="sport">
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-offset-1 col-sm-6">
								<button type="submit" class="btn btn-primary">Chercher</button>
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-offset-1 col-sm-6">
								<input type="checkbox" id="chkBox"> Afficher les options avancées
							</div>
						</div>
					</div>
					<!-- Options avancées -->
					<div class="col-md-6" id="optAvc">
						<div class="form-group">
							<!-- En relation avec la table Instalation -->
							<div class="col-sm-offset-1 col-sm-10">
								<input type="checkbox"> Accessibilité handicapés sensoriels
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-offset-1 col-sm-10">
								<input type="checkbox"> Accessibilité handicapés à mobilité réduite
							</div>
						</div>
						<!-- En relation avec la table Equipement -->
						<div class="form-group">
							<div class="col-sm-offset-1 col-sm-10">
								<input type="checkbox"> Salle polyvalente
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-offset-1 col-sm-10">
								<input type="checkbox"> Présence d'un éclairage
							</div>
						</div>
						<div class="form-group">
							<div class="col-sm-offset-1 col-sm-10">
								<input type="checkbox"> Etablissement sportif couvert
							</div>
						</div>
					</div>
				</div>	
			</form>	
		</div>
















		<!-- About modal content -->
		<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		  <div class="modal-dialog">
		    <div class="modal-content">
		      <div class="modal-header">
		        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
		        <h4 class="modal-title" id="myModalLabel">A propos du projet</h4>
		      </div>
		      <div class="modal-body">
		        Ce projet a été réalisé par 
		        <a href="https://github.com/ErwannNevou" target="_blank">Erwann Nevou</a>, 
		        Pierre Lefrancois et 
		        <a href="https://github.com/zabka14" target="_blank">Benjamin Vianey</a> 
		        dans le cadre d'un projet d'étude. 
		        <br><br>
		        Les données sont issues du site disponible <a href="http://data.paysdelaloire.fr/" target="_blank"> ici </a>.
		        <br><br>
		        L'énoncé du problème auquel ce projet répond est disponible sur le <a HREF="https://github.com/sebprunier/installations-sportives-pdl" target="_blank">GitHub de Sébastien Prunier</a>
		      </div>
		      <div class="modal-footer">
		        <button type="button" class="btn btn-default" data-dismiss="modal">Fermer</button>
		      </div>
		    </div>
		  </div>
		</div>


		<!-- Footer -->
		<nav class="navbar-fixed-bottom">
		    <h5 class="text-center">Erwann Nevou - Pierre LeFrancois - Benjamin Vianey</h5>
		</nav>
	</body>
</html>
