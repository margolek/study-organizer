$('.like, .supers, .dislike').click(function(event){
	var id = $(this).attr('id');
	var href = $(this).find("a").attr("href");
	event.preventDefault();
	$.ajax({
		url: href,
		type: 'POST',
		dataType: 'json',
		data: {'content_id': id,
			   'csrfmiddlewaretoken': "{{ csrf_token }}",
			  },
      	success: function (response) {
      	switch (response.type){
      		case 'super':
        	if (response.supers_status) {
          	$("#superbtn" + id).html('<span class="material-icons reactions">favorite</span>');
        	} else{
          	$("#superbtn" + id).html('<span class="material-icons reactions">favorite_border</span>');
        	}
      			break;
      		case 'like':
		 	if (response.like_status) {
	          $("#likebtn" + id).html('<span class="material-icons reactions">thumb_up</span>');
	        } else{
	          $("#likebtn" + id).html('<span class="material-icons reactions">thumb_up_off_alt</span>');
	        }
      			break;
      		case 'dislike':
			if (response.dislike_status) {
	          $("#dislikebtn" + id).html('<span class="material-icons reactions">thumb_down</span>');
	        } else {
	          $("#dislikebtn" + id).html('<span class="material-icons reactions">thumb_down_off_alt</span>');
	        }
      			break;
      	}
      },
	});
});


