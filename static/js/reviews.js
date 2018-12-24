/**
 * Created by adagio on 2018-09-28.
 */

// Menu selection
function menuselection(which_selection) {

    // change url displayed in the site
    if (history.pushState) {
      window.history.pushState("object or string", "Title", "/");
    } else {
        document.location.href = "/";
    }

    // // Let's sending a request to url
    var xhr = new XMLHttpRequest();
    xhr.open('GET', which_selection+'?selection=new', true);
    xhr.onload = function() {

        if(this.status ==200) {
            $("body").html(this.responseText);
            $('#'+which_selection).parent().addClass('active').siblings().removeClass('active');
        }
    };
    xhr.send();
    return false;
}

// Search form
$('#search-form').on('submit', function(event){
    event.preventDefault();
    send_sesearch_request();
});

function send_sesearch_request() {
    // Check which menu is currently being selected
    var menu = $('.top-menu').find('.active').children('a').attr('id');

    // Check which sorting option is currently being selected
    var sorting = $('.middle-menu').find('.active').children('a').attr('id');

    // CSRF obtain from HTML
    var token = $('input[name="csrfmiddlewaretoken"]').attr('value');

    // Get the string in the searching box
    var searchValue = document.getElementById("id_search").value;

    // // Let's sending a request to url
    var xhr = new XMLHttpRequest();

    if (menu) {// If a menu is being selected
        xhr.open('POST', menu, true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader('X-CSRFToken', token);
        xhr.send("selection="+sorting+"&search="+searchValue);}
    else {    // otherwise
        xhr.open('POST','/', true);
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.setRequestHeader('X-CSRFToken', token);
        xhr.send("selection="+sorting+"&search="+searchValue);}

    xhr.onload = function() {
         if(this.status ==200) {
            $('.replace').replaceWith($(this.responseText).find(".replace"));
            $('.pagination').replaceWith($(this.responseText).filter(".pagination"));
        }
    };
}