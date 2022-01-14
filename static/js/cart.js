var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
        var boxId = this.dataset.box
        var action = this.dataset.action
        console.log('boxId:', boxId, 'action:', action)
    })
}