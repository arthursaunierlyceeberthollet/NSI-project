from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Mot de passe en dur
PASSWORD = "JaiCompris"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/check-password", methods=["POST"])
def check_password():
    data = request.get_json()
    user_input = data.get("password", "")
    if user_input == PASSWORD:
        return jsonify({"result": "Bravo ! Mot de passe correct."})
    else:
        return jsonify({"result": "Mot de passe incorrect."})
    for i in range(nombre):
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
  
return PASSWORD

if __name__ == "__main__":
    app.run(debug=True)
