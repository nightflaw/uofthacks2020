//cursor
// const cursor = document.querySelector('.cursor');
// document.addEventListener('mousemove', e => {
// cursor.setAttribute("style", "top: "+(e.pageY-20)+"px; left: "+(e.pageX-20)+"px")
// })
// document.addEventListener('click',() => {
// cursor.classList.add("expand");
// setTimeout(() => {
//     cursor.classList.remove("expand");
// }, 500)
// })

//smooth scroll

$(document).ready(function() {
  
  var scrollLink = $('.scroll');
  
  // Smooth scrolling
  scrollLink.click(function(e) {
    e.preventDefault();
    $('body,html').animate({
      scrollTop: $(this.hash).offset().top
    }, 1000 );
  });
  
  // Active link switching
  $(window).scroll(function() {
    var scrollbarLocation = $(this).scrollTop();
    
    scrollLink.each(function() {
      
      var sectionOffset = $(this.hash).offset().top - 20;
      
      if ( sectionOffset <= scrollbarLocation ) {
        $(this).parent().addClass('active');
        $(this).parent().siblings().removeClass('active');
      }
    })
    
  })
  
})

//nav bar

const navToggle = document.querySelector('.nav__toggle');

navToggle.addEventListener('click', () => {
document.body.classList.toggle('nav-open');
});