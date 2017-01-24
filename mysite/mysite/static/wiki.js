function wiki()
{
if (window.location.href != "http://memorialab.info/blog/main/") {
var xhr = new XMLHttpRequest();
xhr.open('GET', "http://memorialab.info/blog/api/?id=" + window.location.href.split("/").slice(-2)[0], false);
xhr.send(null);
var obj = JSON.parse(xhr.responseText);
return obj;
                                                                 }
else {return ""}
}

function notes(dict) {
var tmp = 0
for(var key in dict) {
  var value = dict[key];
  var x = document.getElementsByClassName('affix')[0];
  setTimeout(function (val) { x.innerHTML = val; }, tmp, value);
  tmp += 3000
                     }
}

