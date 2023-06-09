var updateBtns = document.getElementsByClassName("update-cart");

function updateUserOrder(productId, action, quantity) {
  console.log("User is authenticated, sending data...");

  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productId: productId,
      action: action,
      quantity: quantity,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log("data:", data);
      document.querySelector("#cart-count").textContent =
        data.cart_items_quantity;
      location.reload();
    });
}

function addCookieItem(productId, action) {
  console.log("User is not authenticated");

  if (action == "add") {
    if (cart[productId] == undefined) {
      cart[productId] = { quantity: 1 };
    } else {
      cart[productId]["quantity"] += 1;
    }
  }

  if (action == "remove") {
    cart[productId]["quantity"] -= 1;

    if (cart[productId]["quantity"] <= 0) {
      console.log("Item should be deleted");
      delete cart[productId];
    }
  }
  console.log("CART:", cart);
  document.cookie = "cart=" + JSON.stringify(cart) + ";domain=;path=/";

  location.reload();
}
