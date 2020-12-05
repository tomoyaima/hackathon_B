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


var lineChartData = {
    //x軸の情報
    labels : ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'],
    //各グラフの情報。複数渡すことができる。
    datasets : [
      {
        //rgba(220, 220, 220, 1)は、rgbと透過度。
  
        //線の色。ポイントの色を省略すると線の色と同じになる。
        strokeColor : "rgba(220, 220, 220, 1)",      
        //線の下側の色
        fillColor : "rgba(220, 220, 220, 0.5)",
        //ポイントの色
        pointColor : "rgba(220, 220, 220, 1)",
        //ポイントの枠の色
        pointStrokeColor : "rgba(220, 220, 220, 1)",
        //実際のデータ
        data : [1, 59, 90, 81, 56, 55, 40, 30, 10, 40, 48, 58],
        //凡例名
        'label'=>'data1'
      },
      {
        fillColor : "rgba(151, 187, 205, 0.5)",
        strokeColor : "rgba(151, 187, 205, 1)",
        pointColor : "rgba(151, 187, 205, 1)",
        pointStrokeColor : "#fff",
        data : [28, 48, 40, 19, 96, 27, 100, 33, 63, 31, 64, 51],
        'label'=>'data2'
      }
    ]
  }
  
  var option = {
    //縦軸の目盛りの上書き許可。これ設定しないとscale関連の設定が有効にならないので注意。
    scaleOverride : true,
  
    //以下設定で、縦軸のレンジは、最小値0から5区切りで35(0+5*7)までになる。
    //縦軸の区切りの数
    scaleSteps : 7,
    //縦軸の目盛り区切りの間隔
    scaleStepWidth : 5,
    //縦軸の目盛りの最小値
    scaleStartValue : 0,
  
    //アニメーション設定
    animation : false,
  
    //Y軸の表記（単位など）
    scaleLabel : "<%=value%>A",
  
    //ツールチップ表示設定
    showTooltips: false,
  
    //ドットの表示設定
    pointDot : false,
  
    //線を曲線にするかどうか。falseで折れ線になる。
    bezierCurve : false
  
    //凡例
    legendTemplate : "<% for (var i=0; i<datasets.length; i++){%><span style=\"background-color:<%=datasets[i].strokeColor%>\">&nbsp;&nbsp;&nbsp;</span>&nbsp;<%if(datasets[i].label){%><%=datasets[i].label%><%}%><br><%}%>"
  }
  
  //jQueryオブジェクト[0]とすれば、getContext("2D")できる。
  var ctx = $('#lineChartCanvas')[0].getContext("2d");
  //グラフ描画
  var char = new Chart(ctx).Line(lineChartData,option);
  //凡例のhtmlを取得して設定
  $('#chart_legend').html(chart.generateLegend());

  var a = 10;
  console.log(a);




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