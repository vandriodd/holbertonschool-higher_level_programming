const url = 'https://hellosalut.stefanbohacek.dev/?lang=f';

$.ajax({
  url: url,
  success: (data) => {
    const helloData = data.hello;
    $('#hello').text(helloData);
  }
});
