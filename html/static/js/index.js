// import firebase from "firebase/app"
// import "firebase/firestore"
const db = firebase.firestore();
let user_name = document.getElementById('user_name')
let eye_time = document.getElementById('eye_time')
let rank = document.getElementById('rank')
let login_count = document.getElementById('login_count')
let user_uid
let user_info = []
let time =0
let interval_id =null;

// let stream = null;

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
                    let time=0;
                    let total_time=0;
                    console.log(user_info.time)
                    // time.foreach(user_info.time[end]-user_info.time[start])
                    for(let i=0;i<user_info.time.start.length;i++){
                      time= user_info.time.end[i].seconds - user_info.time.start[i].seconds
                      console.log(time)
                      total_time +=time 
                    }
                    console.log(user_info.time)
                    user_name.innerHTML = "こんにちは"+user_info.name+"さん"
                    eye_time.innerHTML = "視聴時間："+total_time+"秒"
                    rank.innerHTML = "ランキング："+user_info.state+"位"
                    login_count.innerHTML = "ログイン回数："+user_info.login_count+"回"

                }
            }).catch(error => {
                console.log(error)
            })
        } else {
            location.href = "/login.html";
        }

    });

});


function logout() {
    firebase.auth().signOut().then(() => {
      console.log('ログアウトしました')
      alert('ログアウトしました')
      location.href = "/login";
    }).catch((error) => {
      console.log('ログアウト失敗', error);
      alert('ログアウト失敗')
    })
}


$(function(){
    const constraints = window.constraints = {
      audio: false,
      video: {
        facingMode: "environment"
      }
    };

  $('#start').click(async function(){
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        const video = document.querySelector('#myvideo');
  
        const videoTracks = stream.getVideoTracks();
        window.stream = stream; 
        video.srcObject = stream;
        e.target.disabled = true;
      } catch{
        $('#errorMsg').text('カメラの使用を許可してください');
      }

  });
  $('#stop').click(function(){
      
        clearInterval(interval_id);
        // stream = navigator.mediaDevices.getUserMedia(constraints);
        interval_id = null;
        const video = document.querySelector('#myvideo');
        const videoTracks = window.stream.getVideoTracks();
        for (let i = 0; i < videoTracks.length; i++){
            videoTracks[i].stop()
          } 
        window.stream = null; 
        location.href = `/stop/${user_uid}`;
        alert('頑張ったね')
        // e.target.disabled = false;
       
  });
  
  
  var canvas = $('#videocanvas')[0];
  
  $('#myvideo').on('loadedmetadata', function(){
    // canvasのサイズ合わせ
     console.log(user_uid);
    var video = $('#myvideo')[0];
    var width = canvas.width = 640
    var height = canvas.height = 480; 
          // 描画先の指定
    var ctx = canvas.getContext("2d");
          // 送信データの作成
    var fd = new FormData();
    fd.append('video', null);
   
          //毎フレーム処理
    interval_id = setInterval(function(){
      ctx.drawImage(video, 0, 0, width, height);
      canvas.toBlob(function(blob){  
        
        fd.set('video', blob);
        // fd.set('watching', true);
        // console.log(blob)
        
        $.ajax({
            url: `/img/${user_uid}`,
            type : "POST",
            processData: false,
            contentType: false,
            data : fd,
            dataType: "text",
        })
        .done(function(data){
            console.log(data);
        })
        .fail(function(data){
            console.log(data);
        });
              }, 'image/jpeg');
          },1000);
      });
  });
  
  const userId = "js-primer-example";
  fetch(`img/${user_uid}`)
      .then(response => {
          console.log(response.status); // => 200
          return response.json().then(userInfo => {
              // JSONパースされたオブジェクトが渡される

              console.log(userInfo); // => {...}
          });
      });

// function video() {
//     //動画流す準備
//     console.log('ログアウトしました')
//     var video = document.getElementById("video");
//     // getUserMedia によるカメラ映像の取得
//     var media = navigator.mediaDevices.getUserMedia({
//         video: true,//ビデオを取得する
//         //使うカメラをインカメラか背面カメラかを指定する場合には
//         //video: { facingMode: "environment" },//背面カメラ
//         video: { facingMode: "user" },//インカメラ
//         audio: false,//音声が必要な場合はture
//     });
//     //リアルタイムに再生（ストリーミング）させるためにビデオタグに流し込む
//     media.then((stream) => {
//         video.srcObject = stream;
//     });
// }

