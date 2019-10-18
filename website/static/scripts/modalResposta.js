
const removerElementos = (moldura) => {

    const elementos = moldura.children

    for(let i = 3; i >= 0; i--){

        elementos[i].remove()
    }
}

const colocarElementos = (moldura, target) => {
    const conteudo = target.children[3].children

    for(let elm of conteudo){

        console.log(elm)

        let clone = elm.cloneNode(true)

        console.log(clone)

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
    
    const targetPai = event.target.parentNode
    const targetAvo = targetPai.parentNode

    return colocarElementos(moldura, targetAvo)
}

const fecharModal = () => {

    const modal = document.querySelector('#modal')
    const moldura = document.querySelector('#moldura')
    
    removerElementos(moldura)
    
    modal.className = 'inativo'
    moldura.className = 'inativo'
}

const colocarEvento = () => {

    const respostas = document.querySelectorAll('.ver-resposta')
    
    for(let elm of respostas){
        elm.onclick = mostrarModal
    }
}

colocarEvento()