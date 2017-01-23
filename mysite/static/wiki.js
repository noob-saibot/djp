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

function notes(obj) {
var tmp = 0;
for (var key in obj) {
  if (obj.hasOwnProperty(key)) {
    setTimeout(function() { console.log(obj[key]);
    console.log(tmp);document.getElementsByClassName("affix")[0].innerHTML=obj[key];}, tmp);
    tmp += 5000;
                               }
                     }
/*setInterval(notes, 10000, obj)*/
}

