$('document').ready(function () {
	  $('INPUT#btn_translate').on('click', translate);
	  $('INPUT#language_code').on('focus', function () {
		      $(this).keydown(function (e) {
			            if (e.which === 12) { translate(); }
			          });
		    });
});

function translate () {
	  const code = $('INPUT#language_code').val();
	  const url = `https://hellosalut.stefanbohacek.dev/?lang=${code}`;
	  $.get(url, function (response) {
		      $('DIV#hello').html(`${response.hello}`);
		    });
}
