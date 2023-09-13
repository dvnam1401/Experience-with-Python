let updateBtns = document.getElementsByClassName('update-cart')
// console.log(updateBtns)
for (i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function () {
        let productID = this.dataset.product;
        let action = this.dataset.action;
        console.log('productID', productID, ' action', action);
        if (user === "AnonymousUser") {
            console.log('user not login')
        } else {
            updateUserOrder(productID, action);
        }
    })
}

function updateUserOrder(productID, action) {
    console.log('user login');
    let url = '/update_item/';
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'productID': productID, 'action': action }),
    })
        .then((response) => response.json())
        .then((data) => console.log('data', data))
}