document.addEventListener("DOMContentLoaded", function () {
  showLoader(); // Show loader when the DOM content is loaded
});

window.addEventListener("load", function () {
  hideLoader(); // Hide loader when all content (including images, etc.) is loaded
});

function showLoader() {
  document.querySelector(".loader-wrapper").style.display = "flex";
  document.querySelector(".content").style.display = "none";
}

function hideLoader() {
  document.querySelector(".loader-wrapper").style.display = "none";
  document.querySelector(".content").style.display = "block";
}
