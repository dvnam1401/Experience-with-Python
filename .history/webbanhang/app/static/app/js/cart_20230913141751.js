let updateBtns = document.getElementsByClassName('update-cart')
// console.log(updateBtns)
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productID = this.dataset.product;
        let action = this.dataset.action;
        console.log('productID', productID, ' action', action);
        console.log('user: ', user)
        if (user === "AnonymousUser") {

        }
    })
}