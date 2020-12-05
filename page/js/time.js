// import firebase from "firebase/app"
// import "firebase/firestore"
const db = firebase.firestore();
let user_name = document.getElementById('user_name')
let eye_time = document.getElementById('eye_time')
let rank = document.getElementById('rank')
let user_uid
let user_info = []


// const firebaseConfig = {
//     /* firebase config */
// }

// 初期化は一度だけ
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

document.addEventListener('DOMContentLoaded', function () {

    firebase.auth().onAuthStateChanged(function(user) {
        
        if (user) {
            user_uid = user.uid
            db.collection("users").doc((user_uid)).get().then((docs) => {
           
                if (docs.exists) {
                    user_info=docs.data();
                    user_name.innerHTML = "こんにちは"+user_info.name+"さん"
                    eye_time.innerHTML = "視聴時間："+user_info.time+"時間"
                    rank.innerHTML = "ランキング："+user_info.state+"位"
                }
            }).catch(error => {
                console.log(error)
            })
        } else {
            location.href = "./";
        }

    });

});



/*
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
*/


 ///////////////////////////////////

 var today = new Date();
 let i = 0
 let render_days = document.getElementById('date0') 
 let day_html =''
 day_html +='<div class="parent">'
 console.log(render_days)
 const startDate = new Date(year, month - 1, 1) // 月の最初の日を取得
 const endDate = new Date(year, month,  0) // 月の最後の日を取得
 const endDayCount = endDate.getDate() // 月の末日
 const lastMonthEndDate = new Date(year, month - 1, 0) // 前月の最後の日の情報
 const lastMonthendDayCount = lastMonthEndDate.getDate() // 前月の末日
 const startDay = startDate.getDay() // 月の最初の日の曜日を取得
 ​
 ​
 ​
 for(i =6;i>=0;i--){
 ​
     if (w == 0 && d < startDay) {
         // 1行目で1日の曜日の前
         let num = lastMonthendDayCount - startDay + d + 1
         calendarHtml += '<td class="is-disabled">' + num + '</td>'
     } else if (dayCount > endDayCount) {
         // 末尾の日数を超えた
         let num = dayCount - endDayCount
         calendarHtml += '<td class="is-disabled">' + num + '</td>'
         dayCount++
     } else {
         day_html += "<div class='child'>"+month+"/"+day+"</div>"
     }
     
 ​
     if (w == 0 && d < startDay) {
         // 1行目で1日の曜日の前
         let num = lastMonthendDayCount - startDay + d + 1
         calendarHtml += '<td class="is-disabled">' + num + '</td>'
     } 
         let day = today.getDate() -i
         let month = today.getMonth() +1;
         day_html += "<div class='child'>"+month+"/"+day+"</div>"
 }
 day_html +="</div>"
 console.log(render_days);
 ​
 render_days.innerHTML = day_html



/////////////////////////////////////////////////////////////////////////////////////

