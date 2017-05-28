var b64pad = "";
var chrsz = 8;
var me = this;
define([], function() { return me; });

function generate(secretpw, domain, callback) {

  require([ "assets/sha1" ], function(sha) {
    var input = secretpw + ':' + domain.toLowerCase();
    input = binb2b64(sha.binb_sha1(str2binb(input), input.length * chrsz));
    input = ensurenumberandletter(input.substring(0, 10));
    callback(input);
  });
}

function str2binb(str) {
  var bin = Array();
  var mask = (1 << chrsz) - 1;
  for (var i = 0; i < str.length * chrsz; i += chrsz)
    bin[i >> 5] |= (str.charCodeAt(i / chrsz) & mask) << (24 - i % 32);
  return bin;
}

function binb2b64(binarray) {
  var tab = "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz123456789?!#@&$";
  var str = "";
  for (var i = 0; i < binarray.length * 4; i += 3) {
    var triplet =
        (((binarray[i >> 2] >> 8 * (3 - i % 4)) & 0xFF) << 16) |
        (((binarray[i + 1 >> 2] >> 8 * (3 - (i + 1) % 4)) & 0xFF) << 8) |
        ((binarray[i + 2 >> 2] >> 8 * (3 - (i + 2) % 4)) & 0xFF);
    for (var j = 0; j < 4; j++) {
      if (i * 8 + j * 6 > binarray.length * 32)
        str += b64pad;
      else
        str += tab.charAt((triplet >> 6 * (3 - j)) & 0x3F);
    }
  }
  return str;
}

function ensurenumberandletter(s) {
  var numbers = "123456789";
  var letters = "ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz";
  var punct = "?!#@&$";
  var hasnumber = 0;
  var hasletter = 0;
  var haspunct = 0;

  for (var i = 0; i < s.length; i++) {
    if (numbers.indexOf(s[i]) > -1)
      hasnumber = 1;
    if (letters.indexOf(s[i]) > -1)
      hasletter = 1;
    if (punct.indexOf(s[i]) > -1)
      haspunct = 1;
  }
  if (hasnumber == 0)
    s = "1" + s.substring(1);
  if (hasletter == 0)
    s = s.substring(0, 1) + "a" + s.substring(2);
  if (haspunct == 0)
    s = s.substring(0, 2) + "@" + s.substring(3);

  return s;
}
