
var change_name = document.querySelector(".change_name")
var post = document.querySelector(".post")
var submit = document.querySelector(".submit")
var empt = document.querySelector(".empt")
var textarea = document.querySelector("#textarea")

function editP(){
    change_name.innerHTML = "Riuzaki";
    console.log(change_name)
}


function empty(){
    if (post.length === 0){
    empt.innerHTML = "Please fill the box";
    console.log(post);
    post.remove()
    }
    
}


function posting(){
    submit.innerHTML = "Post submitted successfully!";
    console.log(post)
    post.remove();
}




let accept = document.querySelector(".image")
let accepted = document.querySelector(".username")
let accept1 = document.querySelector(".image1")
let accepted1 = document.querySelector(".username1")
let sw = document.querySelector(".sw")
let sw1 = document.querySelector(".sw1")

function remove() {
    accepted.remove();
    accept.remove();
    sw.remove();
}

function remove1() {
    accepted1.remove();
    accept1.remove();
    sw1.remove();
}

var decrease = 2;
var countElementt = document.querySelector(".crequest");
function subtract1() {
    decrease--
    countElementt.innerHTML = "Connection Request " + decrease;
    console.log(decrease);
}


var count = 20;
var count_1 = document.querySelector('#num_1')

function add1(){
    count++
    count_1.innerHTML = "Your Connections " + count;
    console.log(count);
}

var count_2 = 0;
var count_3 = 0;
var count_4 = 0;
var countElement = document.querySelector(".likes")
var countElement1 = document.querySelector(".likes1")
function add2(){
    count_2 = 1
    decrease1 = 0;
    countElement.innerHTML =  "Likes " + count_2;
    decreaseElement.innerHTML = "Dislikes " + decrease1;
    console.log(count_2);
    console.log(decrease1)
    } 
    

function add3() {
    count_3= 1;
    decrease2 =0;
    countElement1.innerHTML =  "Likes " + count_3;
    decreaseElement1.innerHTML = "Dislikes " + decrease2;
    console.log(decrease2);
    console.log(count_3);
}


var countElement2 = document.querySelector(".likes2")
function add4() {
    count_4 = 1;
    decrease3 = 0;
    countElement2.innerHTML =  "Likes " + count_4;
    decreaseElement2.innerHTML = "Dislikes " + decrease3;
    console.log(decrease3);
    console.log(count_4);
}




var decrease1 = 0;
var decrease2 = 0;
var decrease3 = 0;
var decreaseElement = document.querySelector(".dislikes")
var decreaseElement1 = document.querySelector(".dislikes1")
var decreaseElement2 = document.querySelector(".dislikes2")
function subtract2(){
    decrease1 = 1;
    count_2 = 0;
    decreaseElement.innerHTML = "Dislikes " + decrease1;
    countElement.innerHTML =  "Likes " + count_2;
    console.log(count_2);
    console.log(decrease1)
}

function subtract3() {
    count_3 = 0;
    decrease2 =1;
    decreaseElement1.innerHTML = "Dislikes " + decrease2;
    countElement1.innerHTML =  "Likes " + count_3;
    console.log(count_3);
    console.log(decrease2);
}

function subtract4() {
    count_4 = 0;
    decrease3 =1;
    decreaseElement2.innerHTML = "Dislikes " + decrease3;
    countElement2.innerHTML =  "Likes " + count_4;
    console.log(count_4);
}



function load(){
    alert('loading more connections');
}