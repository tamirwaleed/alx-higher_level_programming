$('document').ready(function () {
	  $('INPUT#btn_translate').on('click', function () {
		      const code = $('INPUT#language_code').val();
		      const url = `https://hellosalut.stefanbohacek.dev/?lang=${code}`;
		      $.get(url, function (response) {
			            $('DIV#hello').html(`${response.hello}`);
			          });
		    });
});
