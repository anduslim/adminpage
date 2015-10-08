/*
Name: 			Dashboard

*/

var eventHandler = function(data) {

    console.log("success: content(AK) for node:");


};

var errorHandler = function(xhr) {
    switch (xhr.status) {
      //Shipping rate api error
      case 400:
      console.log("API error: inside xhr:" + xhr.status + " " + $.parseJSON(xhr.responseText)["error_msg"]);

    break;


  }
};

function generateKeys(){
  $.ajax("../test", {
    data: {

    },
    success: eventHandler,
    error: errorHandler
  });
  console.log("Inside function generateKeys");
}

	/* test AJAX */
	function testemail(){
	  $.ajax("../test", {
	    data: {
	    },
	    success: function(data) {
	    	console.log('success!');
	    },
	    error: function(xhr) {
	    	console.log('error!');
	    }
	  });
	  console.log("testemail");
	}


(function( $ ) {




	/*
	Modal Dismiss
	*/
	$(document).on('click', '.modal-dismiss', function (e) {
		e.preventDefault();
		$.magnificPopup.close();
	});

	/*
	Form
	*/
	$('.modal-services').magnificPopup({
		type: 'inline',
		preloader: false,
		focus: '#name',
		modal: true,

		// When elemened is focused, some mobile browsers in some cases zoom in
		// It looks not nice, so we disable it:
		callbacks: {
			beforeOpen: function() {
				if($(window).width() < 700) {
					this.st.focus = false;
				} else {
					this.st.focus = '#name';
				}
			}
		}
	});

	$('.modal-hosts').magnificPopup({
		type: 'inline',
		preloader: false,
		focus: '#name',
		modal: true,

		// When elemened is focused, some mobile browsers in some cases zoom in
		// It looks not nice, so we disable it:
		callbacks: {
			beforeOpen: function() {
				if($(window).width() < 700) {
					this.st.focus = false;
				} else {
					this.st.focus = '#name';
				}
			}
		}
	});

}).apply( this, [ jQuery ]);
