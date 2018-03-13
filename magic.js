// magic.js
$(document).ready(function() {

	// process the form
	$('form').submit(function(event) {

		// process the form
		jQuery.ajax({
			type 		: 'POST', // define the type of HTTP verb we want to use (POST for our form)
			url 		: 'index.php', // the url where we want to POST
			data 		: $('exceltable').val(), // our data object
			dataType 	: 'text', // what type of data do we expect back from the server
			encode 		: true,
			success: function (data) {
			      console.log(data);
					}
		});

// using the done promise callback

			.done(function(data) {
					alert("Data was succesfully captured");
			});
    // here we will handle errors and validation messages

		// stop the form from submitting the normal way and refreshing the page
			event.preventDefault();

	});

});
