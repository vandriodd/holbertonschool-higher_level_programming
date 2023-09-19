const languageCode = $('#language_code');
const btnTranslate = $('#btn_translate');
const helloElement = $('#hello');

function translate() {
  const selectedLanguage = languageCode?.val() || 'en';
  let url = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`;

  $.ajax({
    url: url,
    success: (data) => {
      if (data?.hello) helloElement.text(data.hello);
      else helloElement.text('Translation not found');
    }
  });
}

btnTranslate.on('click', () => {
  translate();
});

languageCode.keypress((key) => {
  if (key.keyCode === 13) translate();
});
