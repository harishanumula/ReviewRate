/* javascript file */

$(document).ready( function(){

var res = $("#results");



//var results = document.getElementById("results");

res.html("fffa");

//res.text("kkk");

var toggle = $("#toggle");

toggle.on("click",function(){
    res.toggle(500);
});




result = [{
    name: "harish",
    age : "19"
}]

res.empty();

$.each(result,function(i,item){
    var k = "<div><table><tr><th>name</th><th>age</th></tr>" +
    "<tr><td>" + item.name+"</td><td>"+item.age+"</td></tr></table></div>";
    res.append(k);
});

/*res.on({
            mouseenter:function(){
            //res.toggle(500);
            res.css("background-color","red");
            },
            mouseleave:function(){
             res.css("background-color","white");
            }
});*/

});