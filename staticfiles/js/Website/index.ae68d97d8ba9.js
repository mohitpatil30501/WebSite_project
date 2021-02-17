// Loader
$(window).on("load",function(){
	$('.loader-wrapper, .page-wrapper').hide()
	$(".page-wrapper").removeClass("d-none");
	$('.loader-wrapper').fadeIn(500).fadeOut(1000);
	$('.page-wrapper').delay(500).fadeIn(2800)
});
