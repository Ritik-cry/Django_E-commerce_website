if (localStorage.getItem('cart') == null) {
    var cart = {};
    document.getElementById('cartN').innerHTML = 0;
}
else {
    cart = JSON.parse(localStorage.getItem('cart'));
    cartLenght(cart);
}

var cartbtn = document.querySelectorAll('.cartbtn')
for (const item of cartbtn) {
    item.addEventListener('click', function () {
        var id = this.id;
        var idstr = id.toString();
        var prname = this.name;
        var prprice = document.getElementById('price'+id).innerText;
        if (cart[idstr] == undefined) {
            qty = 1;
            name = prname;
            price = parseInt(prprice);
            cart[idstr] = [name,qty,price];
        }
        else {
            qty = cart[idstr][1] + 1;
            name = prname;
            price = parseInt(prprice);
            cart[idstr] = [name,qty,price];
        }
        localStorage.setItem('cart',JSON.stringify(cart));
        cartLenght(cart);
        document.getElementById('alert').innerHTML = `<div class="alert alert-success" role="alert">
        &#9989 Congrats!..  The item has been added to the cart
      </div>`;
        setTimeout(() => {
            document.getElementById('alert').innerHTML = '';
        }, 1000);
    });
}

function cartLenght(cart) {
    value = Object.values(cart);
    sum = 0;
    value.forEach(element => {
        sum += element[1];
    });
    document.getElementById('cartN').innerHTML = sum;
}