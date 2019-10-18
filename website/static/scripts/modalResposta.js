
const removerElementos = (moldura) => {

    const elementos = moldura.children

    for(let i = 3; i >= 0; i--){
        elementos[i].remove()
    }
}

const colocarElementos = (moldura, target) => {
    const conteudo = target.children[2].children

    for(let elm of conteudo){

        let clone = elm.cloneNode(true)

        moldura.appendChild(clone)
    }
}

const mostrarModal = (event) => {

    const modal = document.querySelector('#modal')
    const moldura = document.querySelector('#moldura')
    const bolinha = document.querySelector('#modal #bolinha')
        
    bolinha.onclick = fecharModal
    modal.className = 'ativo'
    moldura.className = 'ativo'
        
    return colocarElementos(moldura, event.target)
}

const fecharModal = () => {

    const modal = document.querySelector('#modal')
    const moldura = document.querySelector('#moldura')
    
    removerElementos(moldura)
    
    modal.className = 'inativo'
    moldura.className = 'inativo'
}

const colocarEvento = () => {

    const respostas = document.querySelectorAll('.bloco-resposta')
    
    for(let elm of respostas){
        elm.onclick = mostrarModal
    }
}

colocarEvento()