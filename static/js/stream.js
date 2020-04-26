$("document").ready(function(){
    $('form').on('submit', function(event) {
        event.preventDefault();
         var checkBox = document.getElementById("switch1");
        $.ajax({
            data: {
                motor : checkBox.checked,
                angle : $('#angle').val(),
                speed : $('#speed').val()
            },
            type: 'POST',
            url: '/stream'
        })

    });

});
