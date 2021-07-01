$('.like').click(function(event){
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
        if (response.liked) {
          $("#likebtn" + id).css("color", "red");
        } else {
          $("#likebtn" + id).css("color", "green");
        }
      },
	});
});


