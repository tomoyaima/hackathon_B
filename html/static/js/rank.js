const db = firebase.firestore();
// let user_name = document.getElementById('user_name')
// let eye_time = document.getElementById('eye_time')
// let rank = document.getElementById('rank')
// let login_count = document.getElementById('login_count')
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
            db.collection("users").get().then((docs) => {
           
                if (docs.exists) {
                    console.log(docs)
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
                   

                }
            }).catch(error => {
                console.log(error)
            })
        } else {
            location.href = "/login.html";
        }

    });

});