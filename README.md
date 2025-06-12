# Video 62

# COMMANDES PYTHON
##### py -0
##### move *.* 1_Base1

# Configuration de Git Hub

## Etape 1: depuis l'ordinateur Bureau
- <span style="color:yellow;">***git init***<span/>
- ***git add .***
- <span style="color:yellow;">***git commit -m "first commit"***<span/>
- ***git branch -M main***
- <span style="color:yellow;">***git remote add origin https://github.com/ben2ci/1_FormationPython.git***<span/>
- ***git push -u origin main***


## Etape 2: depuis la maison
- ***pip install -r requirements.txt (en ayant fait -> pip freeze > requirements.txt)***
- <span style="color:yellow;">***git clone https://github.com/ben2ci/1_FormationPython.git***<span/>

## Etape 2.1: après des modifications à la maison
- <span style="color:yellow;">***git status***<span/>
- ***git add .***
- <span style="color:yellow;">***git commit -m "Description courte des modifications"***<span/>
- ***git push origin main***


## Etape 4: de retour au bureau
- <span style="color:yellow;">***git add .***<span/>
- ***git commit -m "Description des modifications faites au bureau"***
- <span style="color:yellow;">***git pull origin main***<span/>
- ***git push origin main***


## Etape 5: de retour à la maison
- <span style="color:yellow;">***git pull origin main***<span/>

***🛠️ Ensuite, tu peux travailler comme d’habitude***
- <span style="color:yellow;">***git add .***<span/>
- ***git commit -m "Modifications du soir à la maison"***
- <span style="color:yellow;">***git push origin main***<span/>


## Commande pour inatller un pakcage
- <span style="color:yellow;">***py -3.7 -m pip install Faker***<span/>

## Commande pour créer un environememnt virtuel
- <span style="color:yellow;">***py -3.7 -m venv env***<span/>
