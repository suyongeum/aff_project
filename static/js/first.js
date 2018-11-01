/**
 * Created by adagio on 2018-09-28.
 */

//$(function(){

$(document).ready(function() {
    var pathname = window.location.pathname;
    $('.nav-item a[href="'+pathname+'"]').parent().addClass('active').siblings().removeClass('active');
});

$(document).ready(function() {
    var pathname = window.location.pathname;
    $('.middle-name a[href="'+pathname+'"]').parent().addClass('active').siblings().removeClass('active');
});

function dbupdate(id) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/dbupdate?id='+id, true);
    xhr.onload = function() {
        console.log(this.responseText);
    };
    xhr.send();
}

    // name        = models.CharField(max_length=100)
    // description = models.TextField()
    // price       = models.DecimalField(max_digits=6, decimal_places=2)
    // clicks      = models.IntegerField(default=0)
    // image       = models.ImageField()
    // link        = models.CharField(max_length=200)
    // datetime    = models.DateTimeField()

              //     <script>
              //     if (window.location.pathname == '/man') {
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/man/newsort\"><span class=\"newest\"><strong>Newest</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/man/popularsort\"><span class=\"popular\"><strong>Popular</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/man/pricesort\"><span class=\"price\"><strong>Price</strong></span></a></li>");
              //     } else if (window.location.pathname == '/woman')   {
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/woman/newsort\"><span class=\"newest\"><strong>Newest</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/woman/popularsort\"><span class=\"popular\"><strong>Popular</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/woman/pricesort\"><span class=\"price\"><strong>Price</strong></span></a></li>");
              //     } else if (window.location.pathname == '/geek') {
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/geek/newsort\"><span class=\"newest\"><strong>Newest</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/geek/popularsort\"><span class=\"popular\"><strong>Popular</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/geek/pricesort\"><span class=\"price\"><strong>Price</strong></span></a></li>");
              //     } else if (window.location.pathname == '/kids') {
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/kids/newsort\"><span class=\"newest\"><strong>Newest</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/kids/popularsort\"><span class=\"popular\"><strong>Popular</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/kids/pricesort\"><span class=\"price\"><strong>Price</strong></span></a></li>");
              //     } else {
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/newsort\"><span class=\"newest\"><strong>Newest</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/popularsort\"><span class=\"popular\"><strong>Popular</strong></span></a></li>");
              //         document.write("<li><i class=\"fas fa-sort-alpha-up\"></i>: <a href=\"/pricesort\"><span class=\"price\"><strong>Price</strong></span></a></li>");
              //     }
              // </script>