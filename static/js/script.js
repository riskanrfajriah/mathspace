var swiper = new Swiper('.mySwiper', {
    slidesPerView: 3,
    spaceBetween: 30,
    // slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    centerslide: 'true',
    fade: 'true',
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    breakpoints: {
      0: {
        slidesPerView: 1,
      },
      540: {
        slidesPerView: 2,
      },
      950: {
        slidesPerView: 3,
      },
    },
  });
  
  var scrollSpy = new bootstrap.ScrollSpy(document.body, {
    target: '#navbar-example',
  });
  
  // contact 1
  var btn = document.querySelector('#c-btn');
  var cont = document.querySelector('.popUp');
  
  btn.addEventListener('click', function () {
    cont.id = 'show';
  });
  
  cont.addEventListener('click', function (e) {
    if (e.target == this) {
      this.id = 'hidden';
    }
    e.preventDefault;
  });