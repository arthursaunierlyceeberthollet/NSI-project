document.getElementById("submitBtn").addEventListener("click", () => {
  const bouton = document.getElementById("submitBtn").value;
  const majuscule = document.getElementById("majuscule").value;
  const caractereSpeciaux = document.getElementById("caractereSpeciaux").value;
  const chiffre = document.getElementById("chiffre").value;

  // Envoi la requête POST au backend Python
  fetch("/check-password", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ password }),
  })
    .then((response) => response.json())
    .then((data) => {
      document.getElementById("response").textContent = data.result;
    })
    .catch(() => {
      document.getElementById("response").textContent = "Erreur serveur.";
    });
});

const choix = () => {
	nb = 0;
	if (majuscule.checked == true){
		nb = nb+1;
	}
	if (caractereSpeciaux.checked == true){
		nb = nb+1;
	}
	if (chiffre.checked == true){
		nb = nb+1;
	console.log( nb);
}
