function wiki()
{
if (window.location.href != "http://memorialab.info/blog/main/") {
var xhr = new XMLHttpRequest();
xhr.open('GET', "http://memorialab.info/blog/api/?id=" + window.location.href.split("/").slice(-2)[0], false);
xhr.send(null);
var obj = JSON.parse(xhr.responseText);
var values = Object.keys(obj).map(function(key){
    return obj[key];
});
return obj, values;
                                                                 }
else {return ""}
}

function affix_setter(set, time) {
  var x = document.getElementsByClassName('note')[0];
  setTimeout(function(){x.innerHTML = set}, time);
}


function notes(index, values) {
  console.log(values);
  if (values.length != 0) {
  affix_setter(values[index], 0);
  console.log(index)
  window.id = index}
  else {document.getElementsByClassName('affix')[0].innerHTML = ""}
                    }

