const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

$.ajax({
	url: url,
	success: (data) => {
		const movies = data.results;
		const listMovies = $('#list_movies');
		$.map(movies, (movie) => {
			let movieTitle = movie.title;
			console.log(movieTitle);
			let movieElement = $('<li>').text(movieTitle);
			movieElement.appendTo(listMovies);
		});
	},
});
