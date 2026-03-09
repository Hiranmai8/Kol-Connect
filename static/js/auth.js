// Simple login validation

document.addEventListener("DOMContentLoaded", function(){

const form = document.querySelector("form");

if(form){

form.addEventListener("submit", function(e){

const email = document.querySelector("input[name='email']").value;
const password = document.querySelector("input[name='password']").value;

if(email === "" || password === ""){
alert("Please fill all fields");
e.preventDefault();
}

});

}

});
function showToast(message){

let toast = document.createElement("div");
toast.className = "toast";
toast.innerText = message;

document.body.appendChild(toast);

setTimeout(()=>{
toast.classList.add("show");
},100);

setTimeout(()=>{
toast.remove();
},3000);

}