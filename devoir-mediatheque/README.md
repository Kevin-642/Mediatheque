# Mediatheque
 Projet Médiatheque CEF


INSTRUCTION POUR EXECUTER LE PROGRAMME

		Préparer l'Environnement Virtuel de Travail

	Il est suggéré d'avoir un environnement virtuel dédié pour chaque projet Django, et un moyen de gérer un environnement virtuel. est venv,  qui est inclus dans Python.
    Le nom de l'environnement virtuel  pour les instructions l'appellera « mymediatheque ».


	1. Tapez ce qui suit dans l'invite de commande, n'oubliez pas de naviguer jusqu'à où vous voulez créer votre projet:

	Windows :
			py -m venv mymediatheque

	Unix/MacOs :
			python -m venv mymediatheque 

	Cela permettra de créer un environnement virtuel et de créer un dossier nommé « mymediatheque » avec des sous-dossiers et des fichiers, comme ceci: 

				mymediatheque
				  Include
				  Lib
				  Scripts
				  pyvenv.cfg 

	2. Ensuite, vous devez activer l'environnement, en tapant cette commande: 

	Windows :
			mymediatheque\Scripts\activate.bat

	Unix/MacOs :
			source mymediatheque/bin/activate

	3. Une fois l'environnement activé, vous verrez ce résultat dans l'invite de commande: 

	Windows :
			(mymediatheque)  C:\Users\YourName>

	Unix/MacOs :
			(mymediatheque) … $


    Remarque: Vous devez activer l'environnement virtuel chaque fois que vous ouvrez la commande invite à travailler sur le projet. 


	4. Maintenant, que nous avons créé un environnement virtuel, nous sommes prêts à installer Django. 

	Remarque: N'oubliez pas d'installer Django pendant que vous êtes dans l'environnement virtuel. 

	5. Django est installé à l'aide de pip, avec cette commande: 

	Windows :
			(mymediatheque)  C:\Users\YourName>py -m pip install Django 

	Unix/MacOs :
			(mymediatheque) … $ python -m pip install Django 


	6. Maintenant, que vous avez installé Django dans votre nouveau projet, en cours d'exécution dans un environnement virtuel. 

	Vous pouvez vérifier si Django est installé en demandant son numéro de version comme ceci: 
			(mymediatheque)  C:\Users\YourName>django-admin --version  

	Si Django est installé, vous obtiendrez un résultat avec le numéro de version: 

			5.1.2


	7. Il se peut que vous rencontriez ce message :

    A new release of pip is available: 24.2-> 24.3.1
    To update, run : python.exe -m pip install --updrade pip 


	8. Excecutez la commande pour « update » la derniere version de pip.


	9. Après ça veuillez entrer les commandes suivantes : 

	(mymediatheque) C:\Users\kevin>cd devoir-mediatheque

	(mymediatheque) C:\Users\kevin\devoir-mediatheque>cd mediatheque

	(mymediatheque) C:\Users\kevin\devoir-mediatheque\mediatheque>py manage.py runserver

	Suite à ça vous devriez obtenir ce résultat dans l'invite de commande: 

    Watching for fil changes with StatReloader
    Performing system checks...

    System check identified no issues (0silenced).
    October 30, 2024 - 17:47:50
    Django version 5.1.2, using settings 'mediatheque.settings'
    Starting developpement server at http://127.0.0.0:8000/
    Quit the server with CTRL-Break

	10. Appuyez simultanément sur la touche CTRL+ Clic Gauche de la souris pour ouvrir le projet sur votre navigateur.  


	Pour acceder au menu « admin » , veuillez entrer l'adresse suivante :

    127.0.0.1:8000/admin/

	Qui vous dirigera vers cette page si tu se passe bien :


	Informations d'utilisateur (superuser) pour se connecter à la base de données :
	
    Nom d'utilisateur : BibliothecaireChef02
    Mot de passe : Media2024