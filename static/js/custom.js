document.addEventListener("DOMContentLoaded", function (event) {
  var timer;
  var where = 2;
  var max = parseInt("3");
  var url = window.location;
  var up = document.querySelector("#up");
  var cards = document.querySelector("#articles");
  var spinner = document.querySelector("#spinner");
  window.onscroll = function (ev) {
    setTimeout(function () {
      if (window.scrollY >= 340) {
        up.classList.add("show");
      }
      if (window.scrollY < 340) {
        up.className = "";
      }
    }, 1000);
    up.onclick = function () {
      window.scrollTo(0, 0);
    };
    if (cards !== null) {
      if (where <= max) {
        if (window.innerHeight + window.scrollY <= document.body.offsetHeight) {
          clearTimeout(timer);
          timer = setTimeout(function () {
            var request = new XMLHttpRequest();
            request.open("GET", url + "/page/" + where);
            request.onload = function () {
              var parser = new DOMParser();
              var doc = parser.parseFromString(
                request.responseText,
                "text/html"
              );
              var divs = doc.querySelectorAll("#articles > div");
              for (var index = 0; index < divs.length; index++) {
                cards.appendChild(divs[index]);
              }
              where = where + 1;
            };
            request.send();
          }, 1000);
        }
      } else {
        spinner.innerHTML = "<i>—fin—</i>";
      }
    }
  };
});
