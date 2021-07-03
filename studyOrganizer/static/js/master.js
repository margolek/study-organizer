$('.like, .supers, .dislike').click(function(event){
	var id = $(this).attr('id');
	var super_res = parseInt($("#supercnt" + id).text());
	var like_res = parseInt($("#likecnt" + id).text());
	var dislike_res = parseInt($("#dislikecnt" + id).text());
	var href = $(this).find("a").attr("href");
	event.preventDefault(); //Preventing refresh page
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
          	super_res = super_res + 1;
        	} else{
          	$("#superbtn" + id).html('<span class="material-icons reactions">favorite_border</span>');
          	super_res = super_res - 1;
        	}
        	$("#supercnt" + id).html("<b>"+super_res+"</b>");
      			break;
      		case 'like':
		 	if (response.like_status) {
	          $("#likebtn" + id).html('<span class="material-icons reactions">thumb_up</span>');
	          like_res = like_res + 1;
	        } else{
	          $("#likebtn" + id).html('<span class="material-icons reactions">thumb_up_off_alt</span>');
	          like_res = like_res - 1;
	        }
	        $("#likecnt" + id).html("<b>"+like_res+"</b>");
      			break;
      		case 'dislike':
			if (response.dislike_status) {
	          $("#dislikebtn" + id).html('<span class="material-icons reactions">thumb_down</span>');
	          dislike_res = dislike_res + 1;
	        } else {
	          $("#dislikebtn" + id).html('<span class="material-icons reactions">thumb_down_off_alt</span>');
	          dislike_res = dislike_res - 1;
	        }
	        $("#dislikecnt" + id).html("<b>"+dislike_res+"</b>");
      			break;
      	}
      	reaction_cnt = dislike_res + like_res + super_res
      	if (reaction_cnt == 1) {
      		$("#reaction" + id).html(reaction_cnt + " Reaction");
      	}else{
      		$("#reaction" + id).html(reaction_cnt + " Reactions");
      	}
      },
	});
});


