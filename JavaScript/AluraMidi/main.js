function tocaSom(idTecla) {
    document.querySelector(idTecla).play();
}

const listaTeclas = document.querySelectorAll('.tecla');

for(let i = 0; i < listaTeclas.length; i++) {
    let tecla = listaTeclas[i];
    let instrumento = tecla.classList[1];

    tecla.onclick = function (){
        tocaSom(`#som_${instrumento}`);
    }
}
