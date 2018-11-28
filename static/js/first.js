/**
 * Created by adagio on 2018-09-28.
 */

// Home selection
function home() {
    // Select the current sort option
    var current_sort_option = $('.middle-menu').find('.active').children('a').attr('id');

   // Remove active from all menu
    $('.top-menu').find('.active').removeClass('active');

    // // Let's sending a request to url
    var xhr = new XMLHttpRequest();
    xhr.open('GET','?selection='+current_sort_option, true);
    xhr.onload = function() {
        if(this.status ==200) {
            $('.row').replaceWith($(this.responseText).find(".row"));
        }
    };
    xhr.send();
}

// Menu selection
function menuselection(which_selection) {
    // Change the menu based on the selection: change the location of active
    $('#'+which_selection).parent().addClass('active').siblings().removeClass('active');

    // Select which sorting option is currently being selected
    var current_sort_option = $('.middle-menu').find('.active').children('a').attr('id');

    // // Let's sending a request to url
    var xhr = new XMLHttpRequest();
    xhr.open('GET', which_selection+'?selection='+current_sort_option, true);
    xhr.onload = function() {
        if(this.status ==200) {
             $('.row').replaceWith($(this.responseText).find(".row"));
             $('.pagination').replaceWith($(this.responseText).filter(".pagination"));
        }
    };
    xhr.send();
    return false;
}

// Counting how many times the item has been clicked
function dbupdate(id) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/dbupdate?id='+id, true);
    xhr.onload = function() {
        //console.log(this.responseText);
    };
    xhr.send();
}

// Selection of sorting method
function sortingselection(which_selection) {

    // This part updates 'active'
    $('#'+which_selection).parent().addClass('active').siblings().removeClass('active');

    // Check which menu is currently being selected
    var menu = $('.top-menu').find('.active').children('a').attr('id');

    // // Let's sending a request to url
    var xhr = new XMLHttpRequest();

    if (menu) // If a menu is being selected
        xhr.open('GET', menu+'?selection='+which_selection, true);
    else     // otherwise
        xhr.open('GET','?selection='+which_selection, true);

    xhr.onload = function() {
        if(this.status ==200) {
            $('.row').replaceWith($(this.responseText).find(".row"));
        }
    };
    xhr.send();
}
