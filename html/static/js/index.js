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


function logout() {
    firebase.auth().signOut().then(() => {
      console.log('ログアウトしました')
      alert('ログアウトしました')
      location.href = "/";
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
  
  async function init() {
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
  }
  
  $('#start').click(init);
  
  
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
    setInterval(function(){
      ctx.drawImage(video, 0, 0, width, height);
      canvas.toBlob(function(blob){  
          console.log(user_uid);
        fd.set('video', blob);
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
          },100);
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

