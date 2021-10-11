// -- Fetch API to make a AJAX request  -- //

console.log("Sanity Check!");

// Get Stripe publishable key
fetch("config/")
    .then((result) => result.json())
/*
    .then((data) => {
        const stripe = stripe(data.publicKey);
*/

    .then((freePrice, basicPrice, proPrice) => {

    // Initialize Stripe.js
    
    const freePriceInput = document.querySelector('#freePrice');
    freePriceInput.value = freePrice;
    const basicPriceInput = document.querySelector('#basicPrice');
    basicPriceInput.value = basicPrice;
    const proPriceInput = document.querySelector('#proPrice');
    proPriceInput.value = proPrice;


    // new
/*
    // Event Handler
    let submitBtn = document.querySelector("#submitBtn");
    if (submitBtn != null) {
        submitBtn.addEventListener("click", () => {
        // Get Checkout Session ID
            fetch("create-checkout-session/")
            .then((result) => {
                return result.json();
            })
            .then((data) => {
                console.log(data);

            // Redirect to Stripe Checkout
                return stripe.redirectToCheckout({ sessionId: data.sessionId });
            })
            .then((res) => {
                console.log(res);
            });
        });
    } */
});

// -- FETCH ERRORS --//
// -- Reference: https://github.com/stripe-samples/checkout-single-subscription/blob/master/client/script.js -- //

// If a fetch error occurs, log it to the console and show it in the UI.
var handleFetchResult = function(result) {
    if (!result.ok) {
      return result.json().then(function(json) {
        if (json.error && json.error.message) {
          throw new Error(result.url + ' ' + result.status + ' ' + json.error.message);
        }
      }).catch(function(err) {
        showErrorMessage(err);
        throw err;
      });
    }
    return result.json();
  };
  
  var showErrorMessage = function(message) {
    var errorEl = document.getElementById("error-message")
    errorEl.textContent = message;
    errorEl.style.display = "block";
  };
