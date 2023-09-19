const addItem = $('#add_item');
const removeItem = $('#remove_item');
const clearList = $('#clear_list');
const myList = $('.my_list');

addItem.on('click', () => {
  const newItem = $('<li>').text('Item');
  newItem.appendTo(myList);
});

removeItem.on('click', () => {
  myList.find('li:last').remove();
});

clearList.on('click', () => {
  myList.empty();
});
