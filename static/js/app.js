
// -- For card info box to collaps. From Bootstraps -- //
var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
var collapseList = collapseElementList.map(function (collapseEl) {
  return new bootstrap.Collapse(collapseEl)
})


// -- Popover function -- //
var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover-term"]'))
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
  return new bootstrap.Popover(popoverTriggerEl)
})


// -- For tabs from Bootstraps -- //
function activaTab(tab) {
  $('.nav-tabs a[href="#' + tab + '"]').tab('show');
};



// -- Activate welcome message -- //

console.log('Welcome!')
console.log(document)

const test = document.getElementById('test')
// const gigs2 = document.getElementById('gigs2')
console.log(test)
/*
setTimeout(() => {
  test.textContent = "Check out the lastest updates below."
}, 2000)
*/
// -- Fetch json for gigs  -- //




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