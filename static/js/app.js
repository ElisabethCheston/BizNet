// -- Fetch API to make a AJAX request  -- //
/*
console.log("Sanity Check!");

// Get Stripe publishable key
fetch("/config/")
  .then((result) => result.json())
  .then((data) => {
    // Initialize Stripe.js
    const stripe = stripe(data.publicKey);

    // new

    // Event Handler
    let submitBtn = document.querySelector("#submitBtn");
    if (submitBtn != null) {
      submitBtn.addEventListener("click", () => {
        // Get Checkout Session ID
        fetch("/create-checkout-session/")
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
    }
  });
*/


// -- For card info box to collaps. From Bootstraps -- //
var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
/*
var collapseList = collapseElementList.map(function (collapseEl) {
  return new bootstrap.Collapse(collapseEl)
})
*/

// -- Popover function -- //
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover-term"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})

/*
// -- For tabs from Bootstraps -- //
function activaTab(tab) {
  $('.nav-tabs a[href="#' + tab + '"]').tab('show');
};
*/


// -- Activate welcome message -- //

console.log('Welcome!')
console.log(document)

const message = document.getElementById('message')
// const message2 = document.getElementById('message2')
console.log(message)

/*
setTimeout(() => {
  message.textContent = "Check out the lastest updates below."
}, 2000)
*/
/*
// -- Fetch json for gigs  -- //
$.ajax({
  type: 'GET',
  url: 'gig_json/',
  success: function(response) {
    console.log(response.data)
    const data = JSON.parse(response.data)
    console.log(data)
    setTimeout(() => {
      data.forEach(el=> {
        message2.innerHTML += `${el.fields.title}<br>`
      })
    }, 2000)
  },
  error: function(error) {
    console.log(error)
  }
})
*/


// -- To call the json data for industry --//
/*
var industryChoice = {
  id: fields._id_prof, 
  industry_name: fields.industry_name,
};


$.ajax({
  type: 'POST',
  url: 'profileusers/fixtures/industry.json',
  contentType: 'application/json; charset=utf-8',
  data: $.toJSON(industryChoice),
  dataType: 'text',
  success: function (result) {
    alert(result.Result);
  }
});
*/