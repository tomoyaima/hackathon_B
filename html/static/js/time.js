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



for(i =6;i>=0;i--){

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

render_days.innerHTML = day_html

$('#num-bar-0').height(30);
document.getElementById('#num-bar-0').style.height = "300px";




///////////////////////



  ///////////////////////

<script>
  var barChartData = {
    labels : ["田中","山田","奥谷","ザビエル","おそ松","ピカチュウ","あひる"],
    datasets : [
      {
        fillColor : /*"#d685b0"*/"rgba(214,133,176,0.7)",
        strokeColor : /*"#d685b0"*/"rgba(214,133,176,0.7)",
        highlightFill: /*"#eebdcb"*/"rgba(238,189,203,0.7)",
        highlightStroke: /*"#eebdcb"*/"rgba(238,189,203,0.7)",
        data : [20,45,1,20,19,33,96]
      },
      {
        fillColor : /*"#7fc2ef"*/"rgba(127,194,239,0.7)",
        strokeColor : /*"#7fc2ef"*/"rgba(127,194,239,0.7)",
        highlightFill : /*"#a5d1f4"*/"rgba(165,209,244,0.7)",
        highlightStroke : /*"#a5d1f4"*/"rgba(165,209,244,0.7)",
        data : [2,54,77,32,9,78,95]
      }
    ]

  }
  window.onload = function(){
    var ctx = document.getElementById("chart").getContext("2d");
    window.myBar = new Chart(ctx).Bar(barChartData, {
      responsive : true,
      // アニメーションを停止させる場合は下記を追加
      /* animation : false */
    });
  }
</script>