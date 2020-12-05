const db = firebase.firestore();
let user_uid
let user_info = []
let time =0
let interval_id =null;
let table = document.getElementById("container")

let table_tr="<table id = 'container'><tr><th>" + "順位" + "</th><th>"  + "ID" + "</th><th>" + "時間"  + "</th></tr>"
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
             
              console.log(docs.docs.length)
              docs.forEach(function(doc){

                var data=doc.data();
                console.log(doc.data())
                i+=1
                table_tr+="<tr><td>" + i + "位</td><td>" + data.name + "</td><td>" + data.total_time + "</td></tr>"
                console.log(doc.data())
               
                // for(let i=0;i<data.time.start.length;i++){
                //   time= data.time.end[i].seconds - data.time.start[i].seconds
                //   data.total_time += time
                  
                // }
                
              })
              

              table_tr+="</table>"
              console.log(table_tr)
              table.innerHTML =table_tr
              // docs.sort(function(a,b){
              //   if(a.total_time > b.total_time) return -1;
              //   if(a.total_time < b.total_time) return 1;
              //   return 0;
              // })
             
        
            }).catch(error => {
                console.log(error)
            })
        } else {
            location.href = "/login.html";
        }

    });

});