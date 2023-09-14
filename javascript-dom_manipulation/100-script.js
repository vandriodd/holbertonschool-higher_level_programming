// Script that adds, removes and deletes li elements by clicking

document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.getElementById('add_item');
  const removeItem = document.getElementById('remove_item');
  const clearList = document.getElementById('clear_list');
  const myList = document.querySelector('.my_list');

  addItem.onclick = () => {
    const newItem = document.createElement('li');
    newItem.innerHTML = 'Item';
    myList.appendChild(newItem);
  };

  removeItem.onclick = () => {
    const listItems = myList.querySelectorAll('li');
    lastChild = listItems.length - 1;
    myList.removeChild(listItems[lastChild]);
  };

  clearList.onclick = () => {
    myList.innerHTML = '';
  };
});
