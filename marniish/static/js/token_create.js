$( document ).on('click', '#ajax', function(event) {
    console.log('Шаг 1'); // Чтоб понять, где всё пошло не так
    $.ajax({
        url: '/users/update_token_ajax/',
        success: function (data) { // data - ответ от сервера
            console.log('Шаг 2') // Чтоб понять, где всё пошло не так
            console.log(data); // Что за токен получился, есть ли он
            $('#token').html(data.key); // В теге с id 'token' обновляем содержимое в котором лежит токен по ключу key, полученный из 'data'
        },
    });
});