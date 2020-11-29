  // Your web app's Firebase configuration
  // For Firebase JS SDK v7.20.0 and later, measurementId is optional
  var firebaseConfig = {
    apiKey: "AIzaSyBglYaX00Zlyuw0k2Mh6F09-v1nJeBY8dM",
    authDomain: "hackathon-b-903ff.firebaseapp.com",
    databaseURL: "https://hackathon-b-903ff.firebaseio.com",
    projectId: "hackathon-b-903ff",
    storageBucket: "hackathon-b-903ff.appspot.com",
    messagingSenderId: "370805679019",
    appId: "1:370805679019:web:04bbf452a189fef25c28ee",
    measurementId: "G-Y92ZYE78EN"
  };
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  firebase.analytics();

  document.addEventListener('DOMContentLoaded', function () {
    try {
      let app = firebase.app();
      let features = ['auth', 'database', 'messaging', 'storage'].filter(feature => typeof app[feature] === 'function');
    //   document.getElementById('load').innerHTML = `Firebase SDK loaded with ${features.join(', ')}`;
    } catch (e) {
      console.error(e);
    //   document.getElementById('load').innerHTML = 'Error loading the Firebase SDK, check the console.';
    }
  });