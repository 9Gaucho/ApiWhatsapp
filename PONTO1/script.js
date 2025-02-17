// Verificação de login
function verificarLogin() {
    let user = document.getElementById("username").value;
    let pass = document.getElementById("password").value;

    if (user === "123" && pass === "123") {
        document.getElementById("login-container").classList.add("hidden");
        document.getElementById("ponto-container").classList.remove("hidden");
    } else {
        document.getElementById("error-msg").innerText = "Usuário ou senha incorretos!";
    }
}

// Atualiza o horário em tempo real
function updateTime() {
    document.getElementById('time').innerText = new Date().toLocaleTimeString();
}
setInterval(updateTime, 1000);

// Registra o ponto no histórico
function baterPonto() {
    let timeStamp = new Date().toLocaleString();
    let listItem = document.createElement("li");
    listItem.innerText = "📌 " + timeStamp;
    document.getElementById("history-list").appendChild(listItem);
}
