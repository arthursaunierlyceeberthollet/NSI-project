from flask import Flask, request, jsonify, render_template
nombre = 

chiffre = chiffre.checked
maj = majuscule.checked
spe = caractereSpeciaux.checked

proba_chiffre = nombre
proba_maj = nombre
proba_spe = nombre

# Mot de passe

PASSWORD = " "
ensemble_caractères = [[0,1,2,3,4,5,6,7,8,9],[A,Z,E,R,T,Y,U,I,O,P,Q,S,D,F,G,H,J,K,L,M,W,X,C,V,B,N]['~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|',';',':','<','>',',','.','/','?']];
caracteres = [a,z,e,r,t,y,u,i,o,p,q,s,d,f,g,h,j,k,l,m,w,x,c,v,b,n];


for i in range(nombre):
	if chiffre = true
	a = random.randint(0, 10)
		if proba_chiffre > a :
			PASSWORD += str(ensemble_caractères[0][a])
			proba_chiffre -= 1
	if maj = true
	a = random.randint(0, 10)
		if proba_maj > a :
			PASSWORD += str(ensemble_caractères[1][a])
			proba_maj -= 1
	if spe = true
	a = random.randint(0, 10)
		if proba_spe > a :
			PASSWORD += str(ensemble_caractères[2][a])
			proba_spe -= 1

while len(PASSWORD) != nombre :
	PASSWORD += str(random.choice(caracteres))
	
random.shuffle(PASSWORD)
  
return PASSWORD