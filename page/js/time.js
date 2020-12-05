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

//bit coin

 // WebSocket
var sock = new WebSocket('wss://ws.lightstream.bitflyer.com/json-rpc');
var sock_params = [{
    "method": "subscribe",
    "params": {
        "channel": "lightning_executions_BTC_JPY",
    }
}];
// Websocket message格納用配列
var sock_results = {
    'result': []
}
 
// Websocket 接続
sock.addEventListener('open', function (e) {
    sock.send(JSON.stringify(sock_params));
});
 
// Websocket message受信
sock.addEventListener('message', function (e) {
    data = JSON.parse(e.data)['params'];
    message = data['message'];
    // priceを配列に格納
    sock_results['result']['btc_jpy'] = parseInt(message[message.length - 1]['price'])
});
 
// Chart.js
ctx_btc_jpy = document.getElementById('btc_jpy').getContext('2d');
 
chart_btc_jpy = new Chart(ctx_btc_jpy, {
    type: 'line',
    data: {
        datasets: [{
            label: 'BTC/JPY',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgb(255, 99, 132)',
            data: []
        }]
    },
    options: {
        scales: {
            xAxes: [{
                type: 'realtime',
                realtime: {
                    duration: 20000,
                    refresh: 1000, // デフォルト
                    delay: 1000,
                    frameRate: 30, // デフォルト
                    onRefresh: function (chart) {
                        chart_btc_jpy.data.datasets.forEach(function (v, i, datasets) {
                            datasets[i].data.push({
                                x: Date.now(),
                                y: sock_results['result']['btc_jpy']
                            });
                        });
                    }
                }
            }]
        }
    }
});