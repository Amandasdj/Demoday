
var i = 0

const colocarElementosResposta = (ind) => {
    const conteudo = document.querySelectorAll('.bloco-resposta')
    const divResposta = document.querySelector('.div-resposta')

    if(conteudo[ind] == undefined){
        
        i = 0

        const atual = conteudo[i].cloneNode(true)
    
        return divResposta.append(atual)

    }
    else{

        const atual = conteudo[ind].cloneNode(true)

        return divResposta.append(atual)
    }
    
}

const trocarElementosResposta = (event) => {
    
    const divResposta = document.querySelector('.div-resposta')
    const paraRemover = divResposta.lastElementChild
    
    paraRemover.className = 'inativo'

    paraRemover.remove()
    
    if(event.target.id == 'subtrair'){
        
        i--
        
        return colocarElementosResposta(i)
    }
    else{
        
        i++

        return colocarElementosResposta(i)
    }
    
}
const atribuir = () => {
    const subtrair = document.querySelector('#subtrair')
    const adicionar = document.querySelector('#adicionar')
    subtrair.onclick = trocarElementosResposta
    adicionar.onclick = trocarElementosResposta

    return colocarElementosResposta(i)
}

atribuir()