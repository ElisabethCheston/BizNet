/*
const tabs = document.querySelectorAll('[data-tab-target')
const tabContents = document.querySelectorAll('[data-tab-content')

tabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const target = document.querySelector(tab.dataset.tabTarget)
        // Remove the none active data
        tabContents.forEach(tabContent => {
            tabContent.classList.remove('active')
        })
        tabs.forEach(tab => {
            tab.classList.remove('active')
        })
        tab.classList.add('active')
        target.classList.add('active')
    })
})
*/


var triggerTabList = [].slice.call(document.querySelectorAll('#gigTab a'))
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', function (event) {
    event.preventDefault()
    tabTrigger.show()
  })
})

var triggerEl = document.querySelector('#gigTab a[href="#new"]')
bootstrap.Tab.getInstance(triggerEl).show() // Select tab by name

var triggerEl = document.querySelector('#gigTab a[href="#saved"]')
bootstrap.Tab.getInstance(triggerEl).show() // Select tab by name

var triggerEl = document.querySelector('#gigTab a[href="#apply"]')
bootstrap.Tab.getInstance(triggerEl).show() // Select tab by name

var triggerEl = document.querySelector('#gigTab a[href="#hide"]')
bootstrap.Tab.getInstance(triggerEl).show() // Select tab by name


// Javascript to enable link to tab
/*
var url = document.location.toString();
if (url.match('hide_gig')) {
    $('.nav-tabs a[href=hide_gig'+url.split('hide_gig')[1]+']').tab('show') ;
} 
// Change hash for page-reload
$('.nav-tabs a').on('shown', function (e) {
    window.location.hash = e.target.hash;
})


function activaTab(tab){
    $('.nav-tabs a[href="new_gig' + tab + '"]').tab('show');
    };
    
window.onload = function(){  
    var url = document.location.toString();
    if (url.match('new_gig')) {
        $('.nav-tabs a[href="new_gig' + url.split('new_gig')[1] + '"]').tab('show');
    }
    //Change hash for page-reload
    $('.nav-tabs a[href="new_gig' + url.split('new_gig')[1] + '"]').on('shown', function (e) {
        window.location.hash = e.target.hash;
    }); 
}

function activaTab(tab){
    $('.nav-tabs a[href="saved_gig' + tab + '"]').tab('show');
    };
    
window.onload = function(){  
    var url = document.location.toString();
    if (url.match('saved_gig')) {
        $('.nav-tabs a[href="saved_gig' + url.split('saved_gig')[1] + '"]').tab('show');
    }
    //Change hash for page-reload
    $('.nav-tabs a[href="saved_gig' + url.split('saved_gig')[1] + '"]').on('shown', function (e) {
        window.location.hash = e.target.hash;
    }); 
}

function activaTab(tab){
    $('.nav-tabs a[href="apply_gig' + tab + '"]').tab('show');
    };
    
window.onload = function(){  
    var url = document.location.toString();
    if (url.match('apply_gig')) {
        $('.nav-tabs a[href="apply_gig' + url.split('apply_gig')[1] + '"]').tab('show');
    }
    //Change hash for page-reload
    $('.nav-tabs a[href="apply_gig' + url.split('apply_gig')[1] + '"]').on('shown', function (e) {
        window.location.hash = e.target.hash;
    }); 
}


function activaTab(tab){
$('.nav-tabs a[href="hide_gig' + tab + '"]').tab('show');
};

window.onload = function(){  
    var url = document.location.toString();
    if (url.match('hide_gig')) {
        $('.nav-tabs a[href="hide_gig' + url.split('hide_gig')[1] + '"]').tab('show');
    }
    //Change hash for page-reload
    $('.nav-tabs a[href="hide_gig' + url.split('hide_gig')[1] + '"]').on('shown', function (e) {
        window.location.hash = e.target.hash;
    }); 
} 


jQuery(document).ready(function($){
    $(".addSaveGig").on("click",function(){
        $.ajax({
            url: "{% url 'save_gig' %}",
            type: "POST",
            data: gd_list,
            success: function(response){
                  //do action  
            },
            error: function(){
                  // do action
            }
        });
    });
});


jQuery(document).ready(function($){
    $(".addAppliedGig").on("click",function(){
        $.ajax({
            url: "{% url 'apply_gig' %}",
            type: "POST",
            data: gd_list,
            success: function(response){
                  //do action  
            },
            error: function(){
                  // do action
            }
        });
    });
});


jQuery(document).ready(function($){
    $(".addHideGig").on("click",function(){
        $.ajax({
            url: "{% url 'hide_gig' %}",
            type: "POST",
            data: gd_list,
            success: function(response){
                  //do action  
            },
            error: function(){
                  // do action
            }
        });
    });
});
*/