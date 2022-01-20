if (localStorage.getItem('cart') == null) {
    var cart = {};
    document.getElementById('items').innerHTML = `<p>Nothing to show here.. Please add items to the cart</p>`;
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    carts = Object.values(cart);
    totalPrice = 0;
    carts.forEach(element => {
        name = element[0];
        qty = element[1];
        price = element[2];
        totalPrice += qty * price;
        document.getElementById('items').innerHTML += `<li class="list-group-item d-flex         justify-content-between align-items-center">
            ${name}
        <span class="badge bg-primary rounded-pill">${qty}</span>
        </li>`;
    });
    document.getElementById('items').innerHTML += `<li class="list-group-item d-flex                justify-content-between align-items-center bg-secondary my-2">
            <b>Total Price</b>
        <span class="badge bg-primary rounded-pill">Rs. <span id="price">${totalPrice}</span></span>
        </li>`;
    document.getElementById('clearCartBtn').innerHTML = `<button id="clearCart" class="btn btn-danger">Clear cart</button>`;
    document.getElementById('clearCart').addEventListener('click', function () {
        localStorage.clear();
        location.reload();
    });
    document.getElementById('items_json').value = JSON.stringify(localStorage.getItem('cart'));
    document.getElementById('amount').value = document.getElementById('price').innerHTML;
}
