
var i = 0

const colocarElementoEmGerais = (ind) => {
    const conteudo = document.querySelectorAll('.gerais')
    const blocoDesafiosGerais = document.querySelector('.bloco-desafios-gerais')

    if(conteudo[ind] == undefined){
        
        i = 0

        const atual = conteudo[i].cloneNode(true)
    
        return blocoDesafiosGerais.append(atual)

    }
    else{

        const atual = conteudo[ind].cloneNode(true)

        return blocoDesafiosGerais.append(atual)
    }
    
}

const trocarElementoEmGerais = (event) => {
    
    const blocoDesafiosGerais = document.querySelector('.bloco-desafios-gerais')
    const paraRemover = blocoDesafiosGerais.firstElementChild
    
    paraRemover.className = 'inativo'

    setTimeout(() => {

        paraRemover.remove()
        
        if(event.target.id == 'subtrair'){
            
            i--
            
            return colocarElementoEmGerais(i)
        }
        else{
            
            i++
    
            return colocarElementoEmGerais(i)
        }
    }, 500)
    
}
const atribuir = () => {
    const subtrair = document.querySelector('#subtrair')
    const adicionar = document.querySelector('#adicionar')
    subtrair.onclick = trocarElementoEmGerais
    adicionar.onclick = trocarElementoEmGerais

    return colocarElementoEmGerais(i)
}

atribuir()