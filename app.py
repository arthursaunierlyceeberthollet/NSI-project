from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# variables en dur 
#PASSWORD = "JaiCompris"
ensemble_caractères = [[0,1,2,3,4,5,6,7,8,9],[A,Z,E,R,T,Y,U,I,O,P,Q,S,D,F,G,H,J,K,L,M,W,X,C,V,B,N]['~','`','!','@','#','$','%','^','&','*','(',')','-','_','+','=','{','}','[',']','|',';',':','<','>',',','.','/','?']];
caracteres = [a,z,e,r,t,y,u,i,o,p,q,s,d,f,g,h,j,k,l,m,w,x,c,v,b,n];

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check-password", methods=["POST"])
def check_password():
    data = request.get_json()
    user_input = data.get("password", "")
	    
    for i in range(user_input):
	if chiffre = True
		a = random.randint(0, 10)
		if proba_chiffre > a :
			PASSWORD += str(ensemble_caractères[0][a])
			proba_chiffre -= 1
	if maj = True
	a = random.randint(0, 10)
		if proba_maj > a :
			PASSWORD += str(ensemble_caractères[1][a])
			proba_maj -= 1
	if spe = True
		a = random.randint(0, 10)
			if proba_spe > a :
				PASSWORD += str(ensemble_caractères[2][a])
				proba_spe -= 1

      while len(PASSWORD) != nombre :
	PASSWORD += str(random.choice(caracteres))
	
	random.shuffle(PASSWORD)

      return jsonify({"result": PASSWORD })


if __name__ == "__main__":
    app.run(debug=True)
