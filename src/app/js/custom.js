jQuery(document).ready(function($) {

    // let width = $(window).width();
    // var height = $(window).height();
    // let content_width = $('.content-wrapper').width();
    // var sidebar_width = $('.sidebar-content').width();
    var menu_change = function() {
        if ($(window).width() < 768) {
            $('.nav.nav-sidebar').find('.nav-item-my.nav-item-submenu')
                .removeClass('nav-item-my').removeClass('nav-item-submenu').removeClass('nav-item-open')
                .addClass('nav-item').addClass('nav-item-submenu')
            $('.nav.nav-group-sub').css('display', '').css('width', '')
        } else {
            $('.nav.nav-sidebar').find('.nav-item.nav-item-submenu')
                .removeClass('nav-item').removeClass('nav-item-submenu').removeClass('nav-item-open')
                .addClass('nav-item-my').addClass('nav-item-submenu')
            $('.nav.nav-group-sub').css('display', '').css('width', $('.content-wrapper').width())
        }
    }

    // Меню
    menu_change();
    window.onresize = function() { menu_change() }

    $('.sitebar_reklama').stick_in_parent({
        parent: '.page-content',
        recalc_every: 1
    });

    /*
        Случайные посты в сайтбаре 
    */
   $('.slick_sidebar_random').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
        arrows: false,
        infinite: false
    });

    /*
        отправляем на принтер
     */
    $('.button-print').click(function(event) {

        img = '<html><body onload="window.print()"><img src=' + $('img.image-print').attr('src') + ' /></body></html>'
        let new_win=window.open('','Print-Window');
        new_win.document.open();
        new_win.document.write(img);
        new_win.document.close();
        setTimeout(function(){new_win.close();},10);
    });
 
    /**
     * При прокрутке страницы, показываем или срываем кнопку
     */
    $(window).scroll(function () {
        // Если отступ сверху больше 50px то показываем кнопку "Наверх"
        if ($(this).scrollTop() > 50) {
            $('.btn-up').fadeIn();
        } else {
            $('.btn-up').fadeOut();
        }
    });

    /** Плавный переход по анкорам */
    $('a.scrollto').on('click', function(e){
        e.preventDefault();
        $('html, body').stop().animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 700);
        return false;
    });
});