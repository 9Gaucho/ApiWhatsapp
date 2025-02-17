document.getElementById("ponto-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Impede o envio do formulário
    
    let nome = document.getElementById("nome").value;
    let hora = document.getElementById("hora").value || getCurrentTime();
    let tipo = document.getElementById("tipo").value;

    if (nome && hora && tipo) {
        const registro = {
            nome: nome,
            hora: hora,
            tipo: tipo
        };
        
        adicionarRegistro(registro);
    }
});

function getCurrentTime() {
    const now = new Date();
    let hours = now.getHours();
    let minutes = now.getMinutes();

    // Adiciona zero à esquerda se for necessário
    hours = (hours < 10) ? '0' + hours : hours;
    minutes = (minutes < 10) ? '0' + minutes : minutes;

    return hours + ':' + minutes;
}

function adicionarRegistro(registro) {
    const historicoList = document.getElementById("historico-list");
    
    const li = document.createElement("li");
    li.textContent = `${registro.nome} registrou ${registro.tipo === 'entrada' ? 'entrada' : 'saída'} às ${registro.hora}`;
    historicoList.appendChild(li);
    
    // Limpar os campos
    document.getElementById("nome").value = '';
    document.getElementById("hora").value = '';
}
