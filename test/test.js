



var bar = [1, 2, 3]; 
for (var i in bar) {
    setTimeout(function () { console.log(bar[i]) }, 0);
    console.log(bar[i]);
}