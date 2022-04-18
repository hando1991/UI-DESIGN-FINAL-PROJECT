$(document).ready(function(){
    start()
    $("#next[number='1']").click(function(){
        page2() 
    })  
    $("#next[number='2']").click(function(){
    })  
    $("#return_button").click(function(){
        window.location.href =  "http://127.0.0.1:5000/learn1"
    })
})

function page2(){
    clean()
    $("#next").attr('number','2')
    $("h1").html("Selected a Definition for more details")
    $("#learn_1").html("<a href='http://127.0.0.1:5000/view/1'>Receivables</a>")
    $("#learn_2").html("<a href='http://127.0.0.1:5000/view/2'>Inventory</a>")
    $("#learn_3").html("<a href='http://127.0.0.1:5000/view/3'>Property Plant & Equipment</a>")

}

function start(){
    $("#next").attr('number','1')
    $("h1").html("Asset Entry")
    $("h1").addClass("title")
    $("h1").append("<div><input type = 'image' width = '600px' src = 'https://cdn.wallstreetmojo.com/wp-content/uploads/2019/07/Asset-Classes-1.jpg'></input></div>")
    $("#learn_1").html("<b>1.Economic resources (Resources that will provide monetary benefits:</b>")
    $("#learn_1").append("<div>a.Cash</div> <div>b.Things to be converted to cash (inventory, other firm’s stock)</div>c.Items used to generate cash.")
    $("#learn_2").html("<b>2.Owned or controlled by the entity.</b>")
    $("#learn_3").html("<b>3.Conveniently measurable cost at time of acquisition.</b>")
    $("#learn_4").html("<b>4.Any balance sheet item that, if converted to cash today, would bring cash to the entity.</b>")
}

function clean(){
    $("h1").html('')
    $("#learn_1").html("")
    $("#learn_2").html("")
    $("#learn_3").html("")
    $("#learn_4").html("")
}
