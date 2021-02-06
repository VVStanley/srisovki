wstanley = {

    getCookie: function (name) {
        // Возвращаем куку по имени
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    },

    /** Всплывающие подсказки */
    jG_notifications_warning: function(header, message) {
        $.jGrowl(message, {
            header: header,
            theme: 'bg-warning alert-styled-left',
            position: 'top-right',
        });
    },

    jG_notifications_success: function(header, message) {
        $.jGrowl(message, {
            header: header,
            theme: 'bg-success alert-styled-left',
            position: 'top-right',
        });
    },
}