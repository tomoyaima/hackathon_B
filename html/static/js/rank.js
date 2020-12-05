const db = firebase.firestore();
let user_uid
let user_info = []
let time =0
let interval_id =null;
let table = document.getElementById("container")

let table_tr="<table id = 'container'><tr><th>" + "順位" + "</th><th>"  + "名前" + "</th><th>" + "時間(秒)"  + "</th></tr>"
let i=0
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
            db.collection("users").orderBy("total_time","desc").get().then((docs) => {
              let time=0;
              let minute=0;
              let seconds=0;
              console.log(docs.docs.length)
              docs.forEach(function(doc){
                var data=doc.data();
                i+=1
                minute = Math.floor(data.total_time/60.0)
                seconds = data.total_time%60
                table_tr+="<tr><td>" + i + "位</td><td>" + data.name + "</td><td>" + minute+"分"+ seconds+"秒"+ "</td></tr>"      
              })
 
              table_tr+="</table>"
              console.log(table_tr)
              table.innerHTML =table_tr
        
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