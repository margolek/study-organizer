	var state ={	
		'items':[],
		'values':[],
	}

	var objId = "{{question.id}}"

	var dataURL = `/polls/resultsdata/${objId}/`
	$.ajax({
		method:'GET',
		url:dataURL,
		success:function(response){
			console.log('RESPONSE:', response)
			for (var i in response){

				var key = Object.keys(response[i])[0]
				var value = Object.values(response[i])[0]

				state.items.push(key)
				state.values.push(value)
			}

			console.log('STATE:', state)
			buildChart()

		}
	})

	function buildChart(){
			var chartData = {
			"type":"bar",
			"scale-x":{
				"values":state.items
			},
			"series":[
				{
					"values":state.values
				}
			]
		}


		zingchart.render({
		  id: "myChart",
		  data: chartData,
		});
	}