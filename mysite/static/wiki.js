function wiki()
{
if (window.location.href != "http://memorialab.info/blog/main/") {
var xhr = new XMLHttpRequest();
//xhr.open('GET', "http://memorialab.info/blog/api/?id=" + window.location.href.split("/").slice(-2)[0], false);
xhr.open('GET', "http://memorialab.info/api/wiki_notes/?format=json&post_id=" + window.location.href.split("/").slice(-2)[0], false);
xhr.send(null);
var obj = JSON.parse(xhr.responseText);
var values = Object.keys(obj).map(function(key){
    return obj[key];
});

if (values.length != 0) {
var obj = JSON.parse(values[0]["content"].replace(/\"/g, "xe23r").replace(/'/g, '"').replace(/xe23r/g, "\'"));
values = Object.keys(obj).map(function(key){
return obj[key];
});
return obj, values;
}
else {return ""}
                                                                 }
else {return ""}
}

function affix_setter(set, time) {
  var x = document.getElementsByClassName('note')[0];
  setTimeout(function(){x.innerHTML = set}, time);
}


function notes(index, values) {
  index = parseInt(document.getElementsByName("next")[0].value, 10) + index;
  if (values.length != 0) {
    if (index < 0) {index += values.length;}
    else if (index >= values.length) {index -= values.length;}
    //console.log(values[0]["content"].replace(/\"/g, "xe23r").replace(/'/g, '"').replace(/xe23r/g, "\'"))
    //var obj = JSON.parse(values[0]["content"].replace(/\"/g, "xe23r").replace(/'/g, '"').replace(/xe23r/g, "\'"));
    //values = Object.keys(obj).map(function(key){
    //return obj[key];
    //});
    console.log(values[index]);
    affix_setter(values[index], 0);
    document.getElementsByName("next")[0].value = index;}
  else {document.getElementsByClassName('affix')[0].innerHTML = ""}
                    }

