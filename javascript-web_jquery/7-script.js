const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.ajax({
	url: url,
	success: (data) => {
		const characterName = data.name;
		$('#character').text(characterName);
	},
});
