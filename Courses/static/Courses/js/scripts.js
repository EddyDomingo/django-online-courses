
$("#RegisterLink").click(function(){
    $("#formEddy").slideToggle("slow");
  });

function userInfo(){

    const form = document.getElementById("formEddy");
    var text = "";
    var i;
    for (i = 0; i < form.length ;i++) {
        text += form.elements[i].value + "<br>";
      }
    var user = text.replace(/\<br\>/g," ");
    var userSplit = user.split(" ");

    console.log(userSplit[1]);
    console.log(userSplit[2]);
    console.log(userSplit[3]);

    if (typeof(Storage) !== "undefined") {
    // Store


        localStorage.setItem("First Name", userSplit[1]);
        localStorage.setItem("Last Name", userSplit[2]);
        localStorage.setItem("Last Name", userSplit[3]);

       document.getElementById("userInfo").innerHTML = localStorage.getItem("First Name") + " is logged in";

       } else {
         document.getElementById("result").innerHTML = "Sorry, your browser does not support Web Storage...";
       }
}