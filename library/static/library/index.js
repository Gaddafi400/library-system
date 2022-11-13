// // setup nav
// const navBtn = document.getElementById("nav-btn");
// const navbar = document.getElementById("navbar");
// const navClose = document.getElementById("nav-close");

// // show nav
// navBtn.addEventListener("click", () => {
//   navbar.classList.add("showNav");
// });
// // close nav
// navClose.addEventListener("click", () => {
//   navbar.classList.remove("showNav");
// });
// // setup date

// clearInput
const getElement = (selector) => {
  const el = document.querySelector(selector);
  if (el) return el;
  throw new Error(`Please check your classes : ${selector} does not exist`);
};

const navToggle = getElement(".nav-toggle");
const links = getElement(".links");

navToggle.addEventListener("click", function () {
  links.classList.toggle("show-links");
});


const date = (document.getElementById("date").innerHTML =
   new Date().getFullYear());
