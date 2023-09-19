$('#add_item').on('click', () => {
	const newElement = $('<li>').text('Item');
	newElement.appendTo('.my_list');
});
