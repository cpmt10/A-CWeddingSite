/** Active and inactive responsive nav bar menu */

const toggle = document.getElementsByClassName("toggle-button")[0];
const navLinks = document.getElementsByClassName("nav-links")[0];
const contentArea = document.getElementById("contentArea");

toggle.addEventListener("click", (event) => {
  event.preventDefault();
  navLinks.classList.toggle("active");
  if(contentArea) {
    contentArea[0].classList.toggle("shifted");
  }
});

document.querySelectorAll(".nav-links a").forEach((link) => {
  link.addEventListener("click", (event) => {

    if (document.body.classList.contains('warn-on-leave')) {
      const confirmed = confirm("You have unsaved changes. Are you sure you want to leave this page?");
      if (!confirmed) {
        event.preventDefault();
      }
    }

    if (navLinks.classList.contains("active")) {
      navLinks.classList.remove("active");
    }
  });
});


/** Countown */
var countDownDate = new Date("Dec 27, 2025 15:37:25").getTime();
var x = setInterval(function () {
  var now = new Date().getTime();
  var distance = countDownDate - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("days").innerHTML = days
  document.getElementById("hours").innerHTML = hours
  document.getElementById("minutes").innerHTML = minutes
  document.getElementById("seconds").innerHTML = seconds

  if (distance < 0) {
    clearInterval(x);
    document.getElementById("days").innerHTML = "00"
    document.getElementById("hours").innerHTML = "00"
    document.getElementById("minutes").innerHTML = "00"
    document.getElementById("seconds").innerHTML = "00"
    }
}, 1000);
