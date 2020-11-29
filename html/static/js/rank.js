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
        // console.log(user_info.user.uid)
        alert('ログイン完了')
        
      })
      .catch((error) => {
        console.log('ログイン失敗', error);
        alert('ログイン失敗')
      });
}

function logout() {
    firebase.auth().signOut().then(() => {
      console.log('ログアウトしました')
      alert('ログアウトしました')
      document.getElementById('emailVerify').innerHTML = 'ログイン後に確認します'
    }).catch((error) => {
      console.log('ログアウト失敗', error);
      alert('ログアウト失敗')
    })
  }