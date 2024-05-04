// $(document).ready(function() {
//     // var homeinfoContainer = $('#homeinfo');
//     // Проверяем, пуст ли блок с id="homeinfo"
//     // if(homeinfoContainer.children().length === 0) {
//     //     $('#content-container').load(static_url + "html/homeinfo.html");
//     // }

//     var navContainer = $('#nav-container');
//     // Проверяем, пуст ли блок с id="nav-container"
//     if(navContainer.children().length === 0) {
//         $('#nav-container').load(static_url + "html/nav.html", function() {
//             // Загружаем обработчики после загрузки nav    
//             // $("#homepage").click(function() {
//             //     $('#content-container').load(static_url + "html/homeinfo.html");
//             // });
            
//             $("#about-btn").click(function() {
//                 $('#content-container').load(static_url + "html/about.html", function() {
//                     $.getScript(static_url + "js/author_info_load.js", function() {
//                     });
//                 });
//             });

//             $("#upload").click(function() {
//                 $('#content-container').load(static_url + "html/upload.html", function() {
//                     $.get(get_csrf_token_url, function(data) {
//                         var csrfToken = data.csrf_token;
//                         $('#content-container').find('form').prepend('<input name="csrfmiddlewaretoken" value="' + csrfToken + '" />')
//                     })
//                 });
//             });
            
//         });
//     }


// });
$("#upload_html").click(function() {
    $('#content_load').load(static_url + "html/test.html");
});