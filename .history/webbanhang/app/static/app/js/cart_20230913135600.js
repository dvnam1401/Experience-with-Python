let updateBtns = document.getElementsByClassName('update-cart')
for(i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', () => {
        let productID = this.dataset.product;
        let action = this.dataset.action;
    })
}