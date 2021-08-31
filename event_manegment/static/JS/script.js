function myFunction2() {
  var x = document.getElementById("mynavbar");
  var y =document.getElementById("icon");
  if (x.className === "class-navbar") {
    x.className += " responsive";
    y.className += " responsive";
  } else {
    x.className = "class-navbar";
    y.className = "icon";
  }
}

//Get the button
var mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}


// email validate

function validate() {
    var k=email();
    // alert(k);
    if(k){
      k=password_check();
      if(k){
        document.getElementById("submit").style.display="block";
        document.getElementById("sub").style.display="none";
      }
    }

    // password_check();
    
    
  }

    function email(){
      var email=document.getElementById("txtemail").value;
      regx=/^([a-zA-Z0-9\.-_]+)@([a-zA-Z0-9-]+).([a-z]{2,20})(.[a-z]{2,8})$/;
      if(email.trim()==""){
        alert("email is empty");
        return false;
      }
      else{
        if(regx.test(email)){
          alert("email validate");
          document.getElementById("Ibluser").style.visibility="hidden";
          return true;
        }
        else{
          document.getElementById("Ibluser").style.visibility="visible";
          return false;
      }
      }
      
    }



    function  password_check()
    { 
        var passw=document.getElementById("password");
        
         if(passw.value.trim()=="" ){
          alert("password is blank")
          passw.style.border="solid 3px red";
          
          return false;
        }
        else if(passw.value.trim().length<8 ){
          alert("password is too short ")
          password.style.border="solid 3px red";
          
          return false;
        }
        else{
          alert("password length ok");
          var pass2= document.getElementById("password2");
          if(pass2.value==passw.value){
            alert("password confirmed")
            alert("password ok");
          password.style.border="none";
          return true;
          }
          else{
            alert("password not confirmed")
            return false;
          }
          
        }

    function validate(){
      var mobilenumber=document.getElementById("txtmobile").value;
      var range=/[7-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]/;
      //mobile number has 10 digit hence we write [0-9] nine times
      if(range.test(mobilenumber))
      {
        alert("valid mobile number");
        return true;
      }
      else{
        alert("invalid mobile number");
        // document.getElementById("Ibluser").style.visibility="visible";
        return false;
      }
    }


    }


// date restrict

$(function() {
  $('#datetimepicker2').datetimepicker({
    language: 'en',
    pick12HourFormat: true
  });
});

    