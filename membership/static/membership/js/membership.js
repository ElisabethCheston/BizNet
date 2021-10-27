// Create a Stripe client.

  var stripe = Stripe("{{ STRIPE_PUBLIC_KEY }}");
  // Create an instance of Elements.
  var elements = stripe.elements();

  // Custom styling can be passed to options when creating an Element.
  // (Note that this demo uses a wider set of styles than the guide below.)
  var style = {
    base: {
      color: '#32325d',
      lineHeight: '18px',
      fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': {
        color: '#aab7c4'
      }
    },
    invalid: {
      color: '#fa755a',
      iconColor: '#fa755a'
    }
  };

  // Create an instance of the card Element.
  var card = elements.create('card', {style: style});

  // Add an instance of the card Element into the `card-element` <div>.
  card.mount('#card-element');

  // Handle real-time validation errors from the card Element.
  card.addEventListener('change', function(event) {
    var displayError = document.getElementById('card-errors');
    if (event.error) {
      displayError.textContent = event.error.message;
    } else {
      displayError.textContent = '';
    }
  });

  // Handle form submission.
  var form = document.getElementById('payment-form');
  form.addEventListener('submit', function(event) {
    event.preventDefault();

    stripe.createToken(card).then(function(result) {
      if (result.error) {
        // Inform the user if there was an error.
        var errorElement = document.getElementById('card-errors');
        errorElement.textContent = result.error.message;
      } else {
        // Send the token to your server.
        stripeTokenHandler(result.token);
      }
    });

  });

  var successElement = document.getElementById('stripe-token-handler');
  document.querySelector('.wrapper').addEventListener('click', function() {
    successElement.className = 'is-hidden';
  });

  function stripeTokenHandler(token) {
    successElement.className = '';
    successElement.querySelector('.token').textContent = token.id;
    // Insert the token ID into the form so it gets submitted to the server
    var form = document.getElementById('payment-form');
    var hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);
    form.appendChild(hiddenInput);

    // Submit the form
    form.submit();
  }


/*
// -- Fetch API to make a AJAX request  -- //

console.log("Sanity Check!");

// Get Stripe publishable key
fetch("config/")
    .then((result) => result.json())

    .then((data) => {
        const stripe = stripe(data.publicKey);


/*
    .then((freePrice, basicPrice, proPrice) => {

    // Initialize Stripe.js
    
    const freePriceInput = document.querySelector('#freePrice');
    freePriceInput.value = freePrice;
    const basicPriceInput = document.querySelector('#basicPrice');
    basicPriceInput.value = basicPrice;
    const proPriceInput = document.querySelector('#proPrice');
    proPriceInput.value = proPrice;

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
            return stripe.redirectToCheckout({ sessionId: session_id });
            })
            .then((res) => {
                console.log(res);
            });
        });
    }
});
*/


// -- FETCH ERRORS --//
// -- Reference: https://github.com/stripe-samples/checkout-single-subscription/blob/master/client/script.js -- //
/*
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
*/