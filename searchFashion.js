var count = 1;
var myJSON;

function getValue() {
    var y = document.getElementById('boo');
    var x = document.getElementById('input1').value;
    y.innerHTML=x;
    myJSON = JSON.stringify(x);
    alert(myJSON);
  }


function newcard(){
    var block_to_insert ;
    var container_block ;
    var wardoresize = 12;

    var res = "clothing #" + count.toString();
    
    block_to_insert = document.createElement( 'div' );
    block_to_insert.innerHTML = 'Inserted text' ;
    block_to_insert.setAttribute("class","grid-item");
    block_to_insert.setAttribute("id",res )
    
    container_block = document.getElementById( 'grid-container' );
    container_block.appendChild( block_to_insert );
    
    var img = document.createElement("img");
    var src = document.getElementById(res);
    img.src = "pic/fashion/"+count+".jpg";
    src.appendChild(img);
    document.getElementById(res).width = "10px";

    count++;

    if (count>wardoresize){
        alert("that's all of your clothes");
    }
}


 