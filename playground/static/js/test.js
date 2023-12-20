var vidcontainer=document.getElementById("vidcontr")
var plusbtn=document.getElementById("start-stream-btn");
var srchbtn=document.getElementById("search-button");

var animbtn=document.getElementByClassName("animationBtn");
animbtn.addEventListener("click", e => {
    window.open("https://www.codechef.com/","_blank");
  });

var drambtn=document.getElementByClassName("dramaBtn");
drambtn.addEventListener("click", function(e) {
    window.open("www.google.com","_blank");
    });

var musicbtn=document.getElementByClassName("musicBtn");
musicbtn.addEventListener("click", function(e) {
    window.open("www.google.com","_blank");
      });

var cinembtn=document.getElementByClassName("cinemaBtn");
cinembtn.addEventListener("click", function(e) {
     window.open("www.google.com","_blank");
        });

//function add(){
//    let html=`
//    <div class="video-box">
//    <video src="nani.mp4" controls></video>
//  </div>
//    `;
//    vidcontainer.innerHTML+=html;
//}


function search {
	var inptxt=document.getElementById("search-input");
	var srchtxt=inptxt.value;
	var srchcont=document.getElementById("search-container");
	var frm=document.getElementById("frm");
	var uurl="{%url 'playground/online/' %}";
	uurl+=srchtxt;
	frm.setAttribute("action",uurl);
	srchcont.innerHTML=html;
}
plusbtn.addEventListener("click",add);
srchbtn.addEventListener("click",search);

