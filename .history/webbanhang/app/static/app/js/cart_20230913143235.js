let updateBtns = document.getElementsByClassName('update-cart')
// console.log(updateBtns)
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productID = this.dataset.product;
        let action = this.dataset.action;
        console.log('productID', productID, ' action', action);
        if (user === "AnonymousUser") {
            console.log('user not login');
        } else {
            ud(productID, action);
        }
    })
}

const ud = (productID, action) => {
    console.log('user login');
    let url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body:  JSON.stringify({'productID': productID, ' action': action}),
    })
}