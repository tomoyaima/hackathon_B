var obj = document.getElementById("d1");
function color(time){
    if(time==0){
        obj.style.backgroundColor = "rgba(0,0,255,0)"; 
    }
    else if(time<=3){
        obj.style.backgroundColor = "rgba(0,0,255,0.25)"; 
    }
    else if(time<=6){
        obj.style.backgroundColor = "rgba(0,0,255,0.5)";         
    }
    else if(time<=9){
        obj.style.backgroundColor = "rgba(0,0,255,0.75)";         
    }
    else{
        obj.style.backgroundColor = "rgba(0,0,255,1)";         
    }
}

let time0=15;

function day(){
    let day0 = date.getDate();
}

window.onload = function () {
    var today = new Date();
     console.log(today);
  
     console.log("年=" + today.getFullYear());
     console.log("月=" + (today.getMonth()+1));
     console.log("日=" + today.getDate());
     console.log("時=" + today.getHours());
     console.log("分=" + today.getMinutes());
     console.log("秒=" + today.getSeconds());
 }