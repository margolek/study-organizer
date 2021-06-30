$('.reactions').click(function(){
	console.log('Elo')
	$.ajax({
		url: "{% url 'posts:like' %}",
		type: 'POST',
		data: {'csrfmiddlewaretoken': '{{ csrf_token }}',
			   'id':$(this).attr('id')},
		dataType: "json",
	});
});
