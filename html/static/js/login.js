// import firebase from "firebase/app"
// import "firebase/firestore"
const db = firebase.firestore();
// const firebaseConfig = {
//     /* firebase config */
// }
const time={
    start:0,
    end:0
}
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
            
                login_count:0,
                time:time


            })
            .then(docRef => {
                alert('ユーザー作成完了')
                location.href = `./index/${user_info.user.uid}`;
                console.log('ユーザー作成成功', user_info.user.uid);

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
            console.log(user_info.user.uid);
            db.collection("users").doc(user_info.user.uid).update({
                login_count: firebase.firestore.FieldValue.increment(1)
                
            }).then(docRef => {

                console.log('ログイン完了')
            
                alert('ログイン完了')
                location.href = `./index/${user_info.user.uid}`;
                // success
            }).catch(error => {
                // error
                console.log('ログイン失敗', error);
                alert('ログイン失敗')
            })
        })
      .catch((error) => {
        console.log('ログイン失敗', error);
        alert('ログイン失敗')
      });
}
