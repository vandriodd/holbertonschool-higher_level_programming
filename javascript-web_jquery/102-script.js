const languageCode = $('#language_code');
const btnTranslate = $('#btn_translate');
const helloElement = $('#hello');

btnTranslate.on('click', () => {
  const selectedLanguage = languageCode?.val() || 'en';
  let url = `https://hellosalut.stefanbohacek.dev/?lang=${selectedLanguage}`;

  $.ajax({
    url: url,
    success: (data) => {
      if (data?.hello) helloElement.text(data.hello);
      else helloElement.text('Translation not found');
    }
  });
});
