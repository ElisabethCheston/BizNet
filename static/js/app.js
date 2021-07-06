
// -- For card info box to collaps. From Bootstraps -- //
var collapseElementList = [].slice.call(document.querySelectorAll('.collapse'))
var collapseList = collapseElementList.map(function (collapseEl) {
  return new bootstrap.Collapse(collapseEl)
})

// -- For tabs from Bootstraps -- //

function activaTab(tab){
  $('.nav-tabs a[href="#' + tab + '"]').tab('show');
};

//activaTab('bbb');

/*
$(document).ready(function(){
  activaTab('aaa');
});

function activaTab(tab){
  $('.nav-tabs a[href="#new-gig"]').tab('show');
  $('.nav-tabs a[href="#saved-gig"]').tab('show');
  $('.nav-tabs a[href="#apply-gig"]').tab('show');
  $('.nav-tabs a[href="#hide-gig"]]').tab('show');
};
*/
