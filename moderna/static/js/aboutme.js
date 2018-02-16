$(function() {
  var text = $(".text");
  $(window).scroll(function() {
    var scroll = $(window).scrollTop();

    if (scroll >= 1) {
      text.removeClass("hidden");
    } else {
      text.addClass("hidden");
    }
  });
});
