// import firebase from "firebase/app"
// import "firebase/firestore"
const db = firebase.firestore();
// const firebaseConfig = {
//     /* firebase config */
// }

// 初期化は一度だけ
if (!firebase.apps.length) {
    firebase.initializeApp(firebaseConfig);
}

function signup() {
    let user = document.getElementById('user_name').value
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    firebase.auth().createUserWithEmailAndPassword(email, password)
        .then((user_info) => {
            
           
            db.collection("users").doc(user_info.user.uid).set({ 
                id: user_info.user.uid,
                mail: email,
                name: user,
                state:0,
                time:0

            })
            .then(docRef => {
                alert('ユーザー作成完了')
                location.href = "./index.html";
                // success
            }).catch(error => {
                // error
                console.log('ユーザー作成失敗', error);
                alert('ユーザー作成失敗')
            })
        })
      .catch((error) => {
        console.log('ユーザー作成失敗', error);
        alert('ユーザー作成失敗')
    });
}
  
function login() {
    let email = document.getElementById('email').value
    let password = document.getElementById('password').value
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((user_info) => {
          
        console.log('ログイン完了')
        location.href = "./index.html";
        alert('ログイン完了')
        
      })
      .catch((error) => {
        console.log('ログイン失敗', error);
        alert('ログイン失敗')
      });
}
