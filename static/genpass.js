$(function() {
    $('a#submit_form').bind('click', function() {
        $.getScript("/static/sha1.js", function(){
          //  var password = $('input[name="password"]');
           // var hash = Sha1.hash(password.val());
           // $('input[name="password"]').val(hash);
            $('form[name="myform"]').submit();
        });
    });
});



