$(document).ready(function() {

	// $("#units-list").change(function() {
	// 	$.ajax({
	// 		url: "/unit-change",
	// 		type: "GET",
	// 		data: {item_price: $(".item-price").text(), unit_selected: $("#units-list option:selected").text()},
	// 		success: function(data) {
	// 			var virtual_price = jQuery.parseJSON(data);
	// 			console.log(virtual_price);
	// 		},
	// 		error: function(data) {
	// 			alert("error");
	// 		}
	// 	});
	// });
	

	$("#stumble").click(function() {

		$(document).ajaxStart(function() {
			$(".item-name").hide();
			$("#loader").show();
		});

	$(document).ajaxStop(function() {
		$(".item-name").show();
		$("#loader").hide();
	});

		$.ajax({
			url: "/bit-item",
			type: "get",
			success: function(data) {
				console.log(data)
				var item = jQuery.parseJSON(data);

				$(".item-name").text(item.item_name);
				$(".item-USD").text(item.item_USD);
				$(".item-BTC").text(item.item_BTC);
				$(".item-mBTC").text(item.item_mBTC);
				$(".item-img").attr("src", "static/img/" + item.imgfile);
				console.log(item.item_name);

			},
			error: function(data) {
				alert('error');
			}

		});

	});

});