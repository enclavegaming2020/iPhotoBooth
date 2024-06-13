var col1 = document.querySelector(".col-1")
var signup = document.querySelector("#Sign-up")
var col2 = document.querySelector(".col-2")
var loginmain = document.querySelector(".login-main")
var signupmain = document.querySelector(".signup-main")

signup.addEventListener("click",function(){
    if(col1.style.transform == ""){
        col1.style.transform = "translate(82.25%)"
        col1.style.borderRadius = "30% 0 0 20%"
        col1.style.transition = "transform 1s,border-radius .7s ease .3s";
        signup.innerHTML = "Sign In"
        loginmain.style.display = "none"
        signupmain.style.display = "block"
        signupmain.style.left = "-60%"
        col1.style.zIndex="100"

        signupmain.animate([
            {transform: "translateX(0%)",opacity:0},
            {transform: "translateX(-60%)",opacity:1}
        ],{
            duration: 1000,
            easing:"ease-out",
            fill:"forwards"
        });

    }
    else{
        col1.style.transform = ""
        col1.style.borderRadius = "0 30% 20% 0"
        col1.style.transition = "transform 1s,border-radius .7s ease .3s";
        signup.innerHTML = "Sign Up"
        loginmain.style.display = "block"
        signupmain.style.display = "none"
        loginmain.style.left = "50%"
        col1.style.zIndex = "100"
        loginmain.animate([
            { transform: "translateX(-100%)", opacity: 0 },
            { transform: "translateX(-50%)", opacity: 1 }
          ], {
            duration: 1000,
            easing: "ease-out",
            fill: "backwards"
          });
    }
    }
);
 
msg = document.querySelector(".msg")

if(msg.innerHTML !== ""){
    alert([msg.innerHTML])
}

function togglePassword(){
    var pass = document.querySelector(".Pass");
    if (pass.type === "password"){
        pass.type = "text";
    }else{
        pass.type = "password";
    }
}