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
        }

    });

});

function logout() {
    firebase.auth().signOut().then(() => {
      console.log('ログアウトしました')
      alert('ログアウトしました')
      location.href = "./login.html";
    }).catch((error) => {
      console.log('ログアウト失敗', error);
      alert('ログアウト失敗')
    })
}


 // db.collection("users").doc(user_uid).get({ 
    //     id: user_info.user.uid,
    //     mail: email,
    //     name: user,
    //     state:0,
    //     time:0
    
    // })
    // .then(docRef => {
    //     console.log(docRef);
    //     // success
    // }).catch(error => {
    //     // error
    //     console.log(error);
    
    // })