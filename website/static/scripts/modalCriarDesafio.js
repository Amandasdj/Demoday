
const mostrarModal = () => {

    const modal = document.querySelector('#modal')
    const moldura = document.querySelector('#moldura')

    modal.className = 'ativo'
    moldura.className = 'ativo'
}

const fecharModal = () => {

    const modal = document.querySelector('#modal')
    const moldura = document.querySelector('#moldura')
    
    modal.className = 'inativo'
    moldura.className = 'inativo'
}

const colocarEvento = () => {

    const desafiar = document.querySelector('#desafiar')
    const bolinha = document.querySelector('#bolinha')
    
    bolinha.onclick = fecharModal
    desafiar.onclick = mostrarModal
}

colocarEvento()