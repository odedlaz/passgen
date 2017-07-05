
$(function() {
  cb = new Clipboard('.btn');
  $('#secretpass').keypress(function(e) {
    if (e.which == 13) {
      generatePassword();
      return false;
    }
  });
});

function generatePassword() {
  require([ "assets/chameleon" ], function(pwc) {
    pwc.generate($("#secretpass").val(), $("#domain").val(),
                 function(pw) { $("#passwd").val(pw); });
  });
}
