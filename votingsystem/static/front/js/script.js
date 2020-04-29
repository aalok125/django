
// Navbar Script
function openNav() {
    document.getElementById("myNav").style.height = "100%";
    
  }
  
  
  function closeNav() {
    document.getElementById("myNav").style.height = "0%";
  }

//   category slider
$('.category-nav').slick({
    infinite: true,
    slidesToShow: 4,
    slidesToScroll: 2,
    responsive: [
        {
          breakpoint: 1024,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 2,
            infinite: true,
           
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 2
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 2
          }
        }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
  });
// category scroll
			$(".category-nav .nav-link").on("click", function () {
				$(".category-nav .nav-link").removeClass("active");
				var id = $(this).attr("data-target");
				// console.log('id is '+id);
				$(".panel-collapse").removeClass("in");
				$(id).addClass("in");
				$(this).addClass("active");
			});